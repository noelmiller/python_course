from typing import Self


class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand = brand
        self.max_speed = max_speed

    # This is a factory method
    # Factory methods are class methods that return an instance of the class
    # Factory methods are used to create objects
    # Factory methods can be used to create objects with default values
    # Factory methods can be used to create objects with default values based on the arguments passed
    @classmethod
    def autogenerate_max_speed(cls, brand: str) -> Self:
        lowered: str = brand.lower()
        max_speed: int = 200

        if lowered == "toyota":
            max_speed = 270
        elif lowered == "bmw":
            max_speed = 290
        elif lowered == "volvo":
            max_speed = 300

        return cls(brand, max_speed)

    def display_info(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Max speed: {self.max_speed}")
        print(f"Limiter: {self.LIMITER}")

def main() -> None:
    # This car will have a max speed of 300
    volvo: Car = Car.autogenerate_max_speed("Volvo")
    volvo.display_info()

    # This car will have the default max speed
    some_car: Car = Car.autogenerate_max_speed("Some car")
    some_car.display_info()
if __name__ == '__main__':
    main()
