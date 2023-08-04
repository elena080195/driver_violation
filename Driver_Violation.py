#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r"/usr/local/Police_Data.csv")
data.isnull()

data.isnull().sum()
data.drop(columns = 'country_name', inplace = True)
##Removing the empty country_name column


# In[2]:


data[data.violation == 'Speeding'].driver_gender.value_counts()
##Male drivers were stopped more often than women for speeding 


# In[3]:


data.search_conducted.value_counts()
##Out of all stops, search was conducted 63056 times and not conducted 2479 times.


# In[4]:


data.groupby('driver_gender').search_conducted.sum()
##Male driver is more likely to be searched during a stop (2113 vs 366)


# In[5]:


data.stop_duration.value_counts()


# In[6]:


data['stop_duration'] = data['stop_duration'].map( {'0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' : 45})
data


# In[7]:


data['stop_duration'].mean()
##Mean duration of all stops


# In[8]:


data.groupby('violation').driver_age.describe()
##Age distribution for each type of violation


# In[ ]:




