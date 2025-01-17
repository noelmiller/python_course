from typing import Any
# from math import * # don't pollute the namespace

text: str = 'Bob'
my_list: list[str] = [1, 2, 3]

def func() -> None:
    ...

def main() -> None:
    # creating a dictionary with all the global variables
    my_globals: dict[str, Any] = globals()
    #print(my_globals)

    for k, v in my_globals.items():
        print(k, v)

if __name__ == '__main__':
    main()
