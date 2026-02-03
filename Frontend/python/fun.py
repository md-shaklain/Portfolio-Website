# def ash(a,b,):
#     result = a+b
#     print("sum of total:", result)

# ash(10,20)


# def sum(a,b):
#     return a+b
# result= sum(10,30)
# print(result)

# def my_fahrenheit(celsius):
#      fahrenheit = (celsius * 9/5) +32
#      return fahrenheit
# temp=my_fahrenheit(25)
# print(temp,type(temp))

#  def calculator(a,b,operator):
#     if operator=='+':
#     return a+b


# a= int(input("enter the first numebr:"))
# b=int(input("enter the second numebr:"))
# c=int(input("enter the third numebr:"))
# if(a>b & a>c):
#     print("a is greater all these number")
# elif(b>c):
#     print("b is greater all these number") 
# else:
#     print("c is greate all these number")       


# rating= int(input("enter the ratings:"))
# if(rating==4.5):
#     print("excelent product")
# elif(rating==4):
#     print("very good product")   
# elif(rating==3):
#     print("good product")  
# else:
#     print("poor product")       


# n=int(input("enter the value:"))
# if(n%2==0):
#     print("given number is even")
# else:
#     print("given numebr is odd")    



# i=1
# while i<=5:
#    j=1
#    while j<=i:
#        print("*", end="") 
#        j+=1
#    print()
#    i+=1  

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(i,end="")
#         j-=1
#     print()
#     i+=1    

import pandas as pd
lst=[2,3,4,5,6,7,8,9,10]
Series=pd.Series(lst)
print(Series)
# label=['shaklain','zaid','salim','ashraf']
# s=pd.Series(label)
# print(s)
# shaklain=pd.Series(label,index=['a','b','c','d'])
# print(shaklain)

ashraf=['ashrafi','python',70000]
std_series=pd.Series(ashraf,index=['name','course','fee'])
print(std_series)