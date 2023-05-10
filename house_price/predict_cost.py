#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib


# In[2]:


def predict(data):
    lgb = joblib.load('lgb_model.sav')
    return lgb.predict(data) 


# In[ ]:




