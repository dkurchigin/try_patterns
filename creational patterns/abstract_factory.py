""" EXAMPLE FOR ABSTRACT FACTORY METHOD IN PYTHON """
from abc import ABC, abstractmethod
from typing import Union, Type


class Gun(ABC):  # pylint: disable=too-few-public-methods
    """ ABSTRACT GUN """
    @abstractmethod
    def prepare_gun(self):
        """ PREPARE SOME GUN """
        pass


class Ammo(ABC):  # pylint: disable=too-few-public-methods
    """ ABSTRACT AMMO """
    @abstractmethod
    def get_ammo(self):
        """ PREPARE SOME AMMO """
        pass


class Sight(ABC):  # pylint: disable=too-few-public-methods
    """ ABSTRACT SIGHT """
    @abstractmethod
    def setup_sight(self):
        """ PREPARE SOME SIGHT """
        pass


class AkGun(Gun):  # pylint: disable=too-few-public-methods
    """ AK GUN CLASS """
    def prepare_gun(self) -> None:
        print('Our AK ready!')


class AkAmmo(Ammo):  # pylint: disable=too-few-public-methods
    """ AK AMMO CLASS """
    def get_ammo(self) -> None:
        print('Got AK ammo, nice...')


class AkSight(Sight):  # pylint: disable=too-few-public-methods
    """ AK SIGHT CLASS """
    def setup_sight(self) -> None:
        print('It works without sight...')


class ArGun(Gun):  # pylint: disable=too-few-public-methods
    """ AR GUN CLASS """
    def prepare_gun(self) -> None:
        print('It\'s M-16!')


class ArAmmo(Ammo):  # pylint: disable=too-few-public-methods
    """ AR AMMO CLASS """
    def get_ammo(self) -> None:
        print('So small mag for M-16...')


class ArSight(Sight):  # pylint: disable=too-few-public-methods
    """ AR SIGHT CLASS """
    def setup_sight(self) -> None:
        print('It works with cool optics!')


class Armory(ABC):
    """ ABSTRACT ARMORY FACTORY """
    @abstractmethod
    def get_gun(self):
        """ PREPARE SOME GUN """
        pass

    @abstractmethod
    def get_ammo(self):
        """ PREPARE SOME AMMO """
        pass

    @abstractmethod
    def get_sight(self):
        """ PREPARE SOME SIGHT """
        pass


class AkArmory(Armory):
    """ AK FACTORY """
    def get_gun(self) -> AkGun:
        return AkGun()

    def get_ammo(self) -> AkAmmo:
        return AkAmmo()

    def get_sight(self) -> AkSight:
        return AkSight()


class ArArmory(Armory):
    """ AR FACTORY """
    def get_gun(self) -> ArGun:
        return ArGun()

    def get_ammo(self) -> ArAmmo:
        return ArAmmo()

    def get_sight(self) -> ArSight:
        return ArSight()


def start_fight(some_armory: Union[Type[AkArmory], Type[ArArmory]]) -> None:
    """ USE CONCRETE CLASS """
    print(f'---START WORK {some_armory.__name__}---')
    gun_istance = some_armory()
    gun_istance.get_gun().prepare_gun()
    gun_istance.get_ammo().get_ammo()
    gun_istance.get_sight().setup_sight()


if __name__ == '__main__':
    start_fight(AkArmory)
    start_fight(ArArmory)
