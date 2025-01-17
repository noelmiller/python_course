def main() -> None:
    print("Hello Bob!")

    # print takes multiple arguments
    print(1, 2, True, ['a', 'b'])

    # print takes keyword arguments sep and end
    # sep is the separator between arguments
    # end is the character to print at the end of the line (default is '\n')
    print('A', 'B', 'C', sep='-', end=' ')
    print("Hello Bob!")

    # unpacking arguments
    people: list[str] = ['Alice', 'Bob', 'Charlie']
    # just prints the list
    print(people)

    # unpacks the list
    # *people is the same as people[0], people[1], people[2]
    # so it prints Alice Bob Charlie
    print(*people, sep=", ", end=".")


if __name__ == "__main__":
    main()
