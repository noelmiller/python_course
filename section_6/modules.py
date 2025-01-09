# import the greetings module without using an alias
# import greetings


# To import just the greet module from greetings.py
# You do not save on memory by importing just the greet module
# You can just be more specific about what you are importing

# from greetings import greet
# greet("Mario")

# import using import * to import all modules
# This can be quite dangerous as you can overwrite existing modules
# from greetings import *
# greet("Mario")
# print(f"Author: {AUTHOR}")

# use an alias to import the module
import greetings as g

g.greet("Mario")
print(f"Author: {g.AUTHOR}")
