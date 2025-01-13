import sys
from datetime import datetime
from random import choice


class ChatBot:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_description(self) -> str:
        return f'Hello, my name is {self.name} and I am {self.age} years old.'

    def get_response(self, message: str) -> str:
        lower_message = message.lower()

        if "hello" in lower_message:
            return f"{self.name}: Hello!"
        elif "bye" in lower_message:
            return f"{self.name}: Goodbye!"
        elif "how old are you" in lower_message:
            return f"{self.name}: I am {self.age} years old."
        elif "what time is it" in lower_message:
            return f"{self.name}: The current time is {datetime.now().strftime('%H:%M')}."
        elif "how are you?" in lower_message:
            return f"{self.name}: I am fine, thank you!"
        else:
            random_responses: list[str] = [
                "I am sorry, I do not understand.",
                "Could you please repeat that?",
                "I am not sure what you mean."
            ]
            return f"{self.name}: {choice(random_responses)}"

    def run(self) -> None:
        print(self.get_description())
        try:
            while True:
                message = input("You: ")
                if message == "exit":
                    print(f"{self.name}: Goodbye!")
                    break
                    response = self.get_response(message)
                    print(response)
        except KeyboardInterrupt:
            print(f"\n{self.name}: Goodbye!")

def main() -> int:
    mario: ChatBot = ChatBot("Mario", 27)
    mario.run()
    return 0

if __name__ == '__main__':
    sys.exit(main())
