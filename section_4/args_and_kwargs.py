# print uses *args in its implementation
# this allows for a variable number of arguments to be passed to the function
# the *args parameter is a tuple
# anything passed after the *args parameter must be a keyword argument
print(1, 2, 3, 'hello', 'world', sep=' | ')

# you don't have to use the name 'args'
def add(*numbers: int) -> int:
    print(numbers)
    return sum(numbers)

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# you can have a positional argument before the *args parameter
# But this is not best practice
def greet(greeting: str, *people: str, ending: str) -> None:
    for person in people:
        print(f"{greeting}, {person} {ending}")

greet("Hello", "Mario", "John", "Jane", ending="!")

# This is a better way to write the function above
def greet2(*people: str, greeting: str, ending: str) -> None:
    for person in people:
        print(f"{greeting}, {person} {ending}")

greet2("Mario", "John", "Jane", greeting="Hello", ending="!")

# The **kwargs parameter is a dictionary
# The keys are the parameter names
# The values are the parameter values
# The **kwargs parameter must come after the *args parameter
def pin_position(**kwargs: int) -> None:
    print(kwargs)

pin_position(x=1, y=2, z=3)

# you can use whatever name you want for the **kwargs parameter
def func(*strings: str, default: int, **numbers:int) -> None:
    print(strings)
    print(numbers)

func("hello", "world", default=20, x=1, y=2, z=3)
