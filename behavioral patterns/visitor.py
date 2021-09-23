""" EXAMPLE FOR VISITOR IN PYTHON """
from abc import ABC, abstractmethod


class Cafe(ABC):
    """ ABSTRACT CAFE CLASS """
    def accept(self, visitor):
        """ MAIN METHOD FOR ABSTRACT CAFE """
        visitor.visit(self)

    @abstractmethod
    def make_food_for_vegan(self, vegan):
        """ METHOD FOR VEGAN """
        pass

    @abstractmethod
    def make_food_for_meat_eater(self, meateater):
        """ METHOD FOR MEAT EATER """
        pass

    def speak_with_auditor(self, auditor):
        """ METHOD FOR AUDITOR """
        print(f'\tHi, mister {auditor}')


class VeganCafe(Cafe):
    """ VEGAN CAFE CLASS """
    def make_food_for_vegan(self, vegan):
        print(f'\tSo much food for {vegan}, nice')

    def make_food_for_meat_eater(self, meateater):
        print(f'\tDon\'t have any food for you, {meateater}')


class MeatRestaurant(Cafe):
    """ MEAT RESTAURANT CLASS """
    def make_food_for_vegan(self, vegan):
        print(f'\tDon\'t have any food for you, {vegan}')

    def make_food_for_meat_eater(self, meateater):
        print(f'\tSo much food for {meateater}, great')

    def speak_with_auditor(self, auditor):
        print(f'\tMake diner from {auditor}, lol')


class Visitor(ABC):
    """ MAIN CLASS FOR VISITOR """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def visit(self, some_cafe):
        """ MAIN METHOD FOR VISITOR """
        pass


class MeatEater(Visitor):  # pylint: disable=too-few-public-methods
    """ MEAT EATER CLASS """
    def visit(self, some_cafe):
        some_cafe.make_food_for_meat_eater(self)


class Vegan(Visitor):  # pylint: disable=too-few-public-methods
    """ VEGAN CLASS """
    def visit(self, some_cafe):
        some_cafe.make_food_for_vegan(self)


class Auditor(Visitor):  # pylint: disable=too-few-public-methods
    """ AUDITOR CLASS """
    def visit(self, some_cafe):
        some_cafe.speak_with_auditor(self)


if __name__ == '__main__':
    first_visitor = Vegan('Peter')
    second_visitor = MeatEater('Nick')
    third_visitor = Auditor('Bob')

    vegan_cafe = VeganCafe()
    meat_restaurant = MeatRestaurant()

    print('Visitors are visiting vegan cafe:')
    vegan_cafe.accept(first_visitor)
    vegan_cafe.accept(second_visitor)
    vegan_cafe.accept(third_visitor)

    print('\nVisitors are visiting meat restaurant:')
    meat_restaurant.accept(first_visitor)
    meat_restaurant.accept(second_visitor)
    meat_restaurant.accept(third_visitor)
