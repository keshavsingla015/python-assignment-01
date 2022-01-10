income = int(input('enter your income:$ '))
dependents = int(input("number of dependents on you: "))

income_tax = (income*0.20) - 10000 - (dependents*3000)

payable_tax = str(max(0,income_tax))

print('your payable tax is $' + payable_tax)
