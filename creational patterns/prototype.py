""" EXAMPLE FOR PROTOTYPE IN PYTHON """
from abc import ABC, abstractmethod
from copy import deepcopy
import random


class Cloneable(ABC):  # pylint: disable=too-few-public-methods
    """ ABSTARCT CLONEABLE CLASS """
    @abstractmethod
    def clone(self, new_name):
        """ ABSTARCT METHOD FOR CLONING """
        pass


class Info:  # pylint: disable=too-few-public-methods
    """ CREATE INFO """
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'name is {self.name}'


class DNA:  # pylint: disable=too-few-public-methods
    """ UNIQ DNA IF IT WAS CREATED """
    def __init__(self):
        self.dna = random.random()

    def __str__(self):
        return f'dna_id is {id(self.dna)}'


class SimpleSheep(Cloneable):
    """ CLASS FOR CLONEABLE SHEEP """
    def __init__(self, info: Info, dna: DNA):
        self.info = info
        self.dna = dna

    def clone(self, new_name: str):
        return SimpleSheep(Info(new_name), deepcopy(self.dna))

    def print_info(self) -> None:
        """ JUST PRINT INFO """
        print(f'{self.info}\n{self.dna}')
        print('-' * 10)


if __name__ == '__main__':
    first_sheep = SimpleSheep(Info('EVA'), DNA())
    first_sheep.print_info()

    clone = first_sheep.clone('EVA2')
    clone.print_info()

    another_sheep = SimpleSheep(Info('EVA2'), DNA())
    another_sheep.print_info()
