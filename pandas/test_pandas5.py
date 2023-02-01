# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:43:14 2023

@author: 459
"""




import pandas as pd


import numpy as np 

import time


#pip install missingno
#import missingno as msno

path = ".\\test_csv2.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

print("header", df.columns)

print(" 1st quarter  is ", df[["age","salary"]])

##pd loc get by column name and rows df[row, column1, column2

print(" loc ", df.loc[:,['age' ,'salary']])

print(" tail last 5 ", df.tail())

##pd loc get by column index number slice rows df[row, column1, column2
print(" iloc all rows and first column", df.iloc[:,1])
print(" iloc all rows and 0 to 3 column" , df.iloc[:,0:3])
t1 = time.time()
df.groupby('Location')["salary"].agg({'min','max','count','mean','std','var'})
t2 = time.time()
print ("time1" , (t2 - t1))
#make indwx to make search faster

indexDF  = df.set_index('Location')
#print("headerrrrrrrrrrrrrrrr", indexDF.columns)
t1 = time.time()
#print("groub by location and get agg max min count std var ", df.groupby('Location')["salary"].agg({'min','max','count','mean','std','var'}))

indexDF.groupby('Location')['salary'].agg({'min','max','count','mean','std','var'})
t2 = time.time()
print ("time2" , (t2 - t1))
# we can use povit table the same as group by  [index = group by , values = column to be calculated , aggfunc on values = mean, total var ..... ]
indexDF.pivot_table(index= ['Location', 'Company'], values= "salary", aggfunc=["min", "max", "mean", "var"])
 #histogram
df['salary'].hist(bins= 500)




