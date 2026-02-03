# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i+=1    

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i-=1    

# i=1
# while i<=10:
    
#     print(i)
#     i+=1


# i=10
# while i>=1:
#     print(i)
#     i-=1


# year=int(input("enter year:"))
# if(year%400==0):
#     print("it is leap year")

# elif(year%4==0 and year%100!=0):
#     print("its leap year")   
# else:
#     print("its not a leap year")     

# n=int(input("enter your maks:")) 
# if(n&1==0):
#     print("even maks")
# else:
#     print("odd maks")  

sub1=int(input("enter your subject maks:"))
sub2=int(input("enter your subject maks:"))
sub3=int(input("enter your subject maks:"))
sum=sub1 + sub2 + sub3
avg=sum/3
if(sub1>=90 and sub2<=100):
    grade="A"
    print("A")
elif(sub2>=75 and sub3<=90):
    grade="B"
    print("B")
elif(sub3>=60 and sub2<=75):
    grade="C"
    print("C")
elif(sub1>=33 and sub3<=50):
    grade="D"
    print("D")
else:
    print("you are fail:")   
print(sum)
print(avg)     


