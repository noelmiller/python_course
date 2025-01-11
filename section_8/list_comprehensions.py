# This is a lot of code without a list comprehension
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled_numbers: list[int] = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers) # result is: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# This is the same code with a list comprehension
doubled_lc: list[int] = [number * 2 for number in numbers] # result is: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(doubled_lc)

# This is a lot of code without a list comprehension
names: list[str] = ['Noel', 'Jen', 'Zoe', 'Alex', 'Jen', 'Zoe', 'Alex', 'Jen', 'Zoe', 'Alex']
j_names: list[str] = []
for name in names:
    if name.startswith('J'):
        j_names.append(name)

print(j_names) # result is: ['Jen', 'Jen', 'Jen']

# This is the same code with a list comprehension
j_names_lc: list[str] = [name
                         for name in names
                         if name.startswith('J')] # result is: ['Jen', 'Jen', 'Jen']
print(j_names_lc)

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # result is: [2, 4, 6, 8, 10]

even_numbers: list[int] = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

even_numbers_lc: list[int] = [number for number in numbers if number % 2 == 0] # result is: [2, 4, 6, 8, 10]
print(even_numbers_lc)
