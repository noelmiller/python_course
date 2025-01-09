from my_time import *
# whatever is imported last will override the previous import
# This will override the time() function from my_time.py
from time import *


print(time())
print(date())
