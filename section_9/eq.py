class Car:
    def __init__(self, brand: str, car_id: int, color: str) -> None:
        self.brand = brand
        self.car_id = car_id
        self.color = color

    def __str__(self) -> str:
        return f"{self.brand} {self.car_id} is {self.color}"


    # The standard approach is to use (`other: object`) because:
    # 1. It's compatible with all Python versions
    # 2. It follows the Python data model specification
    # 3. It properly handles cases where `other` might not be of the same type

    def __eq__(self, other: object) -> bool:
        # Make sure the other object is of the same type
        if not isinstance(other, Car):
            return NotImplemented

        # simple example
        # just checks if the car_id is the same
        # return self.car_id == other.car_id

        # more complex example
        # makes sure all the attributes are the same
        print("Current: ", self.__dict__)
        print("Other: ", other.__dict__)
        return self.__dict__ == other.__dict__

def main() -> None:
    car1: Car = Car("BMW", 1, "red")
    car2: Car = Car("BMW", 1, "red")

    # This will print False without the __eq__ dunder method
    # because it is comparing the memory location of the objects
    print(car1 == car2)

if __name__ == '__main__':
    main()
