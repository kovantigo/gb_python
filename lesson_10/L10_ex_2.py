from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, fabric):
        self.fabric = fabric

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Coat(0)

    def __str__(self):
        return f'{Clothes.result}'


class Coat(Clothes):
    @property
    def consumption(self):
        return self.fabric / 6.5 + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return 2 * self.fabric + 0.3


ct = Coat(200)
ce = Costume(100)
print(ce + ct + ce)
