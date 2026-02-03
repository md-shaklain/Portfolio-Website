from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def rate_of_intrest(self):
        pass
class SBI(Bank) :
    def rate_of_intrest(self):
        print("sbi rate of intrest 6%")
class HDFC(Bank) :
    def rate_of_intrest(self):
        print("hdfc rate of intrest 7%")  
class ICICI(Bank) :
    def rateofintrest(self):
        print("rate of intrest 8%")   

sbi= ICICI()  
sbi.rateofintrest()  

# sbi1 = HDFC()
# sbi1.rate_of_intrest()
# sbi2= SBI()
# sbi2.rate_of_intrest()