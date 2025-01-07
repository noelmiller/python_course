# return type is specified by the arrow ->
def get_length(text: str) -> int:
    return len(text)

name: str = "Mario"
print(get_length(name))

print(get_length("Mario"))

def make_upper(text: str) -> str:
    return text.upper()

print(make_upper(name))

def connect_to_internet() -> None:
    print("Connecting to the internet...")
    # implicitly has a return None
