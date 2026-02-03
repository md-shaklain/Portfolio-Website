# def cube(x):
#     return x*x*x
# # print(cube(2))


# l = [2,4,6,8,9]
# new = list(map(cube,l))
# print(new)



# def double(x):
#     return x*x
# print(double(2))



# cube= lambda x : x*x*x
# print(cube(3))

# avg = lambda x,y,z: (x+y+z)/3
# print(avg(4,5,6))


# lst = [2,4,6,8,4,6,8,7,5,3]
# def div(n):
#    return n%2==0

# new = list(filter(div, lst))
# print(new)

# lst = [2,4,6,8,4,6,8,7,5,3]
# new = list(map(lambda x: x*x*x, lst))
# print(new)
   
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op= input("enter your operator")

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)


# def square(x):
#     return x * x

# n = square(4)
# print(n)


# n= [1,2,3,4,5,6,2,4,5]
# unique = list(set(n))
# print(unique)

# n= [1,2,3,4,5,6,2,4,5]
# unique=[]
# for ch in n:
#     if ch not in unique:
#         unique.append(n)
# print(unique)



# s = 'shaklainshaklain'
# result= ""
# for ch in s:
#     if ch not in result:
#         result += ch
# print(result)         

# s = ['sindhu', 'shaklain']
# result = '' .join(s)
# print(result)

# s = "shaklain shaklain"
# result = s.split(" ")
# print(result)



# num= [1,2,3,4,6,7,8,9,7,8,5,8]
# even = []
# odd = []

# for n in num:
#     if n % 2==0:
#         even.append(n)
#     else:
#         odd.append(n) 
# print(even)           
# print(odd)  

# shak =list(set(num))
# print(shak)

# a= 5
# b= 10
# temp=a
# a=b
# b=temp
# print(a)
# print(b)


# a = 5
# b = 10
# a = a+b
# b = a-b
# a = a-b
# print(a)
# print(b)


a= 5
b= 10

a ,b = b, a
print(a)
print(b)