# sub1=70
# sub2=80
# sub3=90
# sub4=91
# sub5=95
# if(sub1>90 & sub2<100):
#     grade="A"
#     print("grade A") 
# elif(sub1>70 & sub2<90):
#     grade="B"
#     print("grade B")
# elif(sub1>50 & sub2<70):
#     grade="C"
#     print("grade C") 
# elif(sub1>33 & sub2<50):
#     grade="D"
#     print("grade D") 
# else:
#     print("you are fail")   
# sum=sub1+sub2+sub3+sub4+sub5
# avg=sum/5
# print("sum of five subjects:", sum)
# print("avg of five subjects:",avg)

# rating= int(input("enter your ratings:"))
# if(rating==5):
#     print("Excellent Product:")
# elif(rating==4):
#     print(" VeryGood Product:")
# elif(rating==3):
#     print("Good Product:")
# elif(rating==2):
#     print("poor Product:")
# else:
#     print("your product is waste")    
    
# num=int(input("enter youer value:"))
# if(num%2==0):
#     print("given number is even")
# else:
#     print("given number is odd")        

# a= int(input("enter a value:"))
# b= int(input("enter b value:"))
# c=int(input("enter c value:"))
# if(a>b and a>c):
#     print("a is greatest of three numbers:")   
# elif( b>c):
#     print("b is greatest of three numbers:")   
# else:
#     print("c is greatest of three numbers:")  
    
# year=int(input("enter a year :"))
# if(year%400==0):
#     print("it is a leap year")
# elif(year%4==0 and year%100!=0):
#     print("it is a leap year") 
# else:
#     print("it's not a leap year")    

    
# num=int(input("enter a number :"))  
# if(num & 1==0):
#     print("even number")
# else:
#     print("odd number")    



# numbers=[2,3,4,5,6,7,8]
# for i in numbers:
#    if (i%2==0):
#       print(i)



# i=10
# while(i>=1):
#     print(i)
#     i-=1

# i=1
# while(i<=10):
#     print(i)
#     i+=1

# i=1
# while(i<=5):
#   j=5
#   while(j>=i):
#    print("*",end=" ") 
#    j-=1 
#   print()
#   i+=1


# i=1
# while(i<=5):
#      j=1
#      while(j<=i):
#        print(i, end ="")
#        j+=1
#      print()
   
#      i+=1
    
    
    
    

   
# i=10
# while(i>=1):
#     print(i)
#     i-=1
# i=1
# while(i<=10):
#     print(i)   
#     i+=1 
    
# sum=1
# for i in range(1,11):
#     sum+=i
# print("sum:",sum)   

# i=1
# total=0
# while(i<=10):
#     total+=i
#     i+=1
# print("sum:",total)  
# 
# 
# num=int(input("enter your number:"))  
# fact=1
# i=1
# while(i<=num):
#     fact*=i
#     i+=1
# print("factorial:",fact)    

# num=int(input("enter your number:"))
# fact=1
# for i in range(1, num+1):
#     fact*=i
#     i+=1
# print("factorial:", fact)   
# num=int(input("enter your number:"))
# fact=1
# i=1
# while i<=num:
#     fact*=i
#     i+=1
# print("factoril:",fact)    
# num=int(input("enter your number:"))  
# fact=1
# for i in range(1,num+1):
#     fact*=i
#     i+=1
# print("factoril:",fact)     
# num=int(input("enter your number:")) 
# total=0
# i=1
# while(i<=10):
#     total+=i
#     i+=1
# print("sum:",total)    
# num=int(input("enter your number:")) 
# total=0
# for i in range(1,11):
#    total+=i
#    i+=1
# print("sum:",total)   
# total=0


# for i in range(1,11):
#     total+=i
#     i+=1
# print(total,end="")

i=5
while(i>=1):
    j=1
    while(j<=i):
        j+=1
        print(i,end="")
    print()
    i-=1        