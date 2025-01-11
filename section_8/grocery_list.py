import sys


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def welcome_message() -> None:
    print("Welcome to the grocery list app!")
    print("Enter:")
    print("-" * 10)
    print("1 to add an item")
    print("2 to remove an item")
    print("3 to view the list")
    print("4 to modify an item")
    print("0 to exit")
    print("-" * 10)

def is_an_option(text: str) -> bool:
    return text in ['1', '2', '3', '4', '0']

def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f"{color.BOLD}{color.PURPLE}{item.capitalize()}{color.END} has been added to the list")

def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'{item} removed from the list')
    except ValueError:
        print(f'{item} not found in the {groceries} list')

def modify_item(groceries: list[str]) -> None:
    try:
        item: str = input('Enter the item to modify: ').lower()
        if item == "":
            print('Item cannot be empty')
            return
        index: int = groceries.index(item)
        new_item: str = input('Enter the new item: ')
        groceries[index] = new_item
        print(f'{item} has been modified to {new_item}')
    except ValueError:
        print(f'{item} not found in the list')

def display_items(groceries: list[str]) -> None:
    print('Grocery List:')
    print('-' * 10)
    for i, item in enumerate(groceries, 1):
        print(f'{i}. {item.capitalize()}')
    print('-' * 10)


def main() -> int:
    groceries: list[str] = []
    welcome_message()
    try:
        while True:
          option: str = input('Enter an option: ')
          if not is_an_option(option):
              print('Invalid option. Please try again')
              continue
          if option == '0':
              print('Exiting the grocery list app')
              return 0
          elif option == '1':
              while True:
                  item: str = input('Enter the item to add: ').lower()
                  if item == "":
                        print('Item cannot be empty')
                        continue
                  add_item(item, groceries)
                  break
          elif option == '2':
              item: str = input('Enter the item to remove: ')
              remove_item(item, groceries)
          elif option == '3':
              display_items(groceries)
          elif option == '4':
              modify_item(groceries)
    except KeyboardInterrupt:
        print('\nExiting the grocery list app')
        return 0

if __name__ == '__main__':
    sys.exit(main())
