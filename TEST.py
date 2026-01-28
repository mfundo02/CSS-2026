# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 11:25:37 2026

@author: mfund
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 11:25:37 2026

@author: mfund
"""
import streamlit as st
import plotly.express as px
import pandas as pd

st.write('CSS 2026')

st.title('Big Title')
st.write('Wassup stl')
st.header('Sample Data')

data = pd.DataFrame({'x':[1,2,3], 'y':[10, 20,30]})
st.write(data)
st.dataframe(data)
fig = px.line(data, x='x', y='y', title = 'Simple PLatly Example')

st.plotly_chart(fig)