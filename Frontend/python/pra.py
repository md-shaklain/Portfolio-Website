# import numpy as np
# a = np.array([[1,2,3,4,5,]])
# # print(a.ndim)
# # print(a.shape)
# # print(type(a))
# # print(a.size)
# # print(a.dtype)
# b = a .astype('float')
# print(b)
# print(b.dtype)

import pandas as pd
df=pd.read_excel('MOCK_DATA.xlsx',sheet_name='Sheet2')
# print(df)
# print(df.loc[df['name'].str.startwith('a')])
# print(df[['sub1','sub2','sub3']].mean())
# print(df[['sub1','sub2','sub3']].median())
# print(df[['sub1','sub2','sub3']].mode())
# print(df[['sub1','sub2','sub3']].max())

# print(df.query('age>20'))

# df=pd.read_excel('MOCK_DATA.xlsx',sheet_name='Sheet2')
# print(df)
# print(df.query('age>25 and age<33'))

# print(df.query("name=='zaid'"))

# print(df.replace({'gender':{'male':1,'female':0}}))
# print(df.replace({'gender':{1:'male',0:'female'}}))
# print(df.loc[df['name'].str.contains ('a')])
# print(df.loc[df['name'].str.startswith ('a')])
# print(df.loc[df['name'].str.endswith ('a')])

df=pd.read_csv('MOCK_DATA.csv')
# print(df)
# df.to_excel('zaid.xlxs',sheet_name='Sheet2')
df.shape
df.dtypes