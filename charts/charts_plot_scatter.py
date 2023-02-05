# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:32:25 2023

@author: 459
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = ".\\housing.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

print(df.columns)

# default values x y
#plt.scatter(df["longitude"], df["latitude"])
# modify size height and width 6 10
plt.figure(figsize=(10,6))
plt.scatter(x= df["longitude"], y= df["latitude"])
#alpha transpanncy 
plt.scatter(x= df["longitude"], y= df["latitude"], alpha=0.5)

plt.title("Housing scattet longitude  and latitude", fontsize=18, color="red")
plt.xlabel("Longitude",color="red")
plt.ylabel("Lsatitude", color="yellow")

##################### add new feature population  s  legend + and median_house_value c in right side color  #################


plt.scatter(x= df["longitude"], y= df["latitude"])
#alpha transpanncy 
#plt.scatter(x= df["longitude"], y= df["latitude"], alpha=1, s=df["population"])
# divide population on 100 as the valus is hige and it is the same percentge
# palet coalr jet is colors
sc = plt.scatter(x= df["longitude"], y= df["latitude"], alpha=1,
            s=df["population"]/100, c=df["median_house_value"]
            ,cmap=plt.get_cmap("jet"), label="legend is population")

# add palet right side represents median_house_value > house price
plt.colorbar(sc)
# show legened
plt.legend()
plt.title("Housing scattet longitude  and latitude", fontsize=18, color="red")
plt.xlabel("Longitude",color="red")
plt.ylabel("Lsatitude", color="yellow")

####################3 i can do it fron df direct

df.plot(kind="scatter", x="longitude", y="latitude",figsize=(8,6),  label="population", 
        c= "median_house_value" , s=df["population"]/100 , cmap=plt.get_cmap("jet"))