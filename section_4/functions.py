from datetime import datetime
import time

def greet():
    print("Hello, World!")
    print('----')

greet()


def show_time():
    now: datetime = datetime.now()
    print(f"Time: {now:%H:%M:%S}")

show_time()

time.sleep(2)

show_time()
