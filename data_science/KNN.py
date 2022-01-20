#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


df = pd.read_csv("Classified Data", index_col = 0)


# In[6]:


df.head()


# In[8]:


df.info()


# ## SCALE THE DATA

# In[10]:


from sklearn.preprocessing import StandardScaler


# In[11]:


scaler = StandardScaler()


# In[12]:


scaler.fit(df.drop('TARGET CLASS', axis =1))


# In[14]:


scaler_feature = scaler.transform(df.drop('TARGET CLASS', axis =1))


# In[15]:


scaler_feature


# In[18]:


new_df = pd.DataFrame(scaler_feature, columns = df.columns[:-1])


# In[47]:


new_df.head()


# ## APPLY TRAIN TEST SPLIT
# 

# In[20]:


from sklearn.model_selection import train_test_split


# In[56]:


X = new_df
y= df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# ## USING KNN

# In[49]:


from sklearn.neighbors import KNeighborsClassifier


# In[57]:


knn = KNeighborsClassifier(n_neighbors=1)


# In[58]:


knn.fit(X_train, y_train)


# In[59]:


pred = knn.predict(X_test)


# ## Prediction and Evaluation

# In[60]:


from sklearn.metrics import classification_report,confusion_matrix


# In[61]:


print(confusion_matrix(y_test,pred))


# In[62]:


print(classification_report(y_test,pred))


# ## How to choose a K value
# 

# In[38]:


error_range = []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train,y_train)
    pred = knn.predict(X_test)
    error_range.append(np.mean(pred != y_test))
    
    
    


# In[39]:


plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_range,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Range')


# In[40]:


#then we can set k = 14 to increade the prediction


# In[45]:


knn = KNeighborsClassifier(n_neighbors = 27)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
    
print('WITH K=27')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# In[42]:


knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
    
print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# In[ ]:




