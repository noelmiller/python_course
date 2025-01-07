no_value: None = None
print(no_value)
print(type(no_value))

users: dict[int, str] = {1: 'Bob', 2: 'Luigi'}
# helper method that will return None if the key is not found
print(users.get(3))

# optionals using the Union type
possible_user: str | None = users.get(3) # gets a None value
# possible_user: str | None = users.get(2) gets a string value

print(possible_user)
