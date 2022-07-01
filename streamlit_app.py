import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.title("""Home Credit Default Risk""")
st.write("""BrainStation Data Science Program Capstone Project""")
st.write("""Author: Yue Gao""")
st.write("""Email: yue.gao1@outlook.com\n""")
st.image("""https://gadgetstouse.com/wp-content/uploads/2016/06/2-logo.jpg""", width=500)
st.header("""Introduction""")
st.header("""Exploratory Data Analysis""")
st.subheader("""#1.Missing Values Imputation""")
st.subheader("""Numerical Missing Values Imputation""")
st.write("""The numeric missing values are imputed using the mean of the column.""")
st.subheader("""Categorical Missing Values Imputation""")
st.write("""The categorical missing values are imputed using the most common value of the column.""")
st.subheader("""Data Visualization""")
st.subheader("""Application table""")
application = pd.read_csv("https://media.githubusercontent.com/media/yybrother989/HomeCreditDefaultRisk/main/application_train.csv")
st.write(application.head())


fig1 = plt.figure(figsize=(10, 10))
sns.histplot(x='TARGET', hue='TARGET', data=application, kde=False)
plt.title('Target variable distribution')
st.pyplot(fig1)


fig2=plt.figure(figsize=(10, 10))
sns.catplot(data=application,x='NAME_INCOME_TYPE',y='AMT_INCOME_TOTAL'
            ,hue='TARGET',kind='bar')
plt.xticks(rotation=45)
plt.title('Income Type VS. Amount of Total Income')
st.pyplot(fig2)


st.subheader("""Bureau table""")
st.subheader("""Previous Applications table""")
st.header("""Feature Engineering""")
st.header("""Model Building""")
st.subheader("""Base Model -- Decision Tree""")
st.subheader("""Bagging Model -- Random Forest""")
st.subheader("""Boosting Model -- XGBoost""")
st.subheader("""Final Model -- LightGBM""")
st.header("""Credit Fast Approval Application""")







