numbers: list[int] = [1, 2, 3, 4, 5, 6]
print(numbers[0:3]) # result is: [1, 2, 3]
print(numbers[3:6]) # result is: [4, 5, 6]
print(numbers[2:4]) # result is: [3, 4]
print(numbers[:3]) # result is: [1, 2, 3]
print(numbers[3:]) # result is: [4, 5, 6]
print(numbers[:3] + numbers[3:]) # result is: [1, 2, 3, 4, 5, 6]
print(numbers[-1]) # result is: 6 (last element)
print(numabers[-2]) # result is: 5 (second to last element)

print(numbers[0:4:2]) # result is: [1, 3]
print(numbers[4:0:-2]) # result is: [5, 3]
print(numbers[::2]) # result is: [1, 3, 5]
print(numbers[::-1]) # result is: [6, 5, 4, 3, 2, 1]

# Slicing can also be done on tuples and strings

string_string: str = 'Noel'
print(string_string[0:3]) # result is: Noe

tuple_thing: tuple[str, str, str, str] = ('N', 'o', 'e', 'l')
print(tuple_thing[0:3]) # result is: ('N', 'o', 'e')
