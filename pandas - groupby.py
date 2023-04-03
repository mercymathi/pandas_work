#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv("Downloads\math result.csv")
df


# In[6]:


df.describe()


# In[10]:


d=df.head(10)
d


# In[11]:


#1 Split the specified dataframe into groups based on school code

re = d.groupby(['Grade'])
for year,group in re:
    print("\ngroup ")
    print(year)
    print(group)


# In[18]:


#2 Split the specified dataframe by year and get mean, min, and max value of grade for each 
g=d.groupby('Year')
g['Grade'].mean()


# In[19]:


g['Grade'].min()


# In[20]:


print(d.groupby('Year').agg({'Grade':['mean','min','max']}))


# In[21]:


#3 Split the specified given dataframe into groups based on Year and Grade
g=d.groupby(['Year','Grade'])
for year,group in g:
    print('\nGroup')
    print(year)
    print(group)


# In[22]:


#4 Split the specified given dataframe into groups based on Grade and cast grouping as a list
g=d.groupby(['Grade'])
temp=list(g)
temp


# In[30]:


#5 Split the specified given dataframe into groups based on single column and multiple columns and find the size of the grouped data
g1=d.groupby(['Year'])
g1.size()


# In[32]:


g2=d.groupby(['Mean Scale Score','Demographic'])
g2.size()


# In[33]:


#6 Split the specified given dataframe into groups based on Demographic and call a specific group with the name of the group
g=d.groupby(['Demographic'])
g.get_group('Female')


# In[35]:


# Second Set Group
import pandas as pd
df=pd.read_csv("Downloads\math result.csv",index_col=0)
df.head(10)


# In[44]:


#7 Split a dataset, group by one column and get mean, min, and max values by group
x=df.head(10)
x
x.groupby('Year').agg({'Mean Scale Score':['mean','min','max','sum']})


# In[45]:


#8 Split a dataset to group by two columns and count by each row
r = x.groupby(['Year','Mean Scale Score']).size().reset_index().groupby(['Year','Mean Scale Score'])[[0]].max()
x.groupby(['Year','Mean Scale Score']).size().reset_index().groupby(['Year','Mean Scale Score'])[[0]].max()


# In[46]:


r


# In[ ]:




