""" EXAMPLE FOR BUILDER IN PYTHON """
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union


class Director:
    """ IT'S DIRECTOR """
    def __init__(self):
        self._builder = None

    def set_builder(self, builder_instance: TownHouseBuilder) -> None:
        """ SET BUILDER """
        self._builder = builder_instance

    def get_simple_house(self) -> TownHouse:
        """ BUILD SMALL HOUSE """
        self._builder.set_windows(1)
        self._builder.set_walls('wood')
        self._builder.set_garden(6)
        return self._builder.get_house()

    def get_big_house(self) -> TownHouse:
        """ BUILD BIG HOUSE """
        self._builder.set_windows(3)
        self._builder.set_walls('bricks')
        self._builder.set_garden(10)
        return self._builder.get_house()


class TownHouse:
    """ IT'S SOME TOWNHOUSE"""
    def __init__(self):
        self.parts = []

    def add(self, part) -> None:
        """ ADD PART FOR PRODUCT """
        self.parts.append(part)

    def show_parts(self) -> None:
        """ PRINT PARTS """
        for part in self.parts:
            print(f'\t{part}')


class Windows:  # pylint: disable=too-few-public-methods
    """ CLASS FOR WINDOWS """
    def __init__(self, count: int):
        self.count = count

    def __str__(self):
        return f'windows count = {self.count}'


class Walls:  # pylint: disable=too-few-public-methods
    """ CLASS FOR WALLS """
    def __init__(self, material: str):
        self.material = material

    def __str__(self):
        return f'walls material is {self.material}'


class Garden:  # pylint: disable=too-few-public-methods
    """ CLASS FOR GARDEN """
    def __init__(self, square: Union[float, int]):
        self.square = square

    def __str__(self):
        return f'garden square is {self.square}'


class Builder(ABC):
    """ ABSTRACT BUILDER """
    @abstractmethod
    def set_windows(self, count):
        """ ABSTRACT METHOD FOR WINDOWS """
        pass

    @abstractmethod
    def set_walls(self, material):
        """ ABSTRACT METHOD FOR WALLS """
        pass

    @abstractmethod
    def set_garden(self, square):
        """ ABSTRACT METHOD FOR GARDEN """
        pass


class TownHouseBuilder(Builder):
    """ CONCRETE BUILDER FOR TOWNHOUSE """
    def __init__(self):
        self._product = TownHouse()

    def get_house(self) -> TownHouse:
        """ RETURN FINAL PRODUCT """
        product = self._product
        self._product = TownHouse()
        return product

    def set_windows(self, count: int) -> None:
        self._product.add(Windows(count))

    def set_walls(self, material: str) -> None:
        self._product.add(Walls(material))

    def set_garden(self, square: Union[float, int]) -> None:
        self._product.add(Garden(square))


if __name__ == '__main__':
    director = Director()

    builder = TownHouseBuilder()
    director.set_builder(builder)

    small_house = director.get_simple_house()
    big_house = director.get_big_house()

    print('Small house parts:')
    small_house.show_parts()

    print('\nBig house parts:')
    big_house.show_parts()
