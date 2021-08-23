""" EXAMPLE FOR PROXY IN PYTHON """
from abc import ABC, abstractmethod


class AbstractBank(ABC):
    """ ABSTRACT BANK """
    @abstractmethod
    def get_money(self, query, user):
        """ GET MY MONEY """
        pass

    @abstractmethod
    def get_balance(self, user):
        """ GET BANK BALANCE """
        pass


class RealBank(AbstractBank):
    """ IT'S REAL BANK """
    def __init__(self):
        self.so_much_money = 500

    def get_money(self, query, user):
        self.so_much_money -= query
        print(f'RealBank: {user} got {query}$')

    def get_balance(self, user):
        print(f'RealBank: balance {self.so_much_money}$')


class BankProxy(AbstractBank):
    """ CLASS FOR SAFE AND LOG """
    def __init__(self, real_bank_instance: RealBank):
        self.real_bank = real_bank_instance

    @staticmethod
    def _check_privileges(user):
        return bool(user not in ('blocked_user', 'pupa', 'lupa'))

    def get_money(self, query, user):
        print(f'BankProxy: check money privileges for {user}...')
        if self._check_privileges(user):
            self.real_bank.get_money(query, user)
        else:
            print(f'BankProxy: you can\'t get money, {user}')

    def get_balance(self, user):
        print(f'BankProxy: check balance privileges for {user}...')
        if self._check_privileges(user):
            self.real_bank.get_balance(user)
        else:
            print(f'BankProxy: you can\'t get balance, {user}')


if __name__ == '__main__':
    real_bank = RealBank()

    print('Start use bank proxy!')
    safe_bank = BankProxy(real_bank)
    safe_bank.get_money(100, 'pupa')
    safe_bank.get_balance('pupa')
    safe_bank.get_money(100, 'za-lupa')
    safe_bank.get_balance('jonh')
