import streamlit as st
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

filename = r'D:\APIpractice\APIpractice\prc_git\python\PS-CH-1508data.xlsx'
_df = pd.read_excel(filename)
vislst = _df['Vis']

num = st.sidebar.number_input('Input sample number', min_value=10, max_value=100000)
bins = st.sidebar.number_input('Bins', value=20, min_value=5, max_value=1000)
average = st.sidebar.number_input('Average', value=10000, min_value=7000, max_value=13000)
chk1 = st.sidebar.checkbox('norm1')
chk2 = st.sidebar.checkbox('norm2')
chk3 = st.sidebar.checkbox('norm3')
chk4 = st.sidebar.checkbox('1508')
submit_button = st.sidebar.button('submit')

if submit_button:

    arr1 = stats.norm.rvs(loc=average, scale=300,size=num, random_state=1)
    arr2 = stats.norm.rvs(loc=average, scale=600,size=num, random_state=2)
    arr3 = stats.norm.rvs(loc=average, scale=1000,size=num, random_state=3)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    if chk1:
        ax.hist(arr1, range=(7000,13000), bins=bins, alpha=0.5)
    if chk2:
        ax.hist(arr2, range=(7000,13000), bins=bins, color='red', alpha=0.5)
    if chk3:
        ax.hist(arr3, range=(7000,13000), bins=bins, color='green', alpha=0.5)
    if chk4:
        ax.hist(vislst, range=(7000,13000), bins=bins, color='blue', alpha=0.5)
    fig.set_size_inches(3,2)
    st.pyplot(fig, use_container_width=False)
