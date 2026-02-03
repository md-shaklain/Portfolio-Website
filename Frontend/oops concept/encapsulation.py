

# example of encapsulation

# class Bank_account():
#     def __init__(self,account_num, balance):
#         self.account_num = account_num
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance += amount
#     def debit(self,amount) :
#         self.__balance -= amount   
#     def get_balance(self) :
#         return self.__balance
#         print(__balance )

# account= Bank_account(123344,5000) 
# account.deposit(1000)
# account.debit(500)
# account.deposit(2000)
# account.debit(3000)
# print(account.get_balance())





class Bank:
    def __init__(self,account_num, balance):
        self._account_number = account_num
        self.__balance= balance
        
        

    def Credit(self,amount) :
        self.__balance+=amount        

    def Debit(self,amount):
        self.__balance-= amount
       

    def get_balance(self):
       return self.__balance

     
obj = Bank(1234567,5000) 
obj. Debit(500)  
obj.Credit(1000)  
print(obj._account_number )
print(obj.get_balance())





               