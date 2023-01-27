import sys
from Account import Account


class BankAccount:
    name: str
    surname: str
    account: Account
    _amount: float

    def __init__(self, name: str, surname: str, account: Account,) -> None:
        self.name=name
        self.surname=surname
        self.account=account
        self._amount=0
        
    def addToBankAccount(self, money: float) -> None:
        self._amount+=money
        print("Succesfully added!")

    def substractFromBankAccount(self, money: float) -> None:
        if(money>self._amount):
            print('You dont have enough money!')
        else:
            self._amount-=money
    
    def money_conversion(self, new_account_type: Account) -> None:
        if(new_account_type==Account.KZT):
            if(self.account==Account.EUR):
                self._amount*=504
            elif(self.account==Account.RUB):
                self._amount*=6.7
            elif(self.account==Account.USD):
                self._amount*=462
            self.account=Account.KZT
        elif(new_account_type==Account.EUR):
            if(self.account==Account.KZT):
                self._amount/=504
            elif(self.account==Account.RUB):
                self._amount/=75
            elif(self.account==Account.USD):
                self._amount/=1.1
            self.account=Account.EUR
        elif(new_account_type==Account.USD):
            if(self.account==Account.KZT):
                self._amount/=462
            elif(self.account==Account.RUB):
                self._amount/=68
            elif(self.account==Account.EUR):
                self._amount*=1.1
            self.account=Account.USD
        elif(new_account_type==Account.RUB):
            if(self.account==Account.KZT):
                self._amount/=6.7
            elif(self.account==Account.EUR):
                self._amount*=75
            elif(self.account==Account.USD):
                self._amount*=69
            self.account=Account.RUB


    def get_amount(self) -> float:
        return f'{self._amount} {self.account.value}'
    
    def set_amount(self, new_amount: float) -> None:
        self._amount=new_amount

    def __repr__(self) -> str:
        return f'{self.name} {self.surname}'
    
    def __del__(self) -> None:
        print(f'{self.name} {self.surname} account has been deleted')

bank_accounts=[]

while True:
    command = int(input('Choose your action: \n1. Creating a user \n2. Select a user \n3. Quit\n'))

    if(command==1):
        name = input('Please, Enter your name: ')
        surname = input('Enter your surname: ')
        wallet_type = input('Enter wallet type: ')
        if wallet_type==Account.EUR.value or wallet_type==Account.USD.value or wallet_type==Account.KZT.value or wallet_type==Account.RUB.value:
            bank_account = BankAccount(name=name, surname=surname, account=Account(wallet_type))
            bank_accounts.append(bank_account)
        else:
            print('Invalid wallet type!')
    elif command==2:
        name, surname = input('Enter your creds: ').split(' ')
        bank_account = next((bankaccount for bankaccount in bank_accounts if name == bankaccount.name and surname == bankaccount.surname),None)
        if bank_account:
            logout = False
            while not logout:
                com_act = int(input
                ('Choose your action: \n1. Add to bank account \n2. Subtract from bank account\n3. Money conversion \n4. Get amount \n5. Set amount \n6. Log out\n')
                )
                if com_act==1:
                    money = int(input('Enter the amount to add:'))
                    bank_account.addToBankAccount(money=money)
                    print(bank_account.get_amount())

                elif com_act==2:
                    money = int(input('Enter the amount to substract:'))
                    bank_account.substractFromBankAccount(money=money)
                    print(bank_account.get_amount())

                elif com_act==3:
                    currency_type=input('Enter a new currency type: ')
                    if currency_type==Account.EUR.value or currency_type==Account.USD.value or currency_type==Account.KZT.value or currency_type==Account.RUB.value:
                        bank_account.money_conversion(Account(currency_type))
                        print(bank_account.get_amount())
                    else:
                        print('Invalid currency type!')

                elif com_act==4:
                    print(bank_account.get_amount())

                elif com_act==5:
                    money = int(input('Enter the amount:'))
                    bank_account.set_amount(money)
                    print(bank_account.get_amount())

                elif com_act==6:
                    logout=True

                else:
                    print("Invalid command, try again: ")

        else:
            print('Bank account have not found!')
    elif command==3:
        sys.exit(0)
    else:
        print("Invalid command, try again: ")
            

