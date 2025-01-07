text: str = "Hello World!"

for i in range(3):
    print(f"{i}: {text}")

people: list[str] = ["Noel", "Johnny", "Jane", "Doe"]

for person in people:
    if len(person) > 4:
        print(f'{person} has a long name!')
    else:
        print(f'{person} has a short name!')
