#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports
# new library: requests
import requests
# standard imports
import numpy as np
import pandas as pd
# formatting
from pprint import pprint
# os
import os


# In[2]:


def create_response(web_url):
    '''
    This definition takes in a web url, 
    imports it into a HTTP request, 
    and creates and returns a HTTP response. 
    Print statements have been added for error checks.
    '''
    response = requests.get(web_url)
    if response.status_code >= 400 and response.status_code < 500:
        print("400's error: you did something wrong or forbidden")
    elif response.status_code >= 500 and response.status_code < 600:
        print("500's error: the server-side is having a problem")
    else:
        print("200's: cleared to move forward.\n")
    home_content = response.json()
    pprint(home_content)
    return response, home_content


# In[3]:


def create_df_from_response(page, entry):
    '''
    This definition takes in 'page' - the web page name of interest,
    and 'entry' - a data index/entry number. It then prints the length
    of the aquired page and the data associated with the provided entry 
    number, and returns a pandas dataframe of the data.
    '''
    page_content = home_content[page]
    page_response = requests.get(home_content[page])
    first_page = page_response.json()
    print(f'\nLength of page: {len(first_page["results"])}')
    print('-'*50)
    print(f'Entry content:')
    pprint(f'{first_page["results"][entry]}')
    if os.path.exists(f'{page}_df.csv'):
        print('-'*50)
        print('csv file already exists, no csv file created.')
        print('_'*70)
        page_df = pd.DataFrame(first_page["results"])
    else: 
        page_df = pd.DataFrame(first_page["results"])
        page_df.to_csv(f'{page}_df.csv') 
        print('-'*50)
        print(f'csv created for {page} data frame.')
        print('_'*70)
    return page_df


# In[5]:


def combine_dfs(dfs_list, concat_df_name):
    '''
    This function takes in dfs_list - a list of dataframes 
    to be concatinated, and concat_df_name - a name for the 
    new concatinated dataframe. The function then concats the
    dataframes in dfs_list and checks if a file with the 
    concat_df_name alreay exists. If the file exists a print 
    statement stating its existence is produced. If the file 
    does not exist a file with concat_df_name is created and 
    a print statement reiterates its creation. There is also 
    a check inplace for an empty list of dfs
    '''
    dfs = []
    for file in dfs_list:
        df = pd.read_csv(file)
        dfs.append(df)
    if os.path.exists(f'{concat_df_name}.csv'):
        print('-'*50)
        print('CSV file already exists. No new CSV file created.')
        print('_'*70)
        combined_df = pd.concat(dfs, axis=0, ignore_index=True)
        return combined_df
    else: 
        if len(dfs) == 0:
            print('-'*50)
            print('Empty list of dataframes.')
            print('_'*70)
            return pd.DataFrame()
        else:
            combined_df = pd.concat(dfs, axis=0, ignore_index=True)
            combined_df.to_csv(f'{concat_df_name}.csv') 
            print('-'*50)
            print(f'CSV file created for {concat_df_name}.')
            print('_'*70)
            return combined_df


# In[ ]:




