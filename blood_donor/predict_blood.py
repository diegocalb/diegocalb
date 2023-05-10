#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib


# In[2]:


def predict(data):
    lr = joblib.load('lr_model.sav')
    return lr.predict(data) 


# In[ ]:




