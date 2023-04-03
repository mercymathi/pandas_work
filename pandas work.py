#!/usr/bin/env python
# coding: utf-8

# In[31]:


#creating a dataframe
import pandas as pd
data = pd.DataFrame([['priya',23],['riya',25]],columns=['name','age'],index=[1,2])
print(data) 


# In[32]:


# adding city column to data dataframe
city=['chennai','hyderabad']
data['city']=city
print(data)


# In[35]:


# how to get data through index
data['city'][1]
data.loc[1]['city']


# In[39]:


# adding new row for dataframe
data.loc[3]={'name':'paul','age':28}

data.loc[3]

data.loc[4]={'name':'john','age':32,'city':'bengaluru'}
print(data)


# In[47]:


# select name from data where age < 35;
data['name'][data['age']<35]


# In[45]:


# select name,age from age where age<35;
data[['name','age']][data['age']<35]


# In[46]:


# select * from data where age<35;
data[data['age']<35]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




