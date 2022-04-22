from abc import ABC
from enum import Enum


class BankAccount:
    """This is an implementation without commands or transactions (using perishable statements).

    Returns:
        _type_: _description_
    """
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance += amount
            print(f'Deposited ${amount}. {self}')
        except:
            print('Error')
        else:
            return True

    def withdraw(self, amount):
        if self.balance - amount < BankAccount.OVERDRAFT_LIMIT:
            return False

        self.balance -= amount
        print(f'Withdrew ${amount}. {self}')
        return True

    def __str__(self):
        return f'Current Balance ${self.balance}'


class Command(ABC):
    def invoke(self):
        ...

    def undo(self):
        ...

    
class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account: BankAccount, action: Action, amount):
        self.account = account
        self.action = action
        self.amount = amount
        self.success = False

    def invoke(self):
        response = False

        if self.action == self.Action.DEPOSIT:
            response = self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            response = self.account.withdraw(self.amount)

        self.success = response

    def undo(self):
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == '__main__':
    account = BankAccount(1000)

    cmd = BankAccountCommand(account, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print(account)
    cmd = BankAccountCommand(account, BankAccountCommand.Action.WITHDRAW, 400)
    cmd.invoke()
    print(account)

    cmd.undo()
    print(account)

    cmd = BankAccountCommand(account, BankAccountCommand.Action.WITHDRAW, 50000)
    cmd.invoke()

    print(account)

    cmd.undo()
    print(account)