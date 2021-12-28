#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Choropleth Maps Exercise 
# 
# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples
# 
# [Full Documentation Reference](https://plot.ly/python/reference/#choropleth)
# 
# ## Plotly Imports

# In[37]:


import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 
import pandas as pd


# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

# In[38]:


df = pd.read_csv('2014_World_Power_Consumption')
df.head()


# In[51]:


data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = df['Country'],
        locationmode = "country names",
        z = df['Power Consumption KWH'],
        text = df['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 

layout = dict(title = '2014 Power Consumption KWH',
                geo = dict(showframe = False,projection = {'type':'mercator'})
             )


# ** Check the head of the DataFrame. **

# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

# In[48]:





# In[52]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# ## USA Choropleth
# 
# ** Import the 2012_Election_Data csv file using pandas. **

# In[20]:


usdf = pd.read_csv('2012_Election_Data')


# ** Check the head of the DataFrame. **

# In[21]:


usdf.head()


# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

# In[31]:


data = dict(type = 'choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'], 
            z = usdf["Voting-Age Population (VAP)"],
            locationmode = 'USA-states',
            text = usdf['State'],
            markers = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar={"title":"Voting-Age Population (VAP)"})

layout = dict(title = '2012 General Election Voting Data',   geo = dict(scope='usa',showlakes = True,lakecolor = 'rgb(85,173,240)')
             )
           


# In[121]:





# In[53]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# # Great Job!
