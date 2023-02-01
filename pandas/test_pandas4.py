# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:06:05 2023

@author: 459
"""



import pandas as pd


import numpy as np 


#pip install missingno
#import missingno as msno

path = ".\\test_csv2.csv"

df = pd.read_csv(path,encoding='cp1252')

print("header", df.columns)



print("groub by location and get agg max min count std var ", df.groupby('Location')["salary"].agg({'min','max','count','mean','std','var'}))


#create a new column and add values salary * age
df["salary_per_old_year"]=  df["salary"] /  df["age"] 


print("header", df.columns)

print("median is ", df["salary"].median())

print(" 1st quarter  is ", df["salary"].quantile(0.25))

print(" 2ed quarter  is ", df["salary"].quantile(0.5))

print(" 3ed quarter  is ", df["salary"].quantile(0.75))


print(" many quarter  is ", df["salary"].quantile([0.25, 0.5, 0.75]))


print("groub by location - Company  and get mean", df.groupby(['Location', 'Company'])["salary"].mean())

print("groub by location - Company  and get mean", df.groupby(['Location', 'Company'])["salary", "age"].mean())

# mean = NAN if there is no data or one row only