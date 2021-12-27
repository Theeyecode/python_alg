#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')


# In[5]:


tips.head()


# In[6]:


flights.head()


# In[7]:


## before you can perform a matrix plot..you need to make your data in matrix form


# In[9]:


tc = tips.corr()
tc


# In[18]:


sns.heatmap(tc, annot = True, cmap = 'coolwarm')


# In[19]:


flights


# In[20]:


# you can turn the flight data_set into a matrix plot by using the pivot_table argument


# In[30]:


fp = flights.pivot_table(index = 'month', columns = 'year', values = "passengers", margins = True)
fp


# In[39]:


sns.heatmap(fp,linewidth = 1, linecolor = "black" , cmap = 'coolwarm')


# In[41]:


sns.clustermap(fp, cmap = 'coolwarm', linecolor = 'black', linewidth = 1)


# In[ ]:




