from typing import override


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def describe(self) -> None:
        print(f"{self.name} has {self.sides} sides")

    def shape_method(self) -> None:
        print(f"{self.name}: shape_method()")

class Square(Shape):
    def __init__(self, size: float) -> None:
        # as long as you pass the required arguments, you can call the super class method
        super().__init__("square", 4)
        self.size = size

    # @override is a type hint that tells the developer that this method is overriding a method from the super class (Shape)
    # You can override methods from the super class by using the same method name
    @override
    def describe(self) -> None:
        print(f"I am a {self.name} and each side is {self.size} units long")

class Rectangle(Shape):
    def __init__(self, length: float, height: float) -> None:
        super().__init__("rectangle", 4)
        self.length = length
        self.height = height

    @override
    def describe(self) -> None:
        print(f"{self.name} ({self.length} x {self.height})")

def main() -> None:
    square: Square = Square(20)
    square.describe()
    square.shape_method()

    rectangle: Rectangle = Rectangle(20, 30)
    rectangle.describe()
    rectangle.shape_method()

if __name__ == '__main__':
    main()
