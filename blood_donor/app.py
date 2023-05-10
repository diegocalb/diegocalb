#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from predict_blood import predict
import numpy as np
 
st.title('Blood donor prediction')
 
st.write('---')

alb = st.number_input('Albumin (15 - 85)')
alk = st.number_input('Alkaline phosphatase (10-400)')
ala = st.number_input('Alanine Transaminase (1-300)')
asp = st.number_input('Aspartate Transaminase (10-300)')
bil = st.number_input('Bilirubin (1-200)')
che = st.number_input('Acetylcholinesterase (1-15)')
chol = st.number_input('Cholesterol (1-10)')
crea = st.number_input('Creatinin (5-1100)')
ggt = st.number_input('GGT (5-700)')
prot = st.number_input('Proteins (45-90)')




if st.button('Predict Donor Category'):
    cost = predict(np.array([[alb, alk, ala, asp, bil, che, chol, crea, ggt, prot]]))
    if cost == 0:
        st.subheader ('Donor')
    elif cost == 1:
        st.subheader ('suspect Donor')
    elif cost == 2:
        st.subheader ('Hepatitis')
    elif cost == 3:
        st.subheader ('Fibrosis')
    else:
        st.subheader('Cirrhosis')

#    st.text(cost[0])


# In[ ]:


# In[ ]:




