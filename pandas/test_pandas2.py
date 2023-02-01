# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:04:13 2023

@author: 459
"""



import pandas as pd
#pip install missingno
import missingno as msno

path = ".\\test_csv2.csv"

df = pd.read_csv(path,encoding='cp1252')

print("names of columns ", df.columns)

#print("vlaues ", df.values)

print("indes ", df.index)

print("salary colmn sub set part of dataset called series ", df.salary)

print("salary colmn too ", df["salary"])

print("id and salary colmn too ", df[["id", "salary"]])

print("sort  ", df.sort_values(by="salary"))
#inplace > replace object passing by refrnce to avoid a = a + "sss"
print("sort  ", df.sort_values(by="salary", axis=0, ascending=False))


print("sort by tow columns  ", df.sort_values(by=["salary", "age"]))