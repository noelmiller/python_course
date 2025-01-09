import string
import sys


def is_letters_only(text: str) -> None:
    alphabet: str = string.ascii_letters + ' '
    for char in text:
        if char not in alphabet:
            raise ValueError("The text must only contain letters and spaces")
    print("The text is valid")

def main() -> None:
    while True:
        try:
            user_input: str = input("Check Text: ")
            is_letters_only(user_input)
        except ValueError as e:
            print("Please only enter letters and spaces")
        except KeyboardInterrupt:
            print("\nYou pressed Ctrl + C")
            print("Exiting program")
            sys.exit()
        except Exception as e:
            print("Program encountered an unknown error")
            print(f"Error type: {type(e)}")
            print(f"Error: {e}")

main()
