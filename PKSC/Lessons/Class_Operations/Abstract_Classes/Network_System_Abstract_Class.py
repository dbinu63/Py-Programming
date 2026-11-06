from abc import ABC, abstractmethod

class NetworkSystem(ABC):
    def __init__(self, sys_id, location):
        self.sys_id = sys_id
        self.location = location

    @abstractmethod
    def show_detail(self):
        pass

class LAN(NetworkSystem):
    def __init__(self, sys_id, location, device):
        super().__init__(sys_id, location)
        self.device = device

    def show_detail(self):
        print(f"System ID: L{self.sys_id}")
        print(f"Location: {self.location}")
        print(f"Device: {self.device}")

class WAN(NetworkSystem):
    def __init__(self, sys_id, location, bandwidth):
        super().__init__(sys_id, location)
        self.bandwidth = bandwidth

    def show_detail(self):
        print(f"System ID: W{self.sys_id}")
        print(f"Location: {self.location}")
        print(f"Bandwidth: {self.bandwidth}")


def main():
    lan = LAN("001", "Building 1", "Router")
    wan = WAN("002", "Dallas", "5 GBPS")

    lan.show_detail()
    print()
    wan.show_detail()


if __name__ == "__main__":
    main()