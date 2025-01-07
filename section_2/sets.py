# all elements in a set must be unique
elements: set = {99, True, "Bob"}
print(f"Original {elements}")

# Add elements (sets are random, the order of the elements is not guaranteed)
elements.add("James")
print(f"Added: {elements}")

# Remove elements (sets are random, so any element can be removed)
elements.remove("Bob")
print(f"Removed: {elements}")

# Pop elements (sets are random, so any element can be popped)
elements.pop()
print(f"Popped: {elements}")

# Clear elements
elements.clear()
print(f"Cleared: {elements}")

# create empty set
empty: set = set()
print(empty)
