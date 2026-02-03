class Car:
    def __init__(self):
        self.accilarator= False
        self.cluch=False
        self.brk=False
    def start(self):
        self.accilarator= True
        self.cluch= True
        self.brk=True
        print("Car Started:") 
car1= Car()
 
print(car1.start())
print(car1.accilarator)
