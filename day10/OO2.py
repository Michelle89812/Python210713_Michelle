from day10 import Bank

if __name__ == '__main__':
    account = Bank.Account()
    account.name = 'John'
    account.saving(10000)
    account.withdraw(6000)
    account.withdraw(5000)
    account.saving(-2000)

