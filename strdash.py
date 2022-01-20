import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Setting up Subplots

plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('bmh')
fig3 = plt.figure(constrained_layout=True,figsize=(21,11))
gs = fig3.add_gridspec(40,40)

#Markdown text

st.write("""
# Analyzing Boston Housing Dataset
""")

#Plotting using streamlit's 'pyplot' function
df = pd.read_csv("BostonHousing.csv")

st.write("""### 1. Data overview""",df.head())