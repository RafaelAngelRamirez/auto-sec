class Credential:
    port = None
    module = None
    host = None
    login = None
    passwd = None

    def _valid_fields(self):
        return [
            "port",
            "module",
            "host",
            "login",
            "passwd",
        ]

    def parse_from_hydra(data):
        for field in self._valid_fields():
            if field in data:
                self[field] = data.get(field)
