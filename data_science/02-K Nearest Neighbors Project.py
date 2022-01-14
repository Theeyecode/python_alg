#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # K Nearest Neighbors Project 
# 
# Welcome to the KNN Project! This will be a simple project very similar to the lecture, except you'll be given another data set. Go ahead and just follow the directions below.
# ## Import Libraries
# **Import pandas,seaborn, and the usual libraries.**

# In[52]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Get the Data
# ** Read the 'KNN_Project_Data csv file into a dataframe **

# In[10]:


df = pd.read_csv('KNN_Project_Data')


# **Check the head of the dataframe.**

# In[11]:


df.head()


# # EDA
# 
# Since this data is artificial, we'll just do a large pairplot with seaborn.
# 
# **Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.**

# In[12]:


sns.pairplot(df, hue = 'TARGET CLASS', palette='coolwarm')


# # Standardize the Variables
# 
# Time to standardize the variables.
# 
# ** Import StandardScaler from Scikit learn.**

# In[13]:


from sklearn.preprocessing import StandardScaler


# ** Create a StandardScaler() object called scaler.**

# In[14]:


scaler = StandardScaler()


# ** Fit scaler to the features.**

# In[17]:


scaler.fit(df.drop('TARGET CLASS', axis =1))


# **Use the .transform() method to transform the features to a scaled version.**

# In[19]:


scaler_feature = scaler.transform(df.drop('TARGET CLASS', axis =1))


# **Convert the scaled features to a dataframe and check the head of this dataframe to make sure the scaling worked.**

# In[22]:


new_df = pd.DataFrame(scaler_feature, columns = df.columns[:-1])
new_df.head()


# # Train Test Split
# 
# **Use train_test_split to split your data into a training set and a testing set.**

# In[74]:


from sklearn.model_selection import train_test_split


# In[76]:


X = scaler_feature
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


# # Using KNN
# 
# **Import KNeighborsClassifier from scikit learn.**

# In[61]:


from sklearn.neighbors import KNeighborsClassifier


# **Create a KNN model instance with n_neighbors=1**

# In[77]:


knn = KNeighborsClassifier(n_neighbors =1)


# **Fit this KNN model to the training data.**

# In[78]:


knn.fit(X_train, y_train)


# # Predictions and Evaluations
# Let's evaluate our KNN model!

# **Use the predict method to predict values using your KNN model and X_test.**

# In[79]:


predict = knn.predict(X_test)


# ** Create a confusion matrix and classification report.**

# In[65]:


from sklearn.metrics import classification_report,confusion_matrix


# In[80]:


print(confusion_matrix(y_test,predict))


# In[81]:


print(classification_report(y_test,predict))


# # Choosing a K Value
# Let's go ahead and use the elbow method to pick a good K Value!
# 
# ** Create a for loop that trains various KNN models with different k values, then keep track of the error_rate for each of these models with a list. Refer to the lecture if you are confused on this step.**

# In[82]:


error_rate =[]
for i in range (1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train,y_train)
    pred = knn.predict(X_test)
    error_rate.append(np.mean(pred != y_test))


# **Now create the following plot using the information from your for loop.**

# In[83]:


plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='black', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# ## Retrain with new K Value
# 
# **Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.**

# In[86]:


knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train, y_train)
predict = knn.predict(X_test)
print('WITH K=30')
print('\n')
print(confusion_matrix(y_test,predict))
print("\n")
print(classification_report(y_test,predict))


# # Great Job!

# In[ ]:




