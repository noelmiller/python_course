# classes share information with each other using self
# objects are instances of classes and do not share information with each other
class Fruit:
    def __init__(self, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def eat(self) -> None:
        print(f'You ate the {self.grams}g of {self.name}')

def main() -> None:
   apple = Fruit('apple', 25) # apple is self
   print(apple.name)
   apple.eat()

   banana = Fruit('banana', 10) # banana is self
   print(banana.name)
   banana.eat()

if __name__ == '__main__':
    main()
