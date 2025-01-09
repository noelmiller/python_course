import sys

# Example try except block
try:
    result: float = 10 / 0
    print(result)
except Exception as e:
    print(f"Error: {e}")

while True:
    try:
        user_input: str = input("Enter a number: ")
        print(f'10 / {user_input} = {10 / float(user_input)}')
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl + C")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
