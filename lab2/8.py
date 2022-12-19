def addToBankAccount(account,money):
    account += money
    return account

def substractFromBankAccount(account,money):
    if account>=money:
        account -= money
        return account
    else:
        return 'You balance is less than money which you want to substract!'

def moneyConversion(money, m_from, m_to):
    match m_from, m_to:
        case 'USD', 'KZT':
            return money*470
        case 'KZT', 'USD':
            return money/470
        case 'EUR', 'KZT':
            return money*480
        case 'KZT', 'EUR':
            return money/480
        case _:
            return 'Invalid conversion'


print(addToBankAccount(50,100))
print(substractFromBankAccount(500,30))
print(substractFromBankAccount(50,100))
print(moneyConversion(100,'USD','KZT'))