class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand = brand
        self.max_speed = max_speed

    # @classmethod is a type hint that tells the developer that this method is a class method
    # Class methods are methods that can be called using the class name
    # This will affect all cars
    # Class methods can access class variables
    @classmethod
    def change_limit(cls, new_limit: int) -> None:
        cls.LIMITER = new_limit

    def display_info(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Max speed: {self.max_speed}")
        print(f"Limiter: {self.LIMITER}")

def main() -> None:
    bmw: Car = Car("BMW", 240)
    toyota: Car = Car("Toyota", 190)

    bmw.display_info()
    toyota.display_info()

    Car.change_limit(250)
    bmw.display_info()
    toyota.display_info()

if __name__ == '__main__':
    main()
