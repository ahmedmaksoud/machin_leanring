# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:18:38 2023

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
# ocean_proximity category

print ("key val ocean_proximity category + count" , df["ocean_proximity"].value_counts ())
print ("val ocean_proximity count  " , df["ocean_proximity"].value_counts ().values)
print ("val ocean_proximity  category " , df["ocean_proximity"].value_counts ().index)

# x = ocean_proximity val + y h height values
plt.bar(x= df["ocean_proximity"].value_counts ().index, height= df["ocean_proximity"].value_counts ().values)
plt.title ("ocean_proximity  here")
plt.xlabel("ocean_proximity")
plt.ylabel("count")