# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 19:40:16 2023

@author: 459
"""


import pandas as pd


import numpy as np 


#pip install missingno
#import missingno as msno

path = ".\\test_csv2.csv"

df = pd.read_csv(path,encoding='cp1252')

print("header", df.columns)

print("unique = groub values in column ", df["Location"].unique)
print("unique values in column with count", df['Location'].value_counts())

cc = df['Location'] ==  ' Maadi'
print("select  where location =  Maadi" , cc)

print("select all data where location =  Maadi" ,( df[ df["Location"] == ' Maadi']))

print("select all data where location =  Maadi & slaly > 2000" ,(df[( df["Location"] == ' Maadi') & ( df["salary"] > 2000 )]))

print("select all data where location =  Maadi or slaly > 2000" ,(df[( df["Location"] == ' Maadi')  | ( df["salary"] > 2000 )]))

print("select all data where in  Maadi & slaly > 2000" ,(df[ df["Location"].isin([' Maadi',' Dokki']) ]))



maadiAndDoki = df[ df["Location"].isin([' Maadi',' Dokki']) ].values

inMaadiOrDoki = df[ df["Location"].isin([' Maadi',' Dokki']) ].values

#np.allclose(maadiAndDoki, inMaadiOrDoki)

meanSalaryMaadi = df[ df["Location"] ==  ' Maadi'] ["salary"].mean()

print("mean Salary Maadi", meanSalaryMaadi)


print("groub by location and get salary mean for every groub", df.groupby('Location')["salary"].mean())

print("groub by location and get salary count for every groub ", df.groupby('Location')["salary"].count())

print("groub by location and get salary std for every groub ", df.groupby('Location')["salary"].std())

print("groub by location and get salary variance for every groub ", df.groupby('Location')["salary"].var())
