#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


#path='C:\\Users\\LENOVO\\Desktop\\NPOWER Materials\\Vancouver resources\\Course 7\\Week 1\GoodBelly-DataSet-Regression.xlsx'

df=pd.read_excel('GoodBelly-DataSet .xlsx')
df.head()



# In[4]:


#Q1 - Give summary of numeric type of columns in dataset?
df.describe()


# In[5]:


#Q2 Calc STD of columns in dataset
std = df.std(numeric_only=True)
print(std)


# In[11]:


#Q3 mean of first 50 records in dataset
mean_f50 = df.head(50).mean(numeric_only=True)
print(mean_f50)


# In[7]:


#Q4 What are thecolumn 
df.columns


# In[8]:


#Q - Number of elements in dataset
df.size


# In[9]:


#Q- No. of records this dataset has
len(df)


# In[10]:


#Q type of column dataset has
df.dtypes


# In[12]:


# 7. What are the mean values of the first 50 records in the dataset? Hint:
# use head() method to subset the first 50 records and then calculate the mean
mean_f50 = df.head(50).mean(numeric_only=True)
print(mean_f50)


# In[ ]:




