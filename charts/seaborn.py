# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 21:31:10 2023

@author: 459
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

path = ".\\housing.csv"
#df data frame
df = pd.read_csv(path,encoding='cp1252')

df_tips = sns.lo