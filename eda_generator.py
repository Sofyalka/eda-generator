#!/usr/bin/env python
# coding: utf-8

# In[5]:


#pip install ydata-profiling


# In[10]:


#import pandas as pd
#from ydata_profiling import ProfileReport
#df = pd.read_csv('dataset_olympics.csv')
#profile = ProfileReport(df)
#profile.to_file("report.html")


# In[1]:


#pip install weasyprint


# In[5]:


import pandas as pd
from ydata_profiling import ProfileReport

def generate_eda_report(df, output_path):
    profile = ProfileReport(df, title = "Автоматический EDA-отчет", explorative=True)
    profile.to_file(output_path)


# In[9]:


#pip install "fastapi[standard]"


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




