def main() -> None:
    # This is a traditional way to iterate over a list
    elements: list[str] = ['A', 'B', 'C', 'D', 'E']
    i: int = 0
    for element in elements:
        print(i, element)
        i += 1

    # This is a more pythonic way to iterate over a list
    # enumerate returns a list of tuple with the index and the element
    # so it is possible to unpack the tuple in the for loop
    elements: list[str] = ['A', 'B', 'C', 'D', 'E']
    enumeration: enumerate = enumerate(elements)
    enumeration2: enumerate = enumerate(elements, 1)
    # print(enumeration) # <enumerate object at 0x7f5d7c7d4c00>
    print(list(enumeration)) # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
    print(list(enumeration2)) # [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]

    # This is the pythonic way to iterate over a list
    for i, element in enumerate(elements):
        print(i, element)

    # you can also provide a start index
    for i, element in enumerate(elements, 1):
        print(i, element)

if __name__ == '__main__':
    main()
