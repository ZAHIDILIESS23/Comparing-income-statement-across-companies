#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import requests
import pandas as pd


# In[159]:


import requests
quote=['FB']
def selectquote(quote):
    r = requests.get(f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={quote}&interval=5min&apikey=UNWGJY8A55P2VSOR').json()
    d = r['annualReports']
    stock=pd.DataFrame(d)
    stock=stock.T
## set name of columns
    stock.columns=stock.iloc[0]
    stock.reset_index(inplace=True)
    stock=stock.iloc[:,0:2]
    stock=stock.rename(columns={stock.columns[1]:quote})
## convert to number
    clos=stock.columns.drop('index')
    stock[clos]=stock[clos].apply(pd.to_numeric,errors='coerce')
## remove first columns
    stock=stock.iloc[2:,:]
    stock[quote]=stock[quote]/stock.iloc[1,1]## devided by the revenue
    stock[quote]=pd.Series(["{0:.2f}%".format(val*100) for val in stock[quote]],index=stock.index)
    return stock
result=selectquote('FB')
result


# In[160]:


listofstock=['GOOGL','MSFT','AAPL']
for item in listofstock:
    y=selectquote(item)
    result=result.merge(y,on='index')
result


# In[146]:


stock


# In[ ]:


pd.read

