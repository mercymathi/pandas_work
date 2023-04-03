#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
wea = pd.read_csv('Downloads\weather_data.csv')
print(wea)


# In[9]:


wea['day'][1]


# In[10]:


type(wea['day'][1])


# In[11]:


#loading csv with date data type

wea_uptd = pd.read_csv('Downloads\weather_data.csv',parse_dates = ['day'])
wea_uptd


# In[12]:


type(wea_uptd['day'][1])


# In[13]:


#converting column to data type

wea['day']=pd.to_datetime(wea['day'])


# In[14]:


wea


# In[15]:


wea['day'][1]


# In[16]:


#dropna
wea.dropna(subset=['event'])


# In[ ]:




