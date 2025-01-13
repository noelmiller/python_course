class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # It is recommended to use __str__ instead of __repr__ because it is more user friendly and you can still use __repr__ to get the memory location of the object
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    # This may be more useful for debugging purposes
    def __repr__(self) -> str:
        return f"<Person(name={self.name}, age={self.age})>"

def main() -> None:
    mario: Person = Person("Mario", 27)
    print(mario) # This will print the memory location of the object without the __str__ or __repr__ dunder methods
    print(repr(mario)) # This will print the memory location of the object with the __repr__ dunder method


if __name__ == '__main__':
    main()
