from typing import Final


AUTHOR: Final[str] = "Noel"
VERSION: Final[int] = 1


def greet(name: str) -> None:
    print(f"Hello, {name}!")
