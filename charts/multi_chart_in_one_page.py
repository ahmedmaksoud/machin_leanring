# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:36:14 2023

@author: 459
"""




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = ".\\housing.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

###slect some data and get histo on these data where ocean_proximity = NEAR BAY, ...... 4 categories
print ("categories " ,df["ocean_proximity"].value_counts ().index)

# fig 2 * 2 = 4 charts subplots(2, 2)
fig, ax = plt.subplots(2, 2, figsize=(20,10))
# sca where chart located
plt.sca(ax[0,0])
data = df[df["ocean_proximity"] == "NEAR BAY"]["median_income"]
plt.hist(data,bins=50)
plt.title("NEAR BAY")

plt.sca(ax[0,1])
data = df[df["ocean_proximity"] == "INLAND"]["median_income"]
plt.hist(data,bins=50)
plt.title("INLAND")


plt.sca(ax[1,0])
data = df[df["ocean_proximity"] == "<1H OCEAN"]["median_income"]
plt.hist(data,bins=50)
plt.title("<1H OCEAN")

plt.sca(ax[1,1])
data = df[df["ocean_proximity"] == "NEAR OCEAN"]["median_income"]
plt.hist(data,bins=50)
plt.title("NEAR OCEAN")