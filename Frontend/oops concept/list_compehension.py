# list = [1,2,4,5,7,9,6,3]
# squares =[x*x for x in list]
# print(squares)



# i=5
# while(i>=1):
#     j=1
#     while(j<=i):
#         print(i,end=" ")
#         j+=1
#     print()  
#     i-=1  


# i=5
# while(i>=1):
#     j=1
#     while(j<=i):
#         print("*",end=" ")
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
# #     i+=1   

# year = int(input("enter a year:"))

# if year%400==0:
#     print("this is leap year")
# elif year%4==0 and year%100!=0:
#     print("this is leap year")  
# else:
#     print("it is not a leap year")      


# def palindrome():
#     s = input("enter your text:")
#     return s == s[::-1]
#     print(s)
# palindrome("madam")    

# def count_vowel(s):
#     vowels ="aeiouAEIOU"
#     count=0
#     for ch in s:
#         if ch in vowels:
#             count+=1
#     return count
# print(count_vowel("shaklainashraf"))        


def count_vowel(s):
    vowels = "aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
print(count_vowel("helloworld"))    