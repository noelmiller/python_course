from abc import ABC, abstractmethod


# Abstract methods are methods that are declared in the abstract class but are not implemented
# Abstract methods must be implemented in the child class
# Abstract methods are used to enforce the implementation of a method in the child class
class Appliance(ABC):
    def __init__(self, brand: str, version_number: int) -> None:
        self.brand = brand
        self.version_number = version_number
        self.is_turned_on: bool = False

    @abstractmethod
    def turn_on(self) -> None:
        ...

    @abstractmethod
    def turn_off(self) -> None:
        ...

class Lamp(Appliance):
    def __init__(self, brand: str, version_number: int, color: str) -> None:
        super().__init__(brand, version_number)
        self.color = color

    def turn_on(self) -> None:
        if self.is_turned_on:
            print(f"{self.brand} lamp is already turned on")
            return

        self.is_turned_on = True
        print(f"{self.brand} lamp is turned on")

    def turn_off(self) -> None:
        if not self.is_turned_on:
            print(f"{self.brand} lamp is already turned off")
            return

        if self.is_turned_on:
            self.is_turned_on = False
            print(f"{self.brand} lamp is turned off")

# Best practice to use NotImplementedError when implementing abstract methods that are not implemented
class Oven(Appliance):
    def __init__(self, brand: str, version_number: int) -> None:
        super().__init__(brand, version_number)

    def turn_on(self) -> None:
        raise NotImplementedError("Oven turn_on method is not implemented")

    def turn_off(self) -> None:
        raise NotImplementedError("Oven turn_off method is not implemented")

def main() -> None:
    lamp: Lamp = Lamp("Philips", 1, "white")
    lamp.turn_on()
    lamp.turn_on()
    lamp.turn_off()
    lamp.turn_off()
    lamp.turn_on()
    lamp.turn_off()

    oven: Oven = Oven("Samsung", 2)
    oven.turn_on()
    oven.turn_off()


if __name__ == '__main__':
    main()
