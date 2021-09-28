""" EXAMPLE FOR STRATEGY IN PYTHON """
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union


class Fighter(ABC):
    """ ABSTRACT FIGHTER """
    @abstractmethod
    def set_strategy(self, strategy):
        """ CHANGE FIGHT STRATEGY """
        pass

    @abstractmethod
    def do_strike(self):
        """ DO SOME KIND OF STRIKE """
        pass


class MMAFighter(Fighter):
    """ CONCRETE FIGHTER CLASS """
    def __init__(self, name: str):
        self.name = name
        self.strategy: Union[BasicStrategy, MuayThaiStrategy,
                             BoxStrategy, WrestlingStrategy] = BasicStrategy()

    def set_strategy(self, strategy: Union[BasicStrategy, MuayThaiStrategy,
                                           BoxStrategy, WrestlingStrategy]) -> None:
        print(f'{self.name} decides to change his strategy...')
        self.strategy = strategy

    def do_strike(self) -> None:
        self.strategy.strike()


class Strategy(ABC):  # pylint: disable=too-few-public-methods
    """ ABSTARCT STRATEGY """
    @abstractmethod
    def strike(self):
        """ JUST STRIKE! """
        pass


class BasicStrategy(Strategy):  # pylint: disable=too-few-public-methods
    """ BASIC LOGIC CLASS """
    def strike(self) -> None:
        print('Some average punch...')


class MuayThaiStrategy(Strategy):  # pylint: disable=too-few-public-methods
    """ MUAY THAI LOGIC CLASS """
    def strike(self) -> None:
        print('Powerful high-kick to the opponent head!')


class BoxStrategy(Strategy):  # pylint: disable=too-few-public-methods
    """ BOX LOGIC CLASS """
    def strike(self) -> None:
        print('Punch to the head and fast uppercut!')


class WrestlingStrategy(Strategy):  # pylint: disable=too-few-public-methods
    """ WRESTLING LOGIC CLASS """
    def strike(self) -> None:
        print('Catch and throw him!')


if __name__ == '__main__':
    muay_thai_strategy = MuayThaiStrategy()
    box_strategy = BoxStrategy()
    wrestling = WrestlingStrategy()

    best_fighter = MMAFighter('Cigano')
    best_fighter.do_strike()
    best_fighter.set_strategy(muay_thai_strategy)
    best_fighter.do_strike()
    best_fighter.set_strategy(box_strategy)
    best_fighter.do_strike()
    best_fighter.set_strategy(wrestling)
    best_fighter.do_strike()
