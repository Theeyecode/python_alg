#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')
iris = sns.load_dataset('iris')
iris.head()


# ## Linear Model and Rgression Plot

# In[10]:


tip = sns.load_dataset('tips')
tip.head()


# In[14]:


sns.lmplot(x='total_bill', y = 'tip', data = tip, hue = 'sex', markers = ['o', 'v'])


# In[15]:


#instead of using "hue"


# In[20]:


sns.lmplot(x='total_bill', y = 'tip', data = tip, col = 'sex', row = 'time')


# In[18]:


tip['time'].unique()


# In[22]:


sns.lmplot(x='total_bill', y = 'tip', data = tip, col = 'day', row = 'time', hue = 'sex')


# In[ ]:




