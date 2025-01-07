# a parameter is a variable in a method definition
# an argument is the actual value of the variable that gets passed to the function
def greet(name: str, language: str, default: str = "Hello"):
    if language == 'it':
        print(f'Ciao, {name}!')
    else:
        print(f'{default}, {name}!')

# this is an example of keyword arguments
# the order of the arguments does not matter
# you can mix positional and keyword arguments
# positional arguments must come before keyword arguments
greet(name="Mario", language="it")

greet("John", "en")
