class Account:
    def __init__(self, account_no, owner, balance):
        self.__account_no = account_no
        self.__owner = owner
        self.__balance = balance

    def __str__(self):
        return f'{self.__account_no} \t {self.__owner} \t {self.__balance} '
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_account_no(self):
        return self.__account_no
    def get_owner(self):
        return self.__owner
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount

class AccountService:
    def __init__(self):
        self.__account_list = []

        
    def create_account(self, account_no, owner, balance):
        account = Account(account_no, owner, balance)
        self.__account_list.append(account)
        return True

    def list_account(self):
        return self.__account_list
    
    def deposit(self, account_no, amount):
        for account in self.__account_list:
            if account.get_account_no() == account_no:
                account.deposit(amount)
                break

    def withdraw(self, account_no, amount):
        for account in self.__account_list:
            if account.get_account_no() == account_no:
                account.withdraw(amount)
                break

if __name__ == '__main__':
    ass = AccountService()
    ass.create_account('111-111', 'kkk', 5500)
    print(ass.list_account())
    alist = ass.list_account()
    for accounnt in alist:
        print (accounnt)
    ass.deposit('111-111', 10000)
    for a in alist:
        print(a)