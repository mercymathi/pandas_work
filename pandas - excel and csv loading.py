#!/usr/bin/env python
# coding: utf-8

# In[3]:


#csv and excel loading
import pandas as pd
stu=pd.DataFrame({'id':[1,2,3],'name':['surya','kinjal','nithin'],'age':[23,32,24]})
stu


# In[4]:


stu.set_index(keys='id',inplace=True)
stu


# In[7]:


stu.to_csv('stu_csv.csv')
stu.to_excel('stu_excel.xlsx')
 


# In[ ]:




