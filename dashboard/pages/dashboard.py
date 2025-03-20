import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns

titanic=sns.load_dataset("titanic")

st.title("titanic dataset dashoard")
st.sidebar.header("filter options")
##to display the dataset
st.dataframe(titanic)

##filters

#gender filter
gender=st.sidebar.multiselect('Gender',
                              options=titanic['sex'].unique(),
                              default=titanic['sex'].unique())

##class filter
pclass=st.sidebar.multiselect('Class',
                              options=sorted(titanic['pclass'].unique()),
                              default=sorted(titanic['pclass'].unique()))

##age filter
min_age,max_age=st.sidebar.slider('Age',
                                  min_value=int(titanic['age'].min()),
                                  max_value=int(titanic['age'].max()),
                                  value=(int(titanic['age'].min()),int(titanic['age'].max())))


##filter the dataset based on selections to check connectivity
filtered_data=titanic[
    (titanic['sex'].isin(gender))&
    (titanic['pclass'].isin(pclass))&
    (titanic['age']>=min_age)&
    (titanic['age']<=max_age)
]
st.subheader("Gender Distribution")
gender_count=filtered_data['sex'].value_counts()
fig=px.pie(names=gender_count.index,values=gender_count.values,title="Gender Distribution ")
st.plotly_chart(fig)

##create histogram of Age distribution
st.subheader("Age Distribution")
fig=px.histogram(filtered_data,x='age',nbins=20,title="Age Distribution",
        labels={'age':'Age','count':'Number of Passengers'})
st.plotly_chart(fig)        

