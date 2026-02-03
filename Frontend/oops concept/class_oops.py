# class student:
#     name="shaklain"
#     course= "python"
#     fee = 20000
#     def __init__(self,fullname):
#         self.name = fullname
        
# s1 =student("karan")
# s1 = print(s1.name)   
# # print(s1.name) 
# # print(s1.course) 
# # print(s1.fee) 
# s2= student("shaklain ashraf")
# print(s2.name)



# using constructor function

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# s1= Student("shaklain", 90) 
# s2= Student ("ashraf",99) 
# print(s1.name,s1.marks)
# print(s2.name,s2.marks)     








# class Student:
#     def __init__(self,name, marks):
#         self.name=name
#         self.marks=marks

#     def avg(self) :
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hii",self.name,"your avg marks is:", sum/3)
# s1= Student("shaklain",[90,80,70])
# s1.avg()        

    
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "was credited")
#         print("Total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance
# acc1 = Account(10000, 12345)

# # Method calls
# acc1.credit(1000)
# acc1.debit(500)
# acc1.credit(2000)
























# class Car:
#     def show_info(self,name,color,model):
#         self.name= name
#         self.color= color
#         self.model= model
# car1 = Car()
# car1.show_info('Tesla','green',2025) 
# print(car1.name)  
# print(car1.color)
# print(car1.model)     



















# class House:
#     def house_info(self,color,size,light,wire):
#         self.color= color
#         self.size= size
#         self.light=light
#         self.wire= wire
#     def saman (self,material) :
#         self.material= material
# house = House() 
# house.house_info('Green','400*1000','noor','hitachi') 
# house.saman('sandas')
# print(house.color)
# print(house.size)  
# print(house.light)
# print(house.wire) 
# print(house.material)     

# house2= House()
# house2.house_info('yellow',5000,'angel','hitachi2')
# house2.saman('soul')
# print(house2.color)
# print(house2.size)  
# print(house2.light)
# print(house2.wire) 
# print(house2.material)     



# with constructor
# class Car:
#     def __init__(self,color,model,brand):
#         self.color=color
#         # print(color)...
#         # print(model)
#         self.brand=brand
#         # print(brand)
# car1 = Car('black',2025,'bmw')
# print(car1.color)
# print(car1.model)
# print(car1.brand)
        

# constructor with default values
# class shak:
#     def __init__(self,name="unknown",age=0):
#         self.name=name
#         self.age=age
# shak2=shak()
# print(shak2.name)  
# print(shak2.age)      











































