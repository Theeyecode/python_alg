#!/usr/bin/env python
# coding: utf-8

# In[50]:


import chart_studio.plotly as py
import plotly.graph_objs as go 
import pandas as pd


# In[5]:


from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot


# In[6]:


init_notebook_mode(connected = True)


# In[46]:


data = dict(type = 'choropleth',
            locations = ['AZ','CA','TX'],
            locationmode = 'USA-states',
            colorscale= 'portland',
            text= ['Arizona','Cali','Texas'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})


# In[47]:


data


# In[41]:


layout = dict(geo = {'scope':'usa'})


# In[42]:


layout


# In[48]:


choromap = go.Figure(data = [data],layout = layout)


# In[49]:


iplot(choromap)


# In[53]:


df = pd.read_csv('2011_US_AGRI_Exports')
df.head()


# In[63]:


data = dict(type='choropleth',
            colorscale = 'ylorrd',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Thousands USD"}
            ) 


# In[65]:


layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[66]:


layout


# In[67]:


choromap = go.Figure(data = [data],layout = layout)


# In[68]:


iplot(choromap)


# In[ ]:




