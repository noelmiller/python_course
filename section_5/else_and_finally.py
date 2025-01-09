user_input: str = "10"

try:
    result: float = 1 / float(user_input)
    print(f'1 / {user_input} = {result}')
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else: # This block will only run if no exceptions were raised, this is not recommended to use
    print("No exceptions were raised")
finally: # This block will always run no matter what
    print("This block will always run")
