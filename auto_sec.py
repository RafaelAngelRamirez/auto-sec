#!/bin/python

from auto_sec_scan import Scan
import ssh.auto_sec_ssh
target="172.17.0.3"
print(f'[+] Escanendo {target}')

scan = Scan(target)
scan.exec().preview().preview_table()
ssh.auto_sec_ssh.brute_force(target)





