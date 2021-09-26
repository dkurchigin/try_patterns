""" EXAMPLE FOR BRIDGE IN PYTHON """
from abc import ABC, abstractmethod


class TV(ABC):
    """ ABSTRACT TV """
    @abstractmethod
    def tv_on(self):
        """ TV ON METHOD """
        pass

    @abstractmethod
    def tv_off(self):
        """ TV OFF METHOD """
        pass

    @abstractmethod
    def tune_channel(self, channel: int):
        """ CNAHGE TV CHANNEL """
        pass


class SonyTV(TV):
    """ EXTEND TV ABSTRACTION FOR SONY """
    def tv_on(self) -> None:
        print('Turn on SonyTV')

    def tv_off(self) -> None:
        print('Turn off SonyTV')

    def tune_channel(self, channel: int) -> None:
        print(f'Tune channel #{channel} on SonyTV')


class LgTV(TV):
    """ EXTEND TV ABSTRACTION FOR LG """
    def tv_on(self) -> None:
        print('Turn on LgTV')

    def tv_off(self) -> None:
        print('Turn off LgTV')

    def tune_channel(self, channel: int) -> None:
        print(f'Tune channel #{channel} on LgTV')


class RemoteControl(ABC):
    """ ABSTRACT RC """
    def __init__(self, some_tv: TV):
        self.some_tv = some_tv

    def rc_on(self) -> None:
        """ CLICK TV ON """
        self.some_tv.tv_on()

    def rc_off(self) -> None:
        """ CLICK TV OFF """
        self.some_tv.tv_off()


class ConcreteRemote(RemoteControl):
    """ CLASS FOR CONCRETE RC IMPLEMENTATION """
    def __init__(self, some_tv: TV):
        super().__init__(some_tv)
        self.channel: int = 10

    def prev_channel(self) -> None:
        """ CLICK PREVIOUS CHANNEL ON RC """
        self.channel -= 1
        self.some_tv.tune_channel(self.channel)

    def next_channel(self) -> None:
        """ CLICK NEXT CHANNEL ON RC """
        self.channel += 1
        self.some_tv.tune_channel(self.channel)


if __name__ == '__main__':
    first_rc = ConcreteRemote(SonyTV())
    first_rc.rc_on()
    first_rc.next_channel()
    first_rc.rc_off()
    print('-' * 20)
    second_rc = ConcreteRemote(LgTV())
    second_rc.rc_on()
    second_rc.prev_channel()
    second_rc.rc_off()
