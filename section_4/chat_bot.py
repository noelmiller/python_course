from datetime import datetime
import sys

def get_response(text: str) -> str:
    lowered: str = text.lower()

    if lowered in ["hello", "hi", "hey"]:
        return "Hey there!"
    elif 'how are you' in lowered:
        return "I'm good, thanks for asking!"
    elif 'your name' in lowered:
        return "I'm Chatbot!"
    elif 'time' in lowered:
        return f"The time is {datetime.now().strftime('%H:%M')}"
    elif lowered in ["see you", "bye", "goodbye"]:
        print("Goodbye!")
        sys.exit()
    else:
        return f"I'm sorry, I don't understand: {text}"

def welcome_message(name: str) -> None:
    print("Welcome to Chatbot!")
    print (f"Hello, {name}!")
    print("Enter 'exit' to quit the chat.")

def get_name() -> str:
    name: str = input("Enter your name: ")
    return name

def main() -> int:
    try:
        name: str = get_name()
        welcome_message(name)
        while True:
            user_input: str = input(f"{name}: ")

            if user_input == "exit":
                print("Goodbye!")
                sys.exit()

            bot_response: str = get_response(user_input)
            print(f"Bot: {bot_response}")
    except KeyboardInterrupt:
        print("\n")
        print("Goodbye!")
        sys.exit(0)
    return 0

if __name__ == "__main__":
    main()
