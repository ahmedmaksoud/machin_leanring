# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:22:34 2023

@author: 459
"""


import pandas as pd


import numpy as np 

import time



#pip install missingno
import missingno as msno

path = ".\\test_csv3.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

print("header", df.columns)
print("header", df.info())
##check null graph
#msno.matrix(df)
#msno.bar(df)

print("is not avilable", df.isna())

print("is not avilable vertical better ", df.isna().any())
print("is not avilable sum vertical better ", df.isna().sum())
#show nulls in bar 
df.isna().sum().plot(kind="bar")

print( "null values  " , df[df["age"].isna()])
##export file csv
df[df["age"].isna()].to_csv("ss.csv")



