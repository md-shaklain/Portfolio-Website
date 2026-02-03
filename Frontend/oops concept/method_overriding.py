# class Parent:
#     def show(self):
#         print("this is parent class")
# class Child (Parent):
#     def show(self):
#         super().show()
#         print("this is child class") 
        

# obj = Child() 
# obj.show()        
                                                                                                





class Animal:
    def sound(self):
        print("Animal make sounds")
class Dog(Animal):
    def sound (self):
        super().sound()
        print("dog barks") 
obj= Dog()             
obj.sound()
