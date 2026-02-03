class Animal:
    def animalinfo(self):
        print("all animal are erritating")
class Dog(Animal):
    def doginfo(self):
        print("all dogs are very loyal")
class Cat(Dog):
    def catinfo(self)  :
        print("all cates are very innocent")  
class Elephant(Cat) :
    def elephantinfo(self):
        print("all elephants are very big ")
class Parrot(Elephant,Cat,Dog,Animal):
    def parrotinfo(self):
        print("parrot sounds is very sweet")
obj = Parrot() 
obj.parrotinfo()
obj1= Parrot()
obj1.animalinfo()
obj2= Parrot()
obj.doginfo()

