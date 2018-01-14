'''
Created on Sep 5, 2017

@author: idolchevic
'''
'''
Created on Sep 1, 2017

@author: idolchevic
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns

sns.set()

# read the source file of companies 
df_base_sirene_reader = pd.read_csv('base-sirene.csv',chunksize=1000,sep=';') 

def extract_area(value):
    if 'TOULOUSE' in value:
        return 'TOULOUSE'
    else:
        return 'AGGLOMERATION'
    
def extract_year(value):
    try:
        return re.compile('[0-9]{4}').match(value).group()
    except TypeError:            
        print('TypeError on ',value)

df_cies_count = pd.DataFrame()

#for _ in range(5):
#    df_chunk = next(df_base_sirene_reader)
for df_chunk in df_base_sirene_reader:        
    
    df_partial_cies_count = pd.DataFrame()
    
    # get the areas
    df_partial_cies_count['area'] = df_chunk['Sixième ligne de l’adressage de l’établissement'].map(extract_area)
    
    # get the years of creation of the companies
    df_partial_cies_count['year'] = df_chunk['Année et mois de création de l\'établissement'].map(extract_year)
    
    df_partial_cies_count.sort_index()
    # aggregate by areas and years    
    df_partial_cies_count = df_partial_cies_count.groupby(['area','year'])['area','year'].count().rename(columns={'year':'count'})
  
    # remove the unused column
    del df_partial_cies_count['area']
    
    # merge with the global count
    df_cies_count = df_cies_count.append(df_partial_cies_count) 

    
# aggregate the count by areas and by years
df_cies_count = df_cies_count.groupby(['area','year']).sum()

# store the result into a csv file
df_cies_count.to_csv('cies_count.csv')
print(df_cies_count)
