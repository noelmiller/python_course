def main() -> None:

    # Don't use more than 3 checks
    wifi_enabled: bool = True
    has_electricity: bool = True
    has_subscription: bool = True

    if wifi_enabled and has_electricity and has_subscription:
        print("You can watch Netflix!")

    requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]

    # Check if all the requirements are met
    # If all the requirements are met, print the message
    # It takes all truthy and falsy values
    if all(requirements):
        print("You can watch Netflix!")

    people_voted: list[int] = [1, 1, 1, 0, 1 , 0, 1, 1, 1, 0]
    if all(people_voted):
        print("The motion passed!")
    else:
        print("The motion failed!")

if __name__ == '__main__':
    main()
