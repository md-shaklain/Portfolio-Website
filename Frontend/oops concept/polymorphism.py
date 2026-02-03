# exaple of polymorphism
# class bird:
#     def sound(self):
#         print("always birds make sounds")
# class crow(bird) :
#     def sound(self):
#         print("crow sounds cow cow") 
# class parrot(bird) :
#     def sound(self) :
#         print("parrot make sounds sow sow ")    
# bird1= crow()  
# bird2= parrot()
# bird1.sound()
# bird2.sound()


# class BMW:
#     def fuel_info(self):
#         print("its a petrol vehical")
#     def gear_info(self):
#         print("bmw have a 5 gear") 
# class Audi:
#     def fuel_info(self):
#         print("its a diesel car")    
#     def gear_info(self):
#         print("audi have a 6 gear")  
# class Ferrori:
#     def fuel_info(self) :
#         print("this is a diesel car") 
#     def gear_info(self) :
#         print("ferrori have a 6 gear" )  

# car = Ferrori()
# car.fuel_info()
# car.gear_info()
# car1 = BMW()
# car1.fuel_info()
# car1.gear_info()




# class Grandfather:
#     def feeling(self):
#         print("grandfather have a good feelings")
# class Father:
#     def feelings(self) :
#         print("father have a good feelings")
# class Son:
#     def feelings(self) :
#         print("son have a bad feelings") 
# m= Son() 
# m.feelings()
# s= Father()
# s.feelings() 
# k= Grandfather() 
# k.feeling()                  





class Vehical:
    def type(self):
        print(" all vehical is type of petrol")
class Car:
    def type(self):  
        print("all car is electric") 
class bike:
    def type(self):
        print("all bike is petrol type")     
class Truck:
    def type(self):
        print("all truck is Diegel")

obj = Truck()
obj.type()
obj1 = bike()
obj1.type()
obj2 = Car()
obj2.type()
obj3 = Vehical()
obj.type()





