# methods are bound to a class
class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        print(f"Connecting to {self.host} on port {self.port}")

    def close(self):
        print(f"Closing connection to {self.host} on port {self.port}")

# functions are not bound to a class
def connect(connection_type: str) -> None:
    print(f"Connecting to {connection_type}")
