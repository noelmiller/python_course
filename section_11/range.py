def main() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5] # easy for small lists

    my_range: range = range(1,6) # more efficient for large lists
    my_range2: range = range(5) # same as range(0, 5)
    print(my_range) # range(1, 6) - range object
    print(list(my_range)) # [1, 2, 3, 4, 5] - list of numbers

    myrange3: range = range(0, 10, 2) # range from 1 to 10 with a step of 2
    print(list(myrange3)) # [0, 2, 4, 6, 8]

    my_range4: range = range(0, -5, -1) # range from 0 to -5 with a step of -1
    print(list(my_range4)) # [0, -1, -2, -3, -4]

    for i in range(3):
        print(i)

if __name__ == '__main__':
    main()
