from abc import ABC
from enum import Enum
import unittest


class BankAccount:
    """This is an implementation without commands or transactions (using perishable statements).

    Returns:
        _type_: _description_
    """
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance += amount
            # print(f'Deposited ${amount}. {self}')
        except:
            print('Error')
        else:
            return True

    def withdraw(self, amount):
        if self.balance - amount < BankAccount.OVERDRAFT_LIMIT:
            return False

        self.balance -= amount
        # print(f'Withdrew ${amount}. {self}')
        return True

    def __str__(self):
        return f'Current Balance ${self.balance}'


class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        ...

    def undo(self):
        ...


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account: BankAccount, action: Action, amount):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

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


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        self.extend(items)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_account, to_account, amount):
        super().__init__([
            BankAccountCommand(from_account, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_account, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False

        self.success = ok


class TestSuit(unittest.TestCase):
    # def test_composite_deposit(self):
    #     account = BankAccount()

    #     deposit1 = BankAccountCommand(account, BankAccountCommand.Action.DEPOSIT, 200)
    #     deposit2 = BankAccountCommand(account, BankAccountCommand.Action.DEPOSIT, 30)

    #     composite = CompositeBankAccountCommand(
    #         [deposit1, deposit2]
    #     )
    #     composite.invoke()

    #     # print(account)
    #     composite.undo()
    #     # print(account)

    # def test_transfer_fail(self):
    #     account1 = BankAccount(100)
    #     account2 = BankAccount()

    #     amount = 100
    #     withdrawal_command = BankAccountCommand(account1, BankAccountCommand.Action.WITHDRAW, amount)
    #     deposit_command = BankAccountCommand(account2, BankAccountCommand.Action.DEPOSIT, amount)

    #     transfer = CompositeBankAccountCommand([withdrawal_command, deposit_command])
    #     transfer.invoke()
    #     print('Hey', account1)
    #     print(account2)
    #     transfer.undo()
    #     print(account1)
    #     print(account2)

    def test_better_transfer(self):
        print('Best transfer')
        account1 = BankAccount(100)
        account2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(account1, account2, amount)

        transfer.invoke()

        print(account1, account2)

        transfer.undo()

        print(account1, account2)

        print('Transfer success', transfer.success)

        print('===============')

if __name__ == '__main__':
    unittest.main()
