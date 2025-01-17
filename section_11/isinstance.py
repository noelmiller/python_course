def main() -> None:
    # isinstance checks if the object is an instance of the class
    # isinstance(object, class)
    number: int = 10
    pi: float = 3.14
    text: str = "banana"
    my_list: list[int] = [1, 2, 3]

    print(isinstance(number, int)) # True
    print(isinstance(number, str)) # False
    print(isinstance(number, float)) # False

    print(isinstance(pi, int))
    print(isinstance(pi, str))
    print(isinstance(pi, float))

    print(isinstance(text, str))

    print(isinstance(pi, int | float))

    class Animal:
        ...
    class Cat(Animal):
        ...

    print(isinstance(Cat(), Animal)) # True
    print(isinstance(Animal(), Cat)) # False

    if isinstance(pi, float):
        print("Pi is a float")


if __name__ == '__main__':
    main()
