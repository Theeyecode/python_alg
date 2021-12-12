#!/usr/bin/env python
# coding: utf-8

# ## Categorical Plots
# 

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')
tips.head()


# In[2]:


import numpy as np


# In[4]:


sns.barplot(x = "sex", y = "total_bill", data = tips, estimator = np.std)


# In[5]:


sns.countplot(x = 'sex', data = tips)


# In[9]:


sns.boxplot(x = 'day', y = 'total_bill', data = tips)


# In[11]:


sns.violinplot(x = 'day', y = 'total_bill', data = tips , hue = 'sex')


# In[22]:


sns.stripplot(x = 'day', y = 'total_bill', data = tips , hue = 'sex', jitter = True, dodge = True)


# In[21]:


sns.swarmplot(x = 'day', y = 'total_bill', data = tips , )


# ## General Plot

# In[27]:


sns.catplot(x = 'day', y = 'total_bill', data = tips , kind = 'box')


# In[ ]:




