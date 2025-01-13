class Car:
    def __init__(self, brand: str, wheels: int) -> None:
        self.brand = brand
        self.wheels = wheels

    def turn_on(self) -> None:
        print(f"{self.brand} is now on.")

    def turn_off(self) -> None:
        print(f"{self.brand} is now off.")

    def drive(self, mi: float) -> None:
        print(f"{self.brand} is driving for {mi} miles.")

    def describe(self) -> None:
        print(f"{self.brand} has {self.wheels} wheels.")

def main() -> None:
    bmw: Car = Car("BMW", 4)
    bmw.turn_on()
    bmw.drive(100)
    bmw.turn_off()
    bmw.describe()

    volvo: Car = Car("Volvo", 6)
    volvo.turn_on()
    volvo.drive(200)
    volvo.turn_off()
    volvo.describe()

if __name__ == "__main__":
    main()
