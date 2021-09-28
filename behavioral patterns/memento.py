""" EXAMPLE FOR MEMENTO IN PYTHON """
from abc import ABC, abstractmethod
from datetime import datetime
import uuid
import time
from typing import List


class Memento(ABC):
    """ ABSTRACT MEMENTO """
    @abstractmethod
    def get_date(self):
        """ GET DATE """
        pass

    @abstractmethod
    def get_entry(self):
        """ GET ENTRY """
        pass


class RandomTextFile(Memento):
    """ CONCRETE MEMENTO FOR FILE ENTRY """
    def __init__(self, entry: str):
        self._entry = entry
        self._date = datetime.now()

    def get_date(self) -> datetime:
        return self._date

    def get_entry(self) -> str:
        return self._entry


class Originator:
    """ ORIGINATOR FOR MANIPULATING """
    def __init__(self):
        self._entry = ''

    def append_random_string(self) -> None:
        """ JUST APPEND STRING """
        self._entry += f'{self._generate_random_string()}\n'

    @staticmethod
    def _generate_random_string() -> uuid.UUID:
        return uuid.uuid4()

    def save(self) -> RandomTextFile:
        """ SAVE METHOD """
        return RandomTextFile(self._entry)

    def restore(self, some_file: RandomTextFile) -> None:
        """ RESTORE METHOD """
        self._entry = some_file.get_entry()

    def print_file(self) -> None:
        """ BACKUP METHOD """
        print(f'\n{self._entry}\n')


class Caretaker:
    """ CARETAKER CLASS """
    def __init__(self, some_originator: Originator):
        self._mementos: List[RandomTextFile] = []
        self._originator = some_originator

    def backup(self) -> None:
        """ BACKUP METHOD """
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        """ ROLLBACK METHOD """
        if not self._mementos:
            return

        self._mementos.pop()
        last_memento = self._mementos[-1]
        print('\tCaretaker: Rollback last...')
        try:
            self._originator.restore(last_memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        """ SHOW ALL BACKUPS """
        for memento in self._mementos:
            print(f'\t{memento.get_date()} entry length = {len(memento.get_entry())}')


if __name__ == "__main__":
    editor = Originator()
    file_state = Caretaker(editor)

    editor.append_random_string()
    file_state.backup()
    print('Added one string and backuped...')
    file_state.show_history()
    time.sleep(0.3)

    editor.append_random_string()
    editor.append_random_string()
    file_state.backup()
    print('Added two string and backuped...')
    file_state.show_history()
    time.sleep(0.3)

    editor.append_random_string()
    file_state.backup()
    print('Added one string and...')
    file_state.show_history()
    time.sleep(0.3)

    print("STOP! WE NEED ROLLBACK LAST CHANGES!")
    file_state.undo()

    print('Now it\'s good:')
    file_state.show_history()
    print('Our file:')
    editor.print_file()
