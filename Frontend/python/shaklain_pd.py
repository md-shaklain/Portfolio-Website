# import pandas as pd
# lst=[2,3,4,5,6,7,8,9]
# Series= pd.Series(lst)
# print(Series)
# friends=['shaklain','zaid','mujahid','salim']
# s=pd.Series(friends)
# print(s)
# label=pd.Series(friends,index=['a','b','c','d'])
# print(label)
# student=['ashraf','python',10000]
# std_series=pd.Series(student,index=['name','course','fee'])
# print(std_series)

# print(pd.__version__)

# print(df.tail())
# print(df.head())

# print(df.tail(10))
# print(df.head(12))

# # print(df.loc[2:10])
# print(df.loc[2:20:5])


# print(df.shape)
# print(df.describe())

# data={
#     'names':['shaklain','sindhu','zaid','salim'],
#     'course':['python','java','web','react'],
#     'fees':[10000,50000,60000,70000]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.head(2))



# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print(i,end=" ")
#         j+=1
#     print()
#     i+=1    

# i=5
# while(i>=1):
#     j=1
#     while(j<=i):
#         print("*",end="")
#         j+=1
#     print()
#     i-=1    


# i=10
# while(i>=1):
#     print(i)
#     i-=1

# year=int(input("enter year:"))
# if(year%400==0):
#     print("its leap year")
# elif(year%4==0 and year%100!=0):
#     print("its leap year") 
# else:
#     print("its not leap year")       

# for i in range(1,11):
#     print(i)

# sum=0
# for i in range(1,11):
#     sum+=i
# print("sum:", sum)


# i=1
# total=0
# while(i<=10):
#     total+=i
#     i+=1
# print("sum:",total) 

import pandas as pd
df=pd.read_excel('MOCK_DATA.xlsx,excel_sheet=excel')
# print(df)
# print(df.tail(10))
# print(df.head(20))
# print(df.describe())
# print(df[['first_name','id','email']])
# print(df.loc[2:10])
# print(df.info())
# df.drop[9]
# print(df.drop([9]))
# # print(df.head(10))
# df.drop([9],inplace=True)
# print(df.head(10))
# df.drop_duplicates(inplace=True)
# print(df)
# print(df.duplicated())

# print(df.fillna(100))