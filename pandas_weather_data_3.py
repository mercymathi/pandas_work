#!/usr/bin/env python
# coding: utf-8

# In[2]:


#FILLNAimport pandas as pd

import pandas as pd
wea = pd.read_csv("downloads\weather_data.csv")
wea


# In[4]:


fillna = wea.fillna('no event')
fillna


# In[5]:


#to find mean
wea['windspeed'].mean()


# In[7]:


#sum of no.of.nulls 
wea.isnull().sum()


# In[8]:


wea['temperature'].count()


# In[13]:


#Fillna using column name and dict
new_df = wea.fillna({'temperature':23,'windspeed': 5.0,'event': 'Event not Recorded'})
new_df


# In[14]:


new_df['temperature'].mean()


# In[15]:


#Use method to determine how to fill na values
#forward fill
new_df = wea.fillna(method="ffill")
new_df


# In[20]:


#backward fill
new_df = wea.fillna(method = 'bfill')
new_df


# In[21]:


#limit parameter

new_df = wea.fillna(method="ffill",limit=1)
new_df


# In[22]:


new_df = wea.fillna(method = 'bfill',limit=1)
new_df


# In[23]:


#interpolate
new_df = wea.interpolate()
new_df


# In[25]:


#DROPNA
new_df = wea.dropna()
new_df


# In[27]:


new_df = wea.dropna(how='all')
new_df


# In[29]:


#thresh
new_df = wea.dropna(thresh=3) # thresh=1 is equal to how=all(method)
new_df


# In[30]:


#Inserting Missing Dates

n=pd.date_range('01-02-2022','01-20-2022')
n


# In[36]:


dt=pd.date_range("01-01-2017","01-11-2017")
dt


# In[42]:


wea['day2']=['2017-01-01','2017-01-04',
               '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-08',
               '2017-01-09', '2017-01-10', '2017-01-11']
wea


# In[44]:


#Replacing list with another list
df = pd.DataFrame({'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],'student': ['abhi', 'maya', 'parthiv', 'tom', 'julian', 'erica']})
df


# In[45]:


li=['poor', 'average', 'good','exceptional']
li2=["C","B","A",'A+']
df['score']=df['score'].replace(li,li2)
df


# In[48]:


import numpy as np
df['age']=[10,20,30,40,60,np.nan]
df


# In[49]:


df.replace("abhi","Ravi")


# In[ ]:




