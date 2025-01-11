number: int = 999 # Global scope

# Global scope
# Variables defined outside a function are accessible inside the function using the global keyword
def change_number() -> None:
    global number # This will change the global variable
    number = 1000
    print(f'Inside function: {number}') # 1000

print(number)
change_number()
print(number)

# Local scope
# Variables defined inside a function are not accessible outside the function
# Variables defined outside a function are accessible inside the function
# Variables defined inside a function are not accessible in other functions
def scope_test() -> None:
    number: int = 100
    print(f'Inside outer function: {number}') # 100
    # Cannot access inner_number from outside inner_scope
    # print(f'Inside outer function: {inner_number}')
    def inner_scope() -> None:
        print(f'Inside inner function: {number}')
        inner_number: int = 10
        print(f'Inside inner function: {inner_number}')
    inner_scope()

scope_test()

# nonlocal keyword
# nonlocal is used to change the value of a variable in the outer scope
def nonlocal_test() -> None:
    number: int = 100
    string: str = 'Hello'
    print(f'Inside outer function: {number}') # 100
    print(f'Inside outer function: {string}') # Hello
    def inner_scope() -> None:
        nonlocal number, string
        string = 'World'
        number = 200
        print(f'Inside inner function: {number}') # 200
        print(f'Inside inner function: {string}') # World
    inner_scope()
    print(f'Inside outer function: {number}') # 200
    print(f'Inside outer function: {string}') # World
