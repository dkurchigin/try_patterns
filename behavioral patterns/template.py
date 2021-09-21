""" EXAMPLE FOR TEMPLATE IN PYTHON """
from abc import ABC, abstractmethod


class Sandwich(ABC):
    """ ABSTRACT SANDWICH """
    def make_it(self):
        """ MAIN TEMPLATE METHOD """
        self.append_top_bread()
        self.append_onion()
        self.append_cheese()
        self.append_some_meat()
        self.append_fish()
        self.append_salad()
        self.append_sauce()
        self.append_bottom_bread()

    @abstractmethod
    def append_bottom_bread(self):
        """ ABSTRACT METHOD FOR BOTTOM BREAD """
        pass

    @abstractmethod
    def append_top_bread(self):
        """ ABSTRACT METHOD FOR TOP BREAD """
        pass

    def append_some_meat(self):
        """ ABSTRACT METHOD FOR MEAT """
        pass

    def append_salad(self):
        """ ABSTRACT METHOD FOR SALAD """
        pass

    def append_onion(self):
        """ ABSTRACT METHOD FOR ONION """
        pass

    def append_sauce(self):
        """ ABSTRACT METHOD FOR SAUSE """
        pass

    def append_fish(self):
        """ ABSTRACT METHOD FOR FISH """
        pass

    def append_cheese(self):
        """ ABSTRACT METHOD FOR CHEESE """
        pass


class FishSandwich(Sandwich):
    """ MEAT SANDWICH REALIZATION """
    def append_bottom_bread(self):
        print('- start with some bread')

    def append_fish(self):
        print('- append nice fish')

    def append_sauce(self):
        print('- append tar-tar')

    def append_top_bread(self):
        print('- finish with some bread too')


class MeatSandwich(Sandwich):
    """ MEAT SANDWICH REALIZATION """
    def append_bottom_bread(self):
        print('- start with bread for meat sandwich')

    def append_cheese(self):
        print('- wow, i like cheese')

    def append_some_meat(self):
        print('- append meat, nice')

    def append_sauce(self):
        print('- append barbecue sauce')

    def append_top_bread(self):
        print('- finish with bread for meat sandwich')


if __name__ == '__main__':
    sandwich_with_fish = FishSandwich()
    sandwich_with_meat = MeatSandwich()

    print('MAKE FISH SANDWICH:')
    sandwich_with_fish.make_it()
    print('\nMAKE MEAT SANDWICH:')
    sandwich_with_meat.make_it()
