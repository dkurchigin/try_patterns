""" EXAMPLE FOR OBSERVER IN PYTHON """
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Union, Dict


class Subject(ABC):
    """ ABSTRACT SUBJECT """
    @abstractmethod
    def attach(self, client):
        """ ATTACH ONE OBSERVER """
        pass

    @abstractmethod
    def detach(self, client):
        """ DETACH ONE OBSERVER """
        pass

    @abstractmethod
    def notify(self):
        """ NOTIFY OUR OBSERVERS """
        pass


class BankRate(Subject):
    """ OUR BANK CLASS """
    currency: Dict[str, Union[int, float]] = {
        'dollar': 100,
        'euro': 80
    }
    _clients: List[Union[ConcreteClientFirst, ConcreteClientSecond]] = []

    def attach(self, client: Union[ConcreteClientFirst, ConcreteClientSecond]) -> None:
        self._clients.append(client)

    def detach(self, client: Union[ConcreteClientFirst, ConcreteClientSecond]) -> None:
        self._clients.remove(client)

    def notify(self) -> None:
        for client in self._clients:
            client.update(self)

    def change_currency(self, dollar_currency: Union[int, float],
                        euro_currency: Union[int, float]) -> None:
        """ OBSERVER CLASS """
        self.currency['dollar'] = dollar_currency
        self.currency['euro'] = euro_currency
        self.notify()


class Observer(ABC):  # pylint: disable=too-few-public-methods
    """ OBSERVER CLASS """
    @abstractmethod
    def update(self, some_informer):
        """ DO SOMETHING WHEN IT UPDATE """
        pass


class ConcreteClientFirst(Observer):  # pylint: disable=too-few-public-methods
    """ SOME FIRST TYPE OF CLIENT """
    def update(self, some_informer: BankRate) -> None:
        if some_informer.currency['dollar'] < 50:
            print('FirstClient: think that a dollar costs so cheap...')
        if some_informer.currency['euro'] > 100:
            print('FirstClient: think that he/she need sell his/her euros!')


class ConcreteClientSecond(Observer):  # pylint: disable=too-few-public-methods
    """ SOME SECOND TYPE OF CLIENT """
    def update(self, some_informer: BankRate) -> None:
        if some_informer.currency['dollar'] > 80:
            print('SecondClient: think that he/she need sell his/her dollars...')


if __name__ == '__main__':
    our_bank = BankRate()
    first_client = ConcreteClientFirst()
    second_client = ConcreteClientSecond()

    our_bank.attach(first_client)
    our_bank.attach(second_client)

    our_bank.change_currency(30.5, 70)
    our_bank.change_currency(100, 100)

    our_bank.detach(second_client)
    our_bank.change_currency(10, 110)
