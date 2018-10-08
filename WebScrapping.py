
# coding: utf-8

# In[39]:


import urllib.request as url
import bs4
import pandas as pd


# In[40]:


page = url.urlopen("http://stats.espncricinfo.com/ci/engine/records/team/largest_margins.html?class=2;id=6;type=team")


# In[41]:


# lxml - library xml
soup = bs4.BeautifulSoup(page, 'lxml')


# In[42]:


tables = soup.find_all('table', class_ = "engineTable")


# In[43]:


# for data in tables:
#     print(data.text)

data = []
for d in tables:
    data.append(d.text)


# In[44]:


# print(data[0])
data_1 = data[0].replace("\n","\t")


# In[45]:


data_1 = data_1.replace("\t\t","\t")


# In[46]:


data_1 = data_1.replace("\t\t\t","\t")


# In[47]:


data_1 = data_1.replace("\t\t","\t")


# In[ ]:


data_1 = re.sub("India")


# In[63]:


data_1


# In[51]:


data_2 = data_1


# In[55]:


data_2 [0]


# In[56]:


df = []
for i in data_1:
    df.append([i])


# In[57]:


print (df)


# In[60]:


dataset = []
for i in range(len(df)):
    print (df[i][0])
#     dataset.append(df[i][0].split(","))


# In[81]:


print(dataset)


# In[83]:


df = pd.DataFrame(dataset)


# In[85]:


df.columns = dataset[0]


# In[87]:


df.drop(0)

