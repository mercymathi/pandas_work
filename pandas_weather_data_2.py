#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
wea = pd.read_csv("downloads\weather_data.csv")
wea


# In[5]:


wea.min()


# In[6]:


wea.max()


# In[8]:


# select day from weather_data where temperature = (select max(temperature) from weather_data)

wea['day'][wea['temperature']==wea['temperature'].max()]


# In[12]:


# select day from weather_data where temperature = (select max(temperature) from weather_data

wea[['day']][wea['temperature']==wea['temperature'].max()]

wea[['day']][wea['windspeed']==wea['windspeed'].max()]


# In[13]:


wea


# In[16]:


wea['day']


# In[17]:


wea['temperature']


# In[18]:


wea['windspeed']


# In[19]:


wea['event']


# In[21]:


wea.loc[0]


# In[22]:


wea.loc[1]


# In[23]:


wea.loc[2]


# In[24]:


wea.loc[3]


# In[25]:


wea.loc[4]


# In[26]:


wea['temperature'][5]


# In[27]:


wea.loc[5]['temperature']


# In[46]:


import pandas as pd
wea = pd.read_csv("downloads\weather_data.csv")
wea

#set index
#wea.set_index(keys='day',inplace=True)
#wea


# In[51]:


# select * from weather data (wea) where temperature=select max(temperature) from weather data (wea))
wea[wea['temperature']==wea['temperature'].max()]


# In[48]:


wea


# In[49]:


wea.shape


# In[58]:


#select day,windspeed from whe where windspeed=(select max(windspeed) from whe)
wea['windspeed'][wea['windspeed']==wea['windspeed'].max()]


# In[56]:


#select * from whe where event='Sunny'
wea[wea['event']=='Sunny']


# In[59]:


#select day,event from whe where event='Sunny'
wea[['day','event']][wea['event']=='Sunny']


# In[ ]:




