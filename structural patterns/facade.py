class CoolRobot:
    def __init__(self, power_system=None, laser_system=None, walk_system=None):
        self._power_system = power_system if power_system else RobotPowerSystem()
        self._laser_system = laser_system if laser_system else RobotLaserSystem()
        self._walk_system = walk_system if laser_system else RobotWalkSystem()

    def get_fun(self):
        self._power_system.power_on()
        self._walk_system.power_on()
        self._laser_system.power_on()
        print('-' * 10)
        self._walk_system.move_to(5)
        print('-' * 10)
        self._laser_system.fire()


class RobotPowerSystem:
    def power_on(self):
        print(self.__class__.__name__, '- ready!')


class RobotLaserSystem:
    def power_on(self):
        print(self.__class__.__name__, '- ready!')

    @staticmethod
    def fire():
        print('PEW-PEW!!!')


class RobotWalkSystem:
    def power_on(self):
        print(self.__class__.__name__, '- ready!')

    @staticmethod
    def make_step(step_num):
        print(f'Robot make a step {step_num}...')

    def move_to(self, meters):
        print(f'Start moving to {meters} meters')
        for step_num in range(1, meters * 2 + 1):
            self.make_step(step_num)
        print('Robot is waiting...')


if __name__ == '__main__':
    power_ = RobotPowerSystem()
    my_robot = CoolRobot(power_)
    my_robot.get_fun()
