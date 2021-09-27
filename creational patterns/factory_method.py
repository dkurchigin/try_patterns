""" EXAMPLE FOR FACTORY METHOD IN PYTHON """
from abc import ABC, abstractmethod
from typing import Union, Type


class AbstractTransport(ABC):
    """ ABSTRACT CLASS """
    def __init__(self):
        self.speed = 0
        self.price = 0

    @abstractmethod
    def show_max_speed(self):
        """ SHOW MAX SPEED """
        pass

    @abstractmethod
    def show_price(self):
        """ SHOW PRICE """
        pass


class MotoTransport(AbstractTransport):
    """ CONCRETE MOTO CLASS """
    def __init__(self):
        super().__init__()
        self.speed = 100
        self.price = 2000

    def show_max_speed(self) -> None:
        print(f'Max speed for moto = {self.speed}')

    def show_price(self) -> None:
        print(f'Price for moto = {self.price}')


class AutoTransport(AbstractTransport):
    """ CONCRETE AUTO CLASS """
    def __init__(self):
        super().__init__()
        self.speed = 80
        self.price = 4000

    def show_max_speed(self) -> None:
        print(f'Max speed for auto = {self.speed}')

    def show_price(self) -> None:
        print(f'Price for auto = {self.price}')


def create_transport(transport_type: Union[Type[MotoTransport], Type[AutoTransport]]) \
        -> Union[MotoTransport, AutoTransport]:
    """ RETURN CREATED CLASS """
    return transport_type()


if __name__ == '__main__':
    various_transport = {'moto': MotoTransport, 'auto': AutoTransport}

    for one_type, transport_class in various_transport.items():
        print(f'\n***{one_type}***')
        one_transport = create_transport(transport_class)
        one_transport.show_max_speed()
        one_transport.show_price()
