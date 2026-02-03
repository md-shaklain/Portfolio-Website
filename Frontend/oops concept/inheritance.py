

#  example of inheritence

# class Animal():
#     def sounds(self):
#         print("animal make sounds always")
# class Dog(Animal) :
#     def bark(self):
#         print("dogs make sounds bhow bhow") 
# cat = Dog()
# cat.sounds()
# cat.bark ()        














class Car:
    color="black"
    def start(self):
        print("Car started:")
    def stop(self):
        print("Car  stopedd:")  
class BMW(Car):
    def __init__ (self,name):
        self.name = name   
model1 =  BMW("Fortuner") 
model2 =  BMW("Volvo")   
print(model1.name) 
print(model2.name)    
print (model1.start()) 
print(model2.color)  
print(model1.stop())