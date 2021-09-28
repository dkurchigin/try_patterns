""" EXAMPLE FOR STATE IN PYTHON """
from abc import ABC, abstractmethod
from typing import Union


class State(ABC):
    """ CLASS FOR STATE """
    @abstractmethod
    def attack(self):
        """ ABSTRACT ATTACK METHOD """
        pass

    @abstractmethod
    def run(self):
        """ ABSTRACT RUN METHOD """
        pass

    @abstractmethod
    def sleep(self):
        """ ABSTRACT SLEEP METHOD """
        pass


class LikeApeState(State):
    """ APE BEHAVIOR """
    def attack(self) -> None:
        print('Throw banana!')

    def run(self) -> None:
        print('Fast moving through the trees')

    def sleep(self) -> None:
        print('Sleep in the trees')


class LikeLionState(State):
    """ LION BEHAVIOR """
    def attack(self) -> None:
        print('Roar and attack!')

    def run(self) -> None:
        print('Fast moving through the savannah')

    def sleep(self) -> None:
        print('Sleep on the earth, meow')


class Chamelion:
    """ OUR HAMELION CLASS """
    def __init__(self):
        self._state = None

    def change_behavior(self, state: Union[LikeApeState, LikeLionState]) -> None:
        """ CHANGE BEHAVIOR LIKE... """
        self._state = state

    def attack(self) -> None:
        """ TRY ATTACK LIKE... """
        self._do_something('attack')

    def run(self) -> None:
        """ TRY RUN LIKE... """
        self._do_something('run')

    def sleep(self) -> None:
        """ TRY SLEEP LIKE... """
        self._do_something('sleep')

    def _do_something(self, operation: str) -> None:
        try:
            func = getattr(self._state, operation)
            func()
        except AttributeError:
            print('Chamelion can\'t do that')


if __name__ == '__main__':
    lion_behavior = LikeLionState()
    ape_behavior = LikeApeState()

    our_chamelion = Chamelion()
    our_chamelion.change_behavior(lion_behavior)
    our_chamelion.attack()
    our_chamelion.run()
    our_chamelion.change_behavior(ape_behavior)
    our_chamelion.sleep()
