number: int = 5

while number > 0:
    number -= 1

    if number == 2:
        print("breaking at 2")
        break

    print(number)

print("Done")

number: int = 5

while number > 0:
    number -= 1

    if number == 2:
        print("skipping 2")
        continue

    print(number)

print("Done")

# practicalish example
total: int = 0

print("Welcome to Calc+! Add positive numbers, or insert '0' to exit.")
while True:
    try:
        user_input: int = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if user_input < 0:
        print("Please enter a positive number.")
        continue

    if user_input == 0:
        print(f"Total: {total}")
        break

    total += user_input
