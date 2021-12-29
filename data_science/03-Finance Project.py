#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Finance Data Project 
# 
# In this data project we will focus on exploratory data analysis of stock prices. Keep in mind, this project is just meant to practice your visualization and pandas skills, it is not meant to be a robust financial analysis or be taken as financial advice.
# ____
# ** NOTE: This project is extremely challenging because it will introduce a lot of new concepts and have you looking things up on your own (we'll point you in the right direction) to try to solve the tasks issued. Feel free to just go through the solutions lecture notebook and video as a "walkthrough" project if you don't want to have to look things up yourself. You'll still learn a lot that way! **
# ____
# We'll focus on bank stocks and see how they progressed throughout the [financial crisis](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308) all the way to early 2016.

# ## Get the Data
# 
# In this section we will learn how to use pandas to directly read data from Google finance using pandas!
# 
# First we need to start with the proper imports, which we've already laid out for you here.
# 
# *Note: [You'll need to install pandas-datareader for this to work!](https://github.com/pydata/pandas-datareader) Pandas datareader allows you to [read stock information directly from the internet](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) Use these links for install guidance (**pip install pandas-datareader**), or just follow along with the video lecture.*
# 
# ### The Imports
# 
# Already filled out for you.

# In[113]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data
# 
# We need to get data using pandas datareader. We will get stock information for the following banks:
# *  Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo
# 
# ** Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**
# 1. Use datetime to set start and end datetime objects.
# 2. Figure out the ticker symbol for each bank.
# 2. Figure out how to use datareader to grab info on the stock.
# 
# ** Use [this documentation page](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html) for hints and instructions (it should just be a matter of replacing certain values. Use google finance as a source, for example:**
#     
#     # Bank of America
#     BAC = data.DataReader("BAC", 'google', start, end)
# 
# ### WARNING: MAKE SURE TO CHECK THE LINK ABOVE FOR THE LATEST WORKING API. "google" MAY NOT ALWAYS WORK. 
# ------------
# ### We also provide pickle file in the article lecture right before the video lectures.

# In[114]:


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016,1,1)


# In[116]:


#Bank of America
BAC = data.DataReader('BAC', 'yahoo', start=start, end=end)
#CitiGroup
C = data.DataReader('C', 'yahoo', start=start, end=end)
#Goldman Sachs
GS = data.DataReader('GS', 'yahoo', start=start, end=end)
#JP Morgan Chace
JPM = data.DataReader('JPM', 'yahoo', start=start, end=end)
#Morgan Stanley
MS = data.DataReader('MS', 'yahoo', start=start, end=end)
#Wells Fargo
WFC= data.DataReader('WFC', 'yahoo', start=start, end=end)


# In[41]:


BAC.head()


# ** Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**

# In[119]:


tickers = ['BAC','C','GS','JPM','MS','WFC']


# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.**

# In[120]:


bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis =1,keys = tickers)
bank_stocks.head()


# ** Set the column name levels (this is filled out for you):**

# In[121]:


bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# ** Check the head of the bank_stocks dataframe.**

# In[122]:


bank_stocks.head()


# # EDA
# 
# Let's explore the data a bit! Before continuing, I encourage you to check out the documentation on [Multi-Level Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html) and [Using .xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html).
# Reference the solutions if you can not figure out how to use .xs(), since that will be a major part of this project.
# 
# ** What is the max Close price for each bank's stock throughout the time period?**

# In[45]:


#best way to do it
bank_stocks.xs(axis= 1,key = 'Close', level = 'Stock Info').max()


# ** Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock. returns are typically defined by:**
# 
# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$

# In[46]:


returns = pd.DataFrame()


# ** We can use pandas pct_change() method on the Close column to create a column representing this return value. Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.**

# In[47]:


for tick in tickers:
    returns[tick+" Return"] = bank_stocks[tick]['Close'].pct_change()
returns


# ** Create a pairplot using seaborn of the returns dataframe. What stock stands out to you? Can you figure out why?**

# In[48]:


sns.pairplot(returns[1:])


# * See solution for details about Citigroup behavior....

# ** Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns. You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?**

# In[56]:


returns.idxmin()


# ** You should have noticed that Citigroup's largest drop and biggest gain were very close to one another, did anythign significant happen in that time frame? **

# * See Solution for details

# In[57]:


returns.idxmax()


# ** Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? Which would you classify as the riskiest for the year 2015?**

# In[58]:


returns.std()   #citi group is the riskiest


# In[71]:


returns.loc['2015-01-01':'2015-12-31'].std() 


# ** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **

# In[83]:


sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'],color = 'green', bins = 50 )


# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **

# In[78]:


sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'], color = 'red', bins =50)


# ____
# # More Visualization
# 
# A lot of this project will focus on visualizations. Feel free to use any of your preferred visualization libraries to try to recreate the described plots below, seaborn, matplotlib, plotly and cufflinks, or just pandas.
# 
# ### Imports

# In[84]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# ** Create a line plot showing Close price for each bank for the entire index of time. (Hint: Try using a for loop, or use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) to get a cross section of the data.)**

# In[88]:


bank_stocks.xs(axis =1, key = 'Close', level = 'Stock Info').plot(figsize=(12,4),label=tick)

plt.legend


# In[89]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()


# In[123]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# ## Moving Averages
# 
# Let's analyze the moving averages for these stocks in the year 2008. 
# 
# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008**

# In[105]:


# BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window= 30).mean().iplot(color = 'green')
# BAC['Close'].loc['2008-01-01':'2009-01-01'].iplot()


# In[106]:


plt.figure(figsize=(12,6))
BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE', color = 'green')
plt.legend()


# ** Create a heatmap of the correlation between the stocks Close Price.**

# In[125]:


sns.heatmap(bank_stocks.xs(key='Close', level='Stock Info', axis = 1).corr(),annot=True)


# ** Optional: Use seaborn's clustermap to cluster the correlations together:**

# In[127]:


sns.clustermap(bank_stocks.xs(level= 'Stock Info', key = 'Close', axis = 1).corr(), annot = True)


# In[42]:





# # Part 2 (Optional)
# 
# In this second part of the project we will rely on the cufflinks library to create some Technical Analysis plots. This part of the project is experimental due to its heavy reliance on the cuffinks project, so feel free to skip it if any functionality is broken in the future.

# ** Use .iplot(kind='candle) to create a candle plot of Bank of America's stock from Jan 1st 2015 to Jan 1st 2016.**

# In[134]:


BAC[['High', 'Low', 'Open', 'Close']].loc['2015-01-01':'2016-01-01'].iplot(kind = 'candle')


# ** Use .ta_plot(study='sma') to create a Simple Moving Averages plot of Morgan Stanley for the year 2015.**

# In[138]:


MS[['High', 'Low', 'Open', 'Close']].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma', periods=[13,21,55],title='Simple Moving Averages')


# **Use .ta_plot(study='boll') to create a Bollinger Band Plot for Bank of America for the year 2015.**

# In[139]:


BAC[['Open', 'Close', 'High', 'Low']].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')


# # Great Job!
# 
# Definitely a lot of more specific finance topics here, so don't worry if you didn't understand them all! The only thing you should be concerned with understanding are the basic pandas and visualization oeprations.
