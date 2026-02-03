# class Animal:
#     def speak(self):
#         print("Animal make sounds always")
        
# class Dog(Animal):
#     def bark(self) :
#         print("dog barks") 

# d=Dog()
# d.speak()
# d.bark()



# class Animal:
#     def __init__(self,name,color):
#         self.name= name
#         self.color=color
#         print("animal name is ",name,"color is ",color)
# class Cat:
#     def __init__(self,name, bried):
#         self.name=name
#         self.bried=bried
#         print("cat name is ",name,"cat bried is",bried)
# obj= Cat('wajiha','percian')
# obj1 = Animal('Gautam','green')        
                
# class Bank:
#     def __init__(self,account_no,balance):
#         self.account_no=account_no
#         self.__balance=balance
#         # print(self.__balance) 

#     def Credit(self,amount) :
#         self.__balance+=amount

#     def Debit(self,amount) :
#         self.__balance-=amount

#     def get_balance(self):
#         return self.__balance

# obj = Bank(123344,6000) 
# obj.Credit(5000)
# obj.Debit(1000)  
# print(obj.get_balance())
# # print(obj.account_no) 
        

class Bank:
    def __init__(self,account_no,balance):
        self.__balance= balance
        self.account_no= account_no

    def Credit(self,amount):
        self.__balance+= amount

    def Debit(self,amount):
        self.__balance-= amount

    def get_balance(self):
        return self.__balance

bank1= Bank(1343,6000) 
bank1.Credit(500) 
bank1.Debit(1000)  
print(bank1.get_balance())

                        