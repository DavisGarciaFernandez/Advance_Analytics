#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import pandas_profiling as pp

Covid = pd.read_csv("C:/Users/WINDOWS/Desktop/dataset/Covid_Data.csv")


# In[5]:


profile = pp.ProfileReport(Covid)

profile.to_file("Covid_profile.html")

