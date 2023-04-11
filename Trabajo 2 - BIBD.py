#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install feature_engine


# In[16]:


import pandas as pd
from feature_engine.discretisation import EqualFrequencyDiscretiser, EqualWidthDiscretiser

Covid = pd.read_csv("C:/Users/WINDOWS/Desktop/dataset/Covid_Data.csv")



# Discretización usando EqualFrequencyDiscretiser
efd = EqualFrequencyDiscretiser(q=5, variables=["SEX"])
Covid_efd = efd.fit_transform(Covid)




# Discretización usando EqualWidthDiscretiser
ewd = EqualWidthDiscretiser(bins=5, variables=["SEX"])
Covid_ewd = ewd.fit_transform(Covid)

