# pass is used as a placeholder for future code
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# The pass statement is a null operation; nothing happens when it executes.
# You can also use ... to represent an empty block of code which is equivalent to pass
# I have a couple of examples below to show you how pass can be used

def get_status():
    pass

def connect_to_internet():
    pass

number: int = 2

if number > 0:
    pass
else:
    pass

for i in range(3):
    pass

def connect():
    ...
