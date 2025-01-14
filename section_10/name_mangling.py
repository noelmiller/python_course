class Car:
    # This is a private variable
    __YEAR: int = 2000

    # note that this is a class variable and should only be used there
    # It is a naming convention to use _ for class variables
    # This will not name mangle the variable
    _YEAR: int = 2000

    def __init__(self, brand: str, fuel_type: str) -> None:
        self.__brand = brand
        self.__fuel_type = fuel_type
        self.__var: str = "red"

        # Having this not be private could lead to a breaking change
        # self.var: str = "red"

    def drive(self) -> None:
        print(f"{self.__brand} is driving")

    def __get_description(self) -> None:
        print(f"Brand: {self.__brand}")
        print(f"Fuel type: {self.__fuel_type}")

    def display_colour(self) -> None:
        print(f"{self.__brand} is {self.__var.capitalize()}")

class Toyota(Car):
    def __init__(self, fuel_type: str) -> None:
        super().__init__("Toyota", fuel_type)
        # breaking change to the parent class
        self.var = 100

    def get_year(self) -> int:
        # This won't work because __YEAR is a private variable to the Car class
        # return self.__YEAR
        return self._YEAR

def main() -> None:
    toyota: Toyota = Toyota("Electric")
    toyota.display_colour

    # Would break if self.var is set to an integer because it's overridden in the parent class
    # toyota.display_colour()

    car: Car = Car("Toyota", "Electric")
    car.drive()

    # This will raise an AttributeError
    # This is because __brand is a private variable to the Car class
    # print(car.__get_description())


    # The linter will raise a warning here
    # This is because __YEAR is a private variable to the Car class
    # get_description is a private method to the Car class
    # __brand is a private variable to the Car class
    print(car._Car__brand)
    car._Car__get_description()
    print(car._Car__YEAR)

if __name__ == '__main__':
    main()
