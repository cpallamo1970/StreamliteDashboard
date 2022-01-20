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

st.write("""### 2. *Data Distributions* and *Pairwise Correlations*""")

#The following methods for defining 'fig' also work for the pyplot function
#fig, ax = plt.subplots()
#fig = plt.figure()

fig3.add_subplot(gs[0:19,0:20])
plt.hist(df['rm'],range=(0,10),bins=16,alpha=0.8)
plt.xlabel('num rooms',fontsize=25)
plt.title('Avg num of rooms per dwelling',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

fig3.add_subplot(gs[21:,0:20])
plt.hist(df['lstat'],range=(0,20),bins=16,alpha=0.8,color='brown')
plt.title('% lower status of the population',fontsize=25)
plt.xlabel('% population',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

fig3.add_subplot(gs[0:19,20:])
plt.scatter(df['tax'],df['medv'],alpha=0.8)
plt.title('Full-value property-tax rate per $10,000 \nvs \nMedian value of owner-occupied homes in $1000s',fontsize=20)
#plt.xlabel('full-value property-tax rate per $10,000',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

fig3.add_subplot(gs[21:,20:])
plt.scatter(df['age'],df['medv'],alpha=0.8,color='brown')
plt.title('Proportion of owner-occupied units built prior to 1940 \nvs \nMedian value of owner-occupied homes in $1000s',fontsize=20)
#plt.xlabel('full-value property-tax rate per $10,000',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

st.pyplot(fig3)
