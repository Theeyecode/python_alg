#!/usr/bin/env python
# coding: utf-8

# In[19]:


import seaborn as sns


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


tips = sns.load_dataset('tips')


# In[22]:


tips.head()


# ## displot (one_variable)

# In[23]:


sns.histplot(tips['total_bill'],)


# In[29]:


sns.jointplot(x = 'total_bill', y ='tip', data = tips, ) 


# In[31]:


sns.pairplot(data = tips, hue = "sex")


# In[ ]:




