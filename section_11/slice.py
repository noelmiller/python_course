def main() -> None:
    text: str = "Hello, World!"

    first_three: slice = slice(0,3)

    print(text[first_three]) # Hel

    reverse_slice: slice = slice(None, None, -1)

    print(text[reverse_slice]) # !dlroW ,olleH

    step_two: slice = slice(None, None, 2)
    print(text[step_two]) # Hlo ol!


if __name__ == '__main__':
    main()
