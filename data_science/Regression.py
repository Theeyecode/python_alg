#!/usr/bin/env python
# coding: utf-8

# ## LINEAR REGRESSION
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('USA_housing.csv')


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[9]:


sns.pairplot(df)


# In[12]:


sns.histplot(df['Price'], kde = True)


# In[14]:


sns.heatmap(df.corr(), annot = True)


# Get an X and Y data then do a training test model
# 

# In[17]:


df.columns


# In[18]:


X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population', ]]

Y = df['Price']    #what we are interested in is the Price and its what we are trying to predict


# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=101)


# In[24]:


from sklearn.linear_model import LinearRegression


# In[25]:


lm = LinearRegression()


# In[33]:


lm.fit(X_train,y_train)


# In[27]:


print(lm.intercept_)


# In[28]:


lm.coef_


# In[30]:


X.columns


# In[31]:


cdf = pd.DataFrame(lm.coef_, X.columns, columns = ['coeff'])


# In[32]:


cdf


# ## PREDICTIONS

# In[34]:


lm


# In[35]:


prediction = lm.predict(X_test)


# In[36]:


prediction


# In[37]:


y_test


# In[38]:


# we want to know how far off is our predction


# In[41]:


sns.scatterplot( x= y_test, y= prediction)


# In[42]:


residuals = y_test - prediction


# In[44]:


sns.histplot(residuals, kde = True)


# In[45]:


from sklearn import metrics


# In[46]:


metrics.mean_absolute_error(y_test, prediction)


# In[47]:


metrics.mean_squared_error(y_test,prediction)


# In[49]:


np.sqrt(metrics.mean_squared_error(y_test,prediction))


# In[ ]:




