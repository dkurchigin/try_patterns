""" EXAMPLE FOR FACADE IN PYTHON """
from __future__ import annotations


class CoolRobot:  # pylint: disable=too-few-public-methods
    """ ITS FACADE FOR OUR ROBOTCLASS """
    def __init__(self, power_system: RobotPowerSystem = None, laser_system: RobotLaserSystem = None,
                 walk_system: RobotWalkSystem = None):
        self._power_system = power_system if power_system else RobotPowerSystem()
        self._laser_system = laser_system if laser_system else RobotLaserSystem()
        self._walk_system = walk_system if laser_system else RobotWalkSystem()

    def get_fun(self):
        """ DIFFICULT CODE INSIDE THE FACADE """
        self._power_system.power_on()
        self._walk_system.power_on()
        self._laser_system.power_on()
        print('-' * 10)
        self._walk_system.move_to(5)
        print('-' * 10)
        self._laser_system.fire()


class RobotPowerSystem:  # pylint: disable=too-few-public-methods
    """ CLASS FOR POWER SYSTEM """
    def power_on(self) -> None:
        """ WE NEED POWER FOR ALL """
        print(self.__class__.__name__, '- ready!')


class RobotLaserSystem:  # pylint: disable=too-few-public-methods
    """ CLASS FOR FIRE SYSTEM """
    def power_on(self) -> None:
        """ WE NEED POWER FOR FIRING """
        print(self.__class__.__name__, '- ready!')

    @staticmethod
    def fire() -> None:
        """ PEW METHOD """
        print('PEW-PEW!!!')


class RobotWalkSystem:
    """ CLASS FOR WALK SYSTEM """
    def power_on(self) -> None:
        """ WE NEED POWER FOR WALKING """
        print(self.__class__.__name__, '- ready!')

    @staticmethod
    def make_step(step_num: int) -> None:
        """ MAKE ONE STEP """
        print(f'Robot make a step {step_num}...')

    def move_to(self, meters: int) -> None:
        """ METHOD FOR ROBOT MOVING STEP BY STEP """
        print(f'Start moving to {meters} meters')
        for step_num in range(1, meters * 2 + 1):
            self.make_step(step_num)
        print('Robot is waiting...')


if __name__ == '__main__':
    power_ = RobotPowerSystem()
    my_robot = CoolRobot(power_)
    my_robot.get_fun()
