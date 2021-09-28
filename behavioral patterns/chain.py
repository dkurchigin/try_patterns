""" EXAMPLE FOR CHAIN OF RESPONSIBILITY IN PYTHON """
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union


class Handler(ABC):
    """ ABSTRACT HANDLER """
    @abstractmethod
    def set_next(self, handler):
        """ NEXT HANDLER METHOD """
        pass

    @abstractmethod
    def handle(self, request):
        """ HANDLE METHOD """
        pass


class AbstractHandler(Handler):
    """ ABSTRACT CLOTHES HANDLER """
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class UndershirtHandler(AbstractHandler):
    """ CLASS FOR UNDERSHIRT """
    def handle(self, request: str) -> Union[UndershirtHandler, ShirtHandler, JacketHandler, str]:
        if request == 'Undershirt':
            return f'Done! I undressed {request}!'
        return super().handle(request)


class ShirtHandler(AbstractHandler):
    """ CLASS FOR SHIRT """
    def handle(self, request: str) -> Union[UndershirtHandler, ShirtHandler, JacketHandler, str]:
        if request == 'Shirt':
            return f'Nice! I undressed {request}!'
        return super().handle(request)


class JacketHandler(AbstractHandler):
    """ CLASS FOR JACKET """
    def handle(self, request: str) -> Union[UndershirtHandler, ShirtHandler, JacketHandler, str]:
        if request == 'Jacket':
            return f'Cool! I undressed {request}!'
        return super().handle(request)


def strip_down_to(handler: Union[UndershirtHandler, ShirtHandler, JacketHandler],
                  request: str) -> None:
    """ STRIPTEASE! """
    result = handler.handle(request)
    if result:
        print(result)
    else:
        print(f'I can\'t undress {request}')


if __name__ == '__main__':
    jacket = JacketHandler()
    shirt = ShirtHandler()
    undershirt = UndershirtHandler()

    jacket.set_next(shirt).set_next(undershirt)
    strip_down_to(jacket, 'Shirt')
    strip_down_to(jacket, 'Pants')
