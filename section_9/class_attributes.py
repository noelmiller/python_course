class Car:
    SPEED_LIMIT_KM: float = 140 # every class will have access to this attribute

    def __init__(self, brand: str) -> None:
        self.brand = brand

    def drive(self, *, speed: float) -> None:
        if speed > self.SPEED_LIMIT_KM:
            print(f"limiter activated: driving at {self.SPEED_LIMIT_KM}km/h")
        else:
            print(f"driving at {speed}km/h")

# dangerous use of class attributes
class Animal:
    tricks: list[str] = [] # every instance of the class will have access to this attribute

    def __init__(self, name: str) -> None:
        self.name = name
        # to fix this issue, we need to initialize the attribute in the __init__ method
        # self.tricks: list[str] = []

    def teach_trick(self, trick_name: str) -> None:
        self.tricks.append(trick_name)

def main() -> None:
    toyota: Car = Car('toyota')
    bmw: Car = Car('bmw')
    bmw.drive(speed=200) # limiter activated: driving at 140km/h
    toyota.drive(speed=200) # limiter activated: driving at 140km/h
    Car.SPEED_LIMIT_KM = 170 # changing the class attribute. This will change the attribute for all instances of the class
    bmw.drive(speed=200) # limiter activated: driving at 170km/h
    toyota.drive(speed=200) # limiter activated: driving at 170km/h

    # dangerous use of class attributes
    dog: Animal = Animal('Helios')
    cat: Animal = Animal('Boomer')

    cat.teach_trick("wash dishes")
    cat.teach_trick("get a job")
    print(cat.tricks) # ['wash dishes', 'get a job']

    dog.teach_trick("sit")
    dog.teach_trick("stay")
    print(dog.tricks) # ['wash dishes', 'get a job', 'sit', 'stay'] # this is not what we want
    print(cat.tricks) # ['wash dishes', 'get a job', 'sit', 'stay'] # this is not what we want

if __name__ == '__main__':
    main()
