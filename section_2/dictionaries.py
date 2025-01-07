users: dict[int, str] = {1: 'Bob', 2: 'Luigi'}
print(users[2])

# add a new key-value pair
users[3] = 'Mario'
print(users)

# change a value
users[1] = 'James'
print(users)

# remove a key-value pair
users.pop(2)
# or
del users[3]
print(users)

weather: dict = {'time': '12:00',
                 'weather': {'morning': 'rain',
                             'evening': 'more rain'}
                }
print(weather)
print(weather['time'])
print(weather['weather'])
print(weather['weather']['morning'])
