def get_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
            break
        except ValueError:
            print("Please enter a valid float")

print("Welcome to your simple adder!")
print("-----------------------------")

a: float = get_input("Enter the first number: ")
b: float = get_input("Enter the second number: ")

print("-----------------------------")

result: int = int(a) + int(b)

print(f"The result is: {result}")
