# def sum():
#     r=5
#     area= 3.14 *r*r
#     print(area)
# sum()


# def palindrome(s):
#     return s== s[::-1]
# print(palindrome("madam"))


# def count_vowel(s):
#     count=0
#     vowels= "aeiouAEIOU"
#     for ch in s:
#         if ch in vowels:
#             count+=1
#     return count
# print(count_vowel("i am from fortune it"))            

# def factorial():

#  fact=1
#  i=1
#  while(i<=5):
#     fact*=i
#     i+=1
#  print(fact)
# factorial() 
 
# lst =[2,3,4,6,7,8,8,9]
# lst.reverse()
# print(lst)

# def square(n):
#     return n**2
# numbers= [2,3,5,7,8,6,8]
# square_number = list(map(square,numbers))
# print(square_number)



# lst=[2,3,4,5,6,7,8,9]
# square_numbers= list(map(lambda x: x**2,lst))
# print(square_numbers)   

# lst=[2,3,4,5,6,7,8,9]
# even_number = list(filter(lambda x: x%2==0, lst))
# print(even_number)



    
# lst= [ 2,3,4,5,7,8,9]

# square_numbers= list(map(lambda x: x**2,lst))
# print(square_numbers)

# lst= [ 2,3,4,5,7,8,9]
# even_numbers =list(filter(lambda x: x%2==0,lst))
# print(even_numbers)

lst= [ 2,3,4,5,7,8,9]
square_root=list(map(lambda x: x**2,lst))
print(square_root)