import time


def connect() -> None:
    print("Connecting to internet...")
    time.sleep(1)
    print("Connected!")

# This is useful for testing the function independently of the larger program
if __name__ == "__main__":
    connect()
