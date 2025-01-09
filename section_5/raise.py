def check_age(age: int) -> bool:
    if age < 0:
        raise ValueError('Age cannot be negative') # This will raise a ValueError
    elif age >= 21:
        print('You are allowed to drink')
        return True
    else:
        print('You are not allowed to drink')
        return False

check_age(30)

raise Exception('This is an exception') # This will raise a general exception

# https://docs.python.org/3/library/exceptions.html
