class Connection:
    def __init__(self, connection_type: str, cost: float) -> None:
        print(f"{connection_type} connection established. (Cost: ${cost}/h)")
        self.connection_type = connection_type
        self.cost = cost

    def close_connection(self) -> None:
        print(f"{self.connection_type} connection closed.")

def main() -> None:
    internet: Connection = Connection("Internet", 2) # object instantiation
    satellite: Connection = Connection("Satellite", 5) # another object instantiation

    internet.close_connection() # method call
    satellite.close_connection() # another method call


if __name__ == '__main__':
    main()
