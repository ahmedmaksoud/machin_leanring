# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:55:02 2023

@author: 459
"""

import pandas as pd



import numpy as np 

import time



#pip install missingno
#import missingno as msno

path = ".\\test_csv_drop.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

#drop column
#df = df.drop(columns=["Customer Service Agent", "Company"])

#print(" header " , df.columns)
print( "null values  " , df["age"].isna())


df["age"].isna()

print("df info after  drop " ,df.info())

# drop null rows based on column
df = df.dropna(subset= ["age"], axis= 0)
print("df info after  drop " ,df.info())

