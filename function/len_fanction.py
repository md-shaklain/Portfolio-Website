# cities = ["Hyderabad","delhi","chennai","mumbai","bhopal","indore","raipur"]
# name = ["shaklain","kashif","salim","zaid","owais"]

# def shak(list):
#     print(len(list))
   
# shak(cities) 
# shak(name)   



# cities = ["Hyderabad","delhi","chennai","mumbai","bhopal","indore","raipur"]
# name = ["shaklain","kashif","salim","zaid","owais"]
# def shak(list):
#     for item in list:
#         print(item, end= " ")
# shak(cities)        

# n = int(input("enter your number:"))
# i=1
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print("factorial",fact) 



# n=5
# fact=1
# for x in range(1, n+1):
#     fact*=x
# print("factorial :", fact)    

# for x in range(1,11):
#     print(x)

# n = int (input("enter 10 natural number"))
# count= n
# total=0
# while count:
#     total+=count
#     count-=1
# print("the sum of first natural number is ", total)    

# def palindrome(s):
#     s= input("enter your text:")


#     return s == s[::-1]
# print(s)
# palindrome("madam")    
   

# i=1
# while(i<=10):
#     print(i*2)
#     i+=1
    

# n=153
# sum=0
# copy_n=n
# order=len(str(n))
# while(n>0):
#     digit= n%10
#     sum+=digit**order
#     n=n//10
# if(sum==copy_n) :
#     print(f"{copy_n} is armstrong number")   

# else:
#     print(f"{copy_n} is not a armstrong number")   





# n=153
# sum=0
# order= len(str(n))
# copy_n=n
# while(n>0):
#     digit=n%10
#     sum+= digit**order
#     n=n//10
# if (sum==copy_n) :
#     print("this is a armstrong number")
# else:
#     ("not armstrong number")       

# n = int(input("enter your value here:-"))
# a=0
# b=1
# count=0
# while(count<n):
#     print(a, end=" ")
#     c = a+b
#     a=b
#     b=c
#     count+=1

# n = int(input("enter your value here:-"))
# a=0
# b=1
# for i in range(n):
#     print(a, end=" ")
#     c =a+b
#     a=b
#     b=c



# i=5
# while(i>=1):
#     j=1
#     while(j<=i):
#         print(i, end=" ")
#         j+=1
#     print()    
#     i-=1

# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print("*", end=" ")
#         j+=1
#     print() 
#     i+=1   

s = input("enter a string:-").lower()
vowel = "aeiou"
count=0
i=0
while(i<len(s)):
    if s[i] in vowel:
        count+=1
    i+=1
print(count)         