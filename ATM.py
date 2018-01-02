# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 17:52:07 2017

@author: longk
"""

class Account:
    def __init__(self,acc_id):
        self.acc_id=acc_id

class Checkingaccount(Account):
    def __init__(self,acc_id,deposit_amount):
        Account.__init__(self,acc_id)
        self.amount = deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.amount:
            self.amount = self.amount - withdraw_amount
            print("the remained amount of your checking account is %d" % self.amount)
        else :
            print("your balance is insufficient")
    def deposit(self,deposit_amount):
        self.amount += deposit_amount
        print("the amount of your checking account is %d" % self.amount)
        
    def display_acc(self):
        print(self.amount)

    def get_amount(self):
        return self.amount
    
class Businessaccount(Account):
    def __init__(self,acc_id,creditline,debt,deposit_amount):
        Account.__init__(self,acc_id)
        self.creditline = creditline
        self.debt = debt
        self.amount = deposit_amount
        self.debt_ratio = (debt/creditline) 
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.amount:
            self.amount = self.amount - withdraw_amount
            print("the remained amount of your checking account is %d" % self.amount)
        else:
            print("your balance is insufficient")
        
    def deposit(self,deposit_amount):
        self.amount += self.deposit_amount
        print("the amount of your checking account is %d" % self.amount)
    
    def display_acc(self):
        print(self.amount)
        
    def get_amount(self):
        return self.amount

### application

if __name__ == '__main__':
    isSessionOn = True
    isCustomer = False
    
    def initializeObject():
        global Sally_checking,Paolo_checking,Paolo_business,master_list
        Sally_checking = Checkingaccount(1,2567.50)
        Paolo_checking = Checkingaccount(2,2000.23)
        Paolo_business = Businessaccount(2,10000,2000,3500.32)
        
        master_list = [[Sally_checking,1,1],[Paolo_checking,2,1],[Paolo_business,2,2]]
        
        return None
    
    initializeObject()
    while isSessionOn == True:
        print("welcome to use BOA's ATM")
        print("please insert your debit card")
        
        #collect the customer identity
        customerID = int(input("enter your customer ID number"))
        print("\n")
        
        cust_accounts = []
        for i in master_list:
            if customerID == i[1]:
                cust_accounts.append(i[2])
                isCustomer = True
        
        if isCustomer == True:
            isAccountSelected = False
        
            while isAccountSelected == False:
                print('Enter 1 for Checking account')
                print('Enter 2 for Business account')
                account_type = int(input('Enter which account to be chosen:'))
                
                if account_type in cust_accounts:
                    for x in master_list:
                        if account_type == x[2] and customerID == x[1]:
                            ObjectName = x[0]
                            
                    isAccountSessionOn = True
                    
                    while isAccountSessionOn == True:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print( "Press 2 for withdrawals")                    
                        print( "Press 3 to exit.")
                    
                        action_selected = int(input("please select your service:"))
                    
                        if action_selected ==1:
                            ObjectName.display_acc()
                        elif action_selected == 2:                        
                            amount_inputed = float(input("please enter the amount you need"))
                            ObjectName.withdraw(amount_inputed)
                            print('your current balance is %d' % ObjectName.get_amount())
                        elif action_selected == 3:
                            isAccountSessionOn = False
                            print("Thank for using the 24-hour ATM service.")
                            print("Have a pleasant day.")
                            print("\n\n")
                            print("##########################################")
                            isCustomer = False
                else:
                    print("error.You do not have that account")
        else:
            print("sorry,we cannot find your information,please take your card")