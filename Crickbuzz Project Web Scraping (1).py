#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


r=requests.get("https://www.britannica.com/sports/Cricket-World-Cup")


# In[3]:


r


# In[5]:


soup=BeautifulSoup(r.text)

soup


# In[6]:


result=soup.find_all("td")


# In[7]:


result  


# In[8]:


firstpart=result[0]
firstpart.text.strip()


# In[9]:


record=[]
for i in result:
    data=i.text.strip()
    record.append(data)


# In[10]:


record


# In[11]:


table=[]
for i in range(len(record)):
    part=record[:6]
    del record[:6]
    
    if len(part)==6:
        table.append(part)


# In[12]:


table


# In[13]:


import pandas as pd
df=pd.DataFrame(table,columns=["Year","Winner","Score","Runner-up","Score","Result"])


# In[14]:


df


# In[15]:


df.to_csv("Crickbuzz.csv",index=False)


# In[16]:


df=pd.read_csv("Crickbuzz.csv")


# In[ ]:




