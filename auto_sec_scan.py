import nmap
from prettytable import from_csv
import io

class Scan:
    target = "127.0.0.1"
    ports = "1-5000"
    scanner = None

    def __init__(self, target=target, ports=ports):
        self.target = target
        self.ports = ports

    def exec(self):
        self.scanner = nmap.PortScanner()
        self.scanner.scan(self.target, self.ports)
        self.order_data()
        return self

    def order_data(self):
        pass

    def preview(self):
        for host in self.scanner.all_hosts():
            print("Host: ", host)
            print("State: ", self.scanner[host].state())
            for proto in self.scanner[host].all_protocols():
                print("Protocol: ", proto)
                ports = self.scanner[host][proto].keys()
                for port in ports:
                    print(
                        "Port: ",
                        port,
                        "State: ",
                        self.scanner[host][proto][port]["state"],
                    )
        return self

    def preview_table(self):
        csv = self.scanner.csv()
        file = io.StringIO(csv)
        print(from_csv(file))
        file.close()
        return self
