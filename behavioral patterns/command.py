""" EXAMPLE FOR COMMAND IN PYTHON """
from abc import ABC, abstractmethod
from typing import Union, List


class RobotSteward:
    """ CLASS FOR OUR ROBOT """
    @staticmethod
    def do_something(some_command):
        """ DO SOMETHING FOR ROBOT """
        print(f'I\'m working on {some_command}!')

    @staticmethod
    def cancel_something(some_command):
        """ CANCEL SOMETHING FOR ROBOT """
        print(f'{some_command} was canceled!')


class Command(ABC):
    """ SOME COMMAND """
    @abstractmethod
    def do_it(self):
        """ DO SOME ACTION """
        pass

    @abstractmethod
    def cancel_it(self):
        """ CANCEL SOME ACTION """
        pass


class CookCommand(Command):
    """ COOKING COMMAND CLASS """
    def __init__(self, steward: RobotSteward):
        self.steward = steward

    def do_it(self) -> None:
        self.steward.do_something('COOKING')

    def cancel_it(self) -> None:
        self.steward.cancel_something('COOKING')


class CleanCommand(Command):
    """ CLEANING COMMAND CLASS """
    def __init__(self, steward: RobotSteward):
        self.steward = steward

    def do_it(self) -> None:
        self.steward.do_something('CLEANING')

    def cancel_it(self) -> None:
        self.steward.cancel_something('CLEANING')


class RobotInterface:
    """ CLASS FOR CONTROLING OUR ROBOT """
    def __init__(self, cooking_command: CookCommand, cleaning_command: CleanCommand):
        self.cooking_command = cooking_command
        self.cleaning_command = cleaning_command
        self._command_list: List[Union[CookCommand, CleanCommand]] = []

    def append_cook(self) -> None:
        """ ADD COOKING """
        print('Add cooking in command queue...')
        self._command_list.append(self.cooking_command)

    def append_clean(self) -> None:
        """ ADD CLEANING """
        print('Add cleaning in command queue...')
        self._command_list.append(self.cleaning_command)

    def cancel_last(self) -> None:
        """ CANCEL LAST COMMAND """
        command_for_cancel = self._command_list[-1]
        command_for_cancel.cancel_it()
        self._command_list.pop()

    def run_all(self) -> None:
        """ RUN ALL COMMANDS ONE BY ONE """
        print('-' * 10)
        for command in self._command_list:
            command.do_it()
        print('All done!')


if __name__ == '__main__':
    robot = RobotSteward()
    robot_interface = RobotInterface(CookCommand(robot), CleanCommand(robot))

    robot_interface.append_cook()
    robot_interface.append_cook()
    robot_interface.cancel_last()
    robot_interface.append_clean()
    robot_interface.append_cook()
    robot_interface.run_all()
