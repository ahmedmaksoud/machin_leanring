# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:09:01 2023

@author: 459
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = ".\\housing.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

print(df.columns)
# chart size
plt.figure(figsize=(10,6))
plt.hist(df["median_income"], bins=50)
plt.title ("median_income here")
plt.xlabel("median_income")
plt.ylabel("frequancy")

###################slect some data and get histo on these data where ocean_proximity = NEAR BAY get hist to median_income

df[df["ocean_proximity"] == "NEAR BAY"]["median_income"].hist()