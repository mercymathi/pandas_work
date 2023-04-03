#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
first_series = pd.Series(list("11111"))
print (first_series)


# In[14]:


np_countries = np.array(["INDIA", "ENGLAND", "AMERICA", "RUSSIA", "CANADA", "CHINA", "TAIWAN", "JAPAN", "SOUTH KOREA"])


# In[15]:


series_c = pd.Series(np_countries)


# In[16]:


print (series_c)


# In[20]:


scalar_series = pd.Series(5., index= ['a','b','c','d','e','f'])
print (scalar_series)


# In[29]:


first_vector_series = pd.Series([1,2,3,4,]),index = (['a','b','c','d'])
second_vector_series = pd.Series([10,20,30,40]), index = (['a','b','c','d'])
first_vector_series + second_vector_series


# In[ ]:





# In[ ]:





# In[ ]:




