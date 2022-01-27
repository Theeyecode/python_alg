#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


from sklearn.datasets import load_breast_cancer


# In[6]:


cancer = load_breast_cancer()


# In[14]:


cancer.keys()


# In[24]:


cancer['feature_names']


# In[15]:


df_cancer = pd.DataFrame(cancer['data'], columns = cancer['feature_names'])


# In[17]:


df_cancer.head(2)


# In[25]:


from sklearn.model_selection import train_test_split


# In[26]:


train_test_split


# In[28]:


X = df_cancer
y = cancer['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# In[30]:


from sklearn.svm import SVC


# In[74]:


model = SVC(gamma = 'auto') #gamma = 'scale' we don't need to grid again 


# In[75]:


model.fit(X_train, y_train)


# In[76]:


predictions = model.predict(X_test)


# In[77]:


from sklearn.metrics import classification_report,confusion_matrix


# In[78]:


print(classification_report(y_test, predictions))
print('\n')
print(confusion_matrix(y_test, predictions))


# In[53]:


from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']} 


# In[54]:


grid = GridSearchCV(SVC(),param_grid, refit=True,verbose=3)


# In[55]:


# May take awhile!
grid.fit(X_train,y_train)


# In[56]:


grid.best_params_


# In[57]:


grid.best_estimator_


# In[60]:


grid_predictions = grid.predict(X_test)


# In[62]:


print(classification_report(y_test, grid_predictions))
print('\n')
print(confusion_matrix(y_test, grid_predictions))


# In[ ]:




