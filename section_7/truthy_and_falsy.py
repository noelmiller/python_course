print(bool('')) # False
print(bool([])) # False
print(bool({})) # False
print(bool(())) # False
print(bool(False)) # False
print(bool(None)) # False
print(bool(0)) # False
print(bool(0.0)) # False

users: dict[int, str] = {1: 'noel', 2: 'jane', 3: 'john'}
users2 = {}

if users: # True
    for k, v in users.items():
        print(k, v, sep=': ')
else:
    print('No users found')

if users2: # False
    for k, v in users.items():
        print(k, v, sep=': ')
else:
    print('No users found')
