#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
from predict_cost import predict
import numpy as np
 
st.title('Home price prediction')
 
st.write('---')
 
# no. of bedrooms in the house
bedrooms = st.number_input('No. of bedrooms', min_value=0, step=1)

# total area of the house
m2 = st.number_input('Total area of the house', min_value=30, step=10)

# total area of the lot
lot_m2 = st.number_input('Lot area', min_value=50, step=10)

# total area of the basement
base_m2 = st.number_input('Basement area', min_value=0, step=10)
 
# how old is the house? (age)
age = st.number_input('How old is the house (in years)?', min_value=0, step=1)

# how old is the house renovation? (age_renovated)
age_renov = st.number_input(
    'How old is the house renovation (in years)? If it was enver renovated, write the age of the house', 
    min_value=0, step=1)
 

if st.button('Predict House Price'):
    cost = predict(np.array([[bedrooms, m2, lot_m2, base_m2, age, age_renov]]))
    st.text(cost[0])


# In[ ]:





# In[ ]:




