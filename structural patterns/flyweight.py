""" EXAMPLE FOR FLYWEIGHT IN PYTHON """


class ToySoldier:  # pylint: disable=too-few-public-methods
    """ IT'S FLYWEIGHT CLASS """
    def __init__(self, specialization):
        self.specialization = specialization
        self._set_params()

    def _set_params(self):
        if self.specialization == 'bazooka':
            self.damage = 100
        elif self.specialization == 'mg':
            self.damage = 50
        else:
            self.damage = 30

    def play_it(self, name):
        """ PLAY YOUR SOLDIER """
        print(f'{name} like {self.specialization} join to battle!')


class ToySoldiersFactory:
    """ IT'S FACTORY """
    _flyweights = {}

    def __init__(self, initial_flyweights):
        for uniq_spec in initial_flyweights:
            self._flyweights[uniq_spec] = ToySoldier(uniq_spec)

    def get_soldier(self, uniq_spec):
        """ GET EXIST FLYWEIGHT OR CREATE NEW """
        if not self._flyweights.get(uniq_spec):
            self._flyweights[uniq_spec] = ToySoldier(uniq_spec)
        return self._flyweights[uniq_spec]

    def list_flyweights(self):
        """ PRINT ALL FLYWEIGHTS """
        count = len(self._flyweights)
        print(f'TSFactory: I have {count} flyweights:')
        for flyweight in self._flyweights:
            print(f'\t{flyweight}')


def add_soldier_to_play(factory_inst, spec, name):
    """ JUST ADD TOY TO BATTLE """
    flyweight = factory_inst.get_soldier(spec)
    flyweight.play_it(name)


if __name__ == "__main__":
    factory = ToySoldiersFactory(['bazooka', 'mg', 'simple'])
    factory.list_flyweights()
    print('=' * 10)
    add_soldier_to_play(factory, 'bazooka', 'Mustafa')
    add_soldier_to_play(factory, 'mg', 'Hans')
    add_soldier_to_play(factory, 'mg', 'Anka')
    add_soldier_to_play(factory, 'sniper', 'SomeStrangeBoy')
    print('=' * 10)
    factory.list_flyweights()
