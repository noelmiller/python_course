import time
# while True:
#     print("This will run forever!")

i: int = 5

while i > 0:
    print(f"Hello: {i}")
    i -= 1

connected: bool = True

while connected:
    print("Using the internet!")
    time.sleep(5)
    connected = False
print("Connection ended!")

while True:
    user_input: str = input("You: ")

    if user_input == "hello":
        print("Bot: Hi!")

    else:
        print("Bot: I don't understand that!")
