# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:33:55 2023

@author: 459
"""

import pandas as pd
#pip install missingno
import missingno as msno


#path = "C:\\machine_learning\\machin_leanring\\pandas\\test_csv2.csv"
path = ".\\test_csv2.csv"

df = pd.read_csv(path,encoding='cp1252')
print("diamention " ,df.shape)

print("head  is " ,df.head())


print("info type (nulls count)" ,df.info())

print("is null  is NA not avilable" ,df.isna())

print("is null  is NA not avilable" ,df.isna().any())

print("total of null  is NA not avilable" ,df.isna().any().sum())


print("describe>>count  mean std min max " ,df.describe())

#show mising data in graph
msno.matrix(df)

#msno.bar(df)
