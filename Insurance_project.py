#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("insurance.csv")
df = pd.DataFrame(data)
df.head()
df.info()


# In[11]:


df.isna().sum()##null value check


# In[ ]:


##no null values


# In[12]:


df.corr() 


# In[ ]:


## age and charges have strongest relationship followed by bmi and charges


# In[14]:


fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(10,8))
df.plot(kind='hist', y = 'age', bins = 70, color = 'b', ax=axes[0][0])
df.plot(kind='hist', y = 'bmi', bins = 70, color = 'r', ax=axes[0][1])
df.plot(kind='hist', y = 'children', bins = 70, color = 'y', ax=axes[1][0])
df.plot(kind='hist', y = 'charges', bins = 70, color = 'g', ax=axes[1][1])
plt.show()


# In[19]:


##df.plot(kind='scatter',x='bmi',y='charges')
sns.scatterplot(data=df,x='bmi',y='charges',hue='smoker')
plt.show()


# In[ ]:


## indicates premium charges of smokers increases with bmi


# In[40]:


sns.pairplot(df,hue='smoker')
plt.show()


# In[ ]:


## indicates age and bmi contribute to increases premium charges for smokers than non smokers


# In[31]:


pd.get_dummies(data=df,columns=['sex','smoker','region'])
sns.countplot(x=df['smoker'])
plt.show()


# In[29]:


sns.boxplot(x='smoker',y='charges',data=df)
plt.show()


# In[ ]:


## Above data clearly represents that the premium charges for smokers is greater than non-smokers


# In[37]:


sns.scatterplot(data=df,x='age',y='charges',size='smoker',hue='smoker',alpha=0.5)
plt.show()


# In[ ]:


## Above data clearly represents that the premium charges increases with age and charges for smokers is greater than non-smokers

