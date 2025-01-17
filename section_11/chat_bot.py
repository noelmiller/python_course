from difflib import get_close_matches


def get_best_match(user_question: str, knowledge: dict) -> str | None:
    questions: list[str] = [q for q in knowledge]
    matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def run_chatbot(knowledge: dict) -> None:
    while True:
        user_input: str = input("You: ")

        best_match: str | None = get_best_match(user_input, knowledge)
        response: str | None = knowledge.get(best_match)

        if response:
            print(f"Bot: {response}")
        else:
            print("Bot: I don't know what you're talking about!")

def main() -> None:
   brain: dict[str, str] = {'hello': 'Hello there!',
                            'how are you?': 'I am a bot, I do not have feelings.',
                            'what is your name?': 'I am a chatbot, I do not have a name.',
                            'goodbye': 'Goodbye!',
                            'what is the weather like today?': 'I am a chatbot, I do not know the weather.',
                            'what is the capital of France?': 'Paris'}
   run_chatbot(brain)

if __name__ == '__main__':
    main()
