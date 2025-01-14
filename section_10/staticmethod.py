class Calculator:
    def __init__(self, version: int) -> None:
        self.version = version

    # @staticmethod is a type hint that tells the developer that this method is a static method
    # Static methods are methods that do not require an instance of the class to be called
    # Static methods are called using the class name
    @staticmethod
    def add(*numbers: float) -> float:
        return sum(numbers)

    def get_version(self) -> int:
        return self.version

def main() -> None:
    calc: Calculator = Calculator(version=1)
    result: float = calc.add(1, 2, 3, 4, 5)

    print(f"Result: {result}")

    # Static methods can be called using the class name
    result2: float = Calculator.add(1, 2, 3, 4, 5)

    print(f"Result2: {result2}")


if __name__ == '__main__':
    main()
