# This will run forever and will cause a RecursionError
# def func() -> None:
#     print('Hello')
#     func()
#
# func()

import time

def connect_to_internet(signal: bool, delay: int = 0) -> None:
    if delay > 5:
        signal = True

    if signal:
        print("Connected to the internet!")
    else:
        print(f"Connecting to the internet... trying again in {delay}s")
        time.sleep(delay)
        connect_to_internet(signal, delay + 1)

connect_to_internet(signal=False, delay=2)
