# The same as globals() but for local variables
print(locals())

def add(a: int, b: int) -> None:
    result: int = a + b
    print(f'{a} + {b} = {result}')

    print(f'add() has: {locals()}') # prints the local variables
    print(f'add() can see the {globals()}')

def main() -> None:
    add(1, 2)

if __name__ == '__main__':
    main()
