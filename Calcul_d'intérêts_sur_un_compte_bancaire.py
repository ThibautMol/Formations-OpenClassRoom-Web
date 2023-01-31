"""Calcul d'intérêts sur un compte bancaire"""

savingsAccount = 10000
rate = 0.75
interest = (savingsAccount*rate)/100
print("your account balance was", savingsAccount)
print("your earned", interest)
print("new bank account is", interest+savingsAccount)