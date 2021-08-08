#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import nltk
import urllib
import re #Regular Expression
import bs4 as bs #BeautifulSoup library for web scraping
from nltk.corpus import stopwords #to remove unnecessary words if needed


# In[2]:


nltk.download('stopwords')


# In[3]:


source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Climate_change').read() 
#this it to get the content of the entire web page


# In[4]:


soup = bs.BeautifulSoup(source,'lxml')


# In[8]:


text = ""
for paragraph in soup.find_all('p'):  #this will get all the content under the <p> tag
    text += paragraph.text


# In[15]:


text


# In[11]:


text = re.sub(r'\[[0-9]*\]',' ',text)


# In[13]:


text = re.sub(r'\s+',' ',text)


# In[14]:


text = text.lower()


# In[16]:


text = re.sub(r'\d',' ',text)


# In[19]:


text = re.sub(r'\s+',' ',text)


# In[22]:


nltk.download('punkt')


# In[23]:


sentences = nltk.sent_tokenize(text)


# In[24]:


sentences


# In[25]:


sentences = [nltk.word_tokenize(sentence) for sentence in sentences]


# In[26]:


sentences


# In[28]:


text_b = ""
for paragraph in soup.find_all():
    text_b += paragraph.text_b


# In[35]:


import autoscraper
from autoscraper import AutoScraper


# In[50]:


amazon_url = "https://www.amazon.in/s?k=iphones"

wanted_list = ["₹50,999","New Apple iPhone 11 (64GB) - Purple","35,388"]


# In[61]:


scraper = AutoScraper()
result = scraper.build(amazon_url,wanted_list)
print(result)


# In[64]:


scraper.get_result_similar(amazon_url, grouped = True)


# In[69]:


# scraper.set_rule_aliases({'rule_77zw':'Title','rule_ub27':'Price'})
# scraper.keep_rules(['rule_77zw','rule_ub27'])
# scraper.save('amazon-search')


# In[66]:


results = scraper.get_result_similar('https://www.amazon.in/s?k=mi+phones+under+15000',group_by_alias=True)


# In[70]:


# results['Title']


# In[71]:





# In[72]:


import os

os.getcwd()


# In[ ]:




