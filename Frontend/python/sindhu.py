# def sham(a,b):
#     return a+b
# result=sham(10,20)
# print(result)

# def sum(a,b,n):
#     n=int(input("enter your number:"))
#     if(n%2==0):
#         print("it is even number")
#     else:
#         print("its odd number")  
# sum(11,13,15)      

# import math
# def circle():
#     r=5
#     area=3.14*r*r
#     print(area)
# circle()    

# def palendrome(s):
   
#     return s==s[::-1]   
# print(palendrome("madam"))
# print(palendrome("hello"))
    
# def count_vowel(s):
#     vowels = "aeiouAEIOU"
#     count=0
#     for ch in s:
#         if ch in vowels:
#             count+=1
#     return count
# print(count_vowel("hello world"))         































# def count_vowel(s):
#     vowels= "aeiouAEIOU"
#     count=0
#     for ch in s:
#         if ch in vowels:
#             count+=1
#     return count
# print(count_vowel("shaklain ashraf"))
        

# fact=1
# i=1
# while(i<=5):
#     fact*=i
#     i+=1
# print(fact)    



# def palendrome(s):
#     return s==s [::-1]
# print(palendrome("madam"))

# import re

# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$"
# email= "shaklai%+-nashraf2001._@gmail.cm"
# if re.match(pattern,email):
#     print("correct password")
# else:
#     print("invalid password")    




# def Walk(steps):
#     for step in range(1,steps+1):
#         print(f"you take steps {step}")
# Walk(50)        


# def Fact(n):
#     if n == 0 :
#         return 1
#     else:
#         return n * Fact(n-1)
# print(Fact(5))    
    

# def sum():
#     i=1
#     while i<=100:
#         yield i
#         i+=1
# print(sum())   
# x = sum()
# print(next(x))  
# print(next(x)) 
# print(list(x)) 


sum = [2,3,4,6,7]
for i in sum:
    print(i, end=" ") 