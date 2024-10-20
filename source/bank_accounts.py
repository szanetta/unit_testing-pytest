class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f'Account "{self.name}" created. Balance = $ {self.balance: .2f}')

    def getBalance(self):
        print(f'Account "{self.name}" balance = $ {self.balance: .2f}')

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Deposit complete.')
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f'Sorry, account "{self.name}" only has a balance of ${self.balance: .2f}')

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print('Withdraw complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'Withdraw interrupted: {error}')


    def transfer(self, amount, account):
        try:
            print(' \n\n ******* Beginning Transfer...🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer complete. ✔ \n\n *******')
        except BalanceException as error:
            print(f'Transfer interrupted. ❌ {error} \n\n *******')