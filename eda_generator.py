#!/usr/bin/env python
# coding: utf-8

# In[5]:

#pip install ydata-profiling

# In[5]:


import pandas as pd
from ydata_profiling import ProfileReport

def generate_eda_report(df, output_path):
    profile = ProfileReport(df, title = "Автоматический EDA-отчет", explorative=True)
    profile.to_file(output_path)


