while True:
    user_input: str = input("Enter a number: ")

    try:
        number: float = float(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print("Program encountered an unknown error")
        print(f"Error type: {type(e)}")
        print(f"Error: {e}")
