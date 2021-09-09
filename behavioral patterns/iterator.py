""" EXAMPLE FOR ITERATOR IN PYTHON """
from collections.abc import Iterable, Iterator


class Car:  # pylint: disable=too-few-public-methods
    """ CLASS FOR ONE CAR """
    def __init__(self, name, price, horse_power):
        self.name = name
        self.price = price
        self.horse_power = horse_power

    def __repr__(self):
        return f'{self.name}:{self.price}:{self.horse_power}'


class CarIterator(Iterator):
    """ BASE CAR ITERATOR """
    def __init__(self, collection):
        self.cars = collection.get_cars()
        self.cursor = len(self.cars)
        self.sort(self.cars)

    def sort(self, cars_for_sort):
        """ ABSTRACT SORT METHOD """
        pass

    def __next__(self):
        try:
            if self.cursor < 0:
                raise IndexError()
            value = self.cars[self.cursor]
            self.cursor += 1
            return value
        except IndexError:
            raise StopIteration()


class CarNameIterator(CarIterator):  # pylint: disable=too-few-public-methods
    """ ITERATOR BY NAME """
    def sort(self, cars_for_sort):
        self.cars = sorted(cars, key=lambda car: car.name)


class CarPriceIterator(CarIterator):  # pylint: disable=too-few-public-methods
    """ ITERATOR BY PRICE """
    def sort(self, cars_for_sort):
        self.cars = sorted(cars, key=lambda car: car.price)


class CarHorsePowerIterator(CarIterator):  # pylint: disable=too-few-public-methods
    """ ITERATOR BY HP """
    def sort(self, cars_for_sort):
        self.cars = sorted(cars, key=lambda car: car.horse_power)


class CarCollection(Iterable):
    """ CAR COLLECTION """
    def __init__(self):
        self._cars = []
        self.default_iterator = self.sort_by_name

    def add_car(self, some_car):
        """ ADD ONE CAR """
        self._cars.append(some_car)

    def get_cars(self):
        """ GET CARS """
        return self._cars

    def __iter__(self):
        return self.default_iterator()

    def sort_by_name(self):
        """ SORT BY NAME """
        return CarNameIterator(self)

    def sort_by_price(self):
        """ SORT BY PRICE """
        return CarPriceIterator(self)

    def sort_by_horse_power(self):
        """ SORT BY HP """
        return CarHorsePowerIterator(self)


if __name__ == '__main__':
    cars = CarCollection()

    cars.add_car(Car('Lamba', 1000, 1000))
    cars.add_car(Car('BMW', 500, 500))
    cars.add_car(Car('VW', 550, 400))
    cars.add_car(Car('Lada', 50, 100))

    print('Cars without sort:')
    print(f'{cars.get_cars()}\n')
    print('Cars sorted by name:')
    print(f'{cars.sort_by_name().cars}\n')
    print('Cars sorted by price:')
    print(f'{cars.sort_by_price().cars}\n')
    print('Cars sorted by horse_power:')
    print(f'{cars.sort_by_horse_power().cars}\n')
