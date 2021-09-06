""" EXAMPLE FOR DECORATOR IN PYTHON """
from abc import ABC, abstractmethod


class Operator(ABC):  # pylint: disable=too-few-public-methods
    """ ABSTRACT Operator """

    @abstractmethod
    def operation(self):
        """ SOME MATH OPERATION METHOD """
        pass


class InitialClass(Operator):  # pylint: disable=too-few-public-methods
    """ IT'S X """
    def __init__(self, value=10):
        self.value = value

    def operation(self):
        return self.value


class DoublingClass(Operator):  # pylint: disable=too-few-public-methods
    """ X * 2 """
    def __init__(self, some_obj):
        self.some_obj = some_obj

    def operation(self):
        return self.some_obj.operation() * 2


class AddingTwoClass(Operator):  # pylint: disable=too-few-public-methods
    """ X + 2 """

    def __init__(self, some_obj):
        self.some_obj = some_obj

    def operation(self):
        return self.some_obj.operation() + 2


if __name__ == '__main__':
    print('Fun programming and math!\n')
    init_value = InitialClass()
    first_variant = DoublingClass(AddingTwoClass(DoublingClass(init_value)))
    second_variant = AddingTwoClass(DoublingClass(AddingTwoClass(init_value)))

    print('First variant:', first_variant.operation())
    print('Second variant:', second_variant.operation())
