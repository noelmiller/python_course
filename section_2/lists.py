people: list[str] = ["Bob", "James", "Tom"]
print(f"Original: {people}")

# Append
people.append("Jeremy")
print(f"Appended: {people}")

# Remove
people.remove("Bob")
print(f"Removed: {people}")

# Pop
people.pop()
print(f"Popped: {people}")

people[0] = "Charlotte"
print(f"Changed: {people}")

people.insert(1, "Timothy")
print(f"Inserted: {people}")

# Clear
people.clear()
print(f"Cleared: {people}")
