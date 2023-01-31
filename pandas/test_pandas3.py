# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:40:16 2023

@author: 459
"""


import pandas as pd
#pip install missingno
import missingno as msno

path = ".\\test_csv2.csv"

df = pd.read_csv(path,encoding='cp1252')

print("header", df.columns)

print("unique = groub values in column ", df["Location"].unique)
print("unique values in column with count", df['Location'].value_counts())

cc = df['Location'] ==  ' Maadi'
print("select  where location =  Maadi" , cc)

print("select all data where location =  Maadi" ,( df[ df["Location"] == ' Maadi']))



