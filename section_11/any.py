def main() -> None:
    # any checks if any of the elements in the iterable are truthy
    people_voted: list[int] = [0, 1, 0, 0, 0]
    if any(people_voted):
        print("The motion passed!")
    else:
        print("The motion failed!")


if __name__ == '__main__':
    main()
