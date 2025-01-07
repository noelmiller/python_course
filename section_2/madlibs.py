name: str = input("Enter a name: ")
noun_a: str = input("Enter a noun: ")
verb_a: str = input("Enter a verb: ")
noun_b: str = input("Enter another noun: ")
verb_b: str = input("Enter another verb (past tense): ")
number_a: str = input("Enter a number: ")
number_b: str = input("Enter another number: ")

story: str = f"""
--------------------------------
This is a story about {name} and their {noun_a} that wanted to {verb_a}.
They went to the {noun_b} and {verb_b} it.
In the end, they found {number_a} {noun_a} and {number_b} {noun_b}.
--------------------------------
"""

print(story)
