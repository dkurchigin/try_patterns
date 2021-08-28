""" EXAMPLE FOR SINGLETON IN PYTHON """
from threading import Lock, Thread


class SingletonMeta(type):
    """ SINGLETON METACLASS """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):  # pylint: disable=too-few-public-methods
    """ OUR SINGLETON """
    def __init__(self, name):
        self.name = name

    def work_with_db(self):
        """ DO SOMETHING IN SINGLETON """
        print(f'\t{self.name}: It\'s so LONELY db connection')


if __name__ == '__main__':
    print('Create first connection by singleton')
    first_connection = Thread(target=Singleton('first').work_with_db())
    print('Create second connection by singleton')
    second_connection = Thread(target=Singleton('second').work_with_db())
    first_connection.start()
    second_connection.start()
