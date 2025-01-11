people: list[str] = ['Anna', 'Bob', 'Chris', 'David', 'Fred']

# Looping and modifying is a bad idea
# for person in people:
#     print(f'- {person}, {people.index(person)}')
#     if person == 'Bob':
#         print(f'Removing {person}')
#         people.remove(person) # we lost Chris

# Best practice is to create a new list and append to it
new_people: list[str] = []
for person in people:
    print(f'- {person}, {people.index(person)}')
    if person == 'Bob':
        print(f'Removing {person}')
        continue
    new_people.append(person)

print(new_people)
