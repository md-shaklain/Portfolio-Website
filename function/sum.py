# def sumtwo(a,b):
#     print(a+b)
# sumtwo(12,13)    



# def calculate_avg(a,b,c):
#     sum= a+b+c
#     avg= sum/3

#     print(avg)
#     return avg
# calculate_avg(10,20,30)  
# calculate_avg(90,80,70)  




# n = int(input("enter your value:-"))
# sum=0
# order= len(str(n))
# copy_n=n
# while(n>0):
#     digit=n%10
#     sum+=digit**order
#     n=n//10
# if(sum==copy_n)  :
#     print(f"{copy_n} is a armstrong number") 
# else:
#     print(f"{copy_n} this is not a armstrong number")     


n = int(input("enter your number:-"))
a=0
b=1
count=0
while(count<n):
    print(a , end=" ")
    c= a+b
    a=b
    b=c
    count+=1
    

