""" EXAMPLE FOR MEDIATOR IN PYTHON """
from abc import ABC, abstractmethod


class Mediator(ABC):  # pylint: disable=too-few-public-methods
    """ABSTRACT MEDIATOR """
    def execute(self, sender, event):
        """ IT'S MEDIATOR MAIN LOGIC """
        pass


class Worker(ABC):
    """ ABSTRACT WORKER """
    def __init__(self):
        self._mediator = None

    @abstractmethod
    def set_mediator(self, mediator):
        """ SET MEDIATOR """
        pass

    @abstractmethod
    def do_task(self, task_type):
        """ DO SOMETHING """
        pass


class Commander(Worker):
    """ CLASS FOR COMMANDER """
    def set_mediator(self, mediator):
        self._mediator = mediator

    def start_reload(self):
        """ START RELOADING """
        self.do_task('reloading')
        self._mediator.execute(self, 'reloading')

    def keep_fire(self):
        """ START FIRING """
        self.do_task('fire')
        self._mediator.execute(self, 'fire')

    def do_task(self, task_type):
        print(f'Commander: {task_type}')


class Loader(Worker):
    """ CLASS FOR LOADER """
    def set_mediator(self, mediator):
        self._mediator = mediator

    def do_task(self, task_type):
        print(f'Loader: {task_type}')
        self._mediator.execute(self, 'reloading')


class Gunner(Worker):
    """ CLASS FOR GUNNER """
    def set_mediator(self, mediator):
        self._mediator = mediator

    def do_task(self, task_type):
        print(f'Gunner: {task_type}')
        self._mediator.execute(self, 'fire')


class GunTeam(Mediator):  # pylint: disable=too-few-public-methods
    """ MAIN MEDIATOR FOR GUNTEAM """
    def __init__(self, commander, loader, gunner):
        self._commander = commander
        self._commander.set_mediator(self)
        self._loader = loader
        self._loader.set_mediator(self)
        self._gunner = gunner
        self._gunner.set_mediator(self)
        self._is_loaded = False

    def execute(self, sender, event):
        if event == 'reloading':
            if isinstance(sender, Commander):
                self._loader.do_task(event)
            elif isinstance(sender, Loader):
                if not self._is_loaded:
                    self._is_loaded = True
                    print('-GunTeam- : gun loaded...\n')
                else:
                    print('-GunTeam- : gun already loaded...\n')
        elif event == 'fire':
            if isinstance(sender, Commander):
                self._gunner.do_task(event)
            if isinstance(sender, Gunner):
                if self._is_loaded:
                    print('-GunTeam- : BOOM!\n')
                    self._is_loaded = False
                else:
                    print('-GunTeam- : can\'t fire! Gun empty!\n')


if __name__ == '__main__':
    team_commander = Commander()
    main_gunner = Gunner()
    fast_loader = Loader()
    commands_list = GunTeam(team_commander, fast_loader, main_gunner)

    team_commander.start_reload()
    team_commander.keep_fire()
    team_commander.keep_fire()
