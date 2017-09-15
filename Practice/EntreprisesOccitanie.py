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


def get_special_char_count(line):
    '''Get the count of special chars into a row'''
    return {char:line.count(char) for char in ''.join(set(line)) if re.compile(';|,|(\t)|(\s{4,6})').match(char)}

def get_column_separator(file,n=20):
    '''Get the count of special chars of each first n rows '''
    # initialize the special char count array
    counts = {}
    
    # for each line
    for i in range(n):
        line = file.readline()
        counts[i] = get_special_char_count(line)
            
    return pd.DataFrame(counts)

# global vars
filename = 'base-sirene.csv'

#check file format
with open(filename) as file:
    df_counts = get_column_separator(file)
    df_counts.index.name = 'char'

means = df_counts.unstack(level='char').groupby('char').mean() 
std = df_counts.unstack(level='char').groupby('char').std()

# get the separator
sep = std[std == 0].index[0]

# inspect the head of the file
#with open(filename) as file:
#    for _ in range(10):
#        print(file.readline())        

# 

def extract_address(df):
    '''Extract the postal code and the city from the original row'''
    return list(df_chunk['Sixième ligne de l’adressage de l’établissement'].apply(lambda address:{'postalcode': re.compile('[0-9]{4,5}').match(address).group(), 'city':address.replace(re.compile('[0-9]{4,5}').match(address).group(),'').strip()}))

def extract_area(value):
    if 'TOULOUSE' in value:
        return 'TOULOUSE'
    else:
        return 'AGGLOMERATION'
    
def extract_coordinates_lat(df):
    '''Extract the latitudes from the original coordinates'''
        
    def get_lat(value):
        try:
            return value.split(',')[0].strip()
        except AttributeError:
            return 0.0         
    
    return list(df_chunk["coordonnees"].apply(get_lat))
        

def extract_coordinates_long(df):
    '''Extract the longitudes from the original coordinates'''
    
    def get_long(value):
        try:
            return value.split(',')[1].strip()
        except AttributeError:
            return 0.0       
        
    return list(df_chunk["coordonnees"].apply(get_long))

def extract_year(value):
    try:
        return re.compile('[0-9]{4}').match(value).group()
    except TypeError:            
         print('TypeError on ',value)


counts = pd.Series()

df_reader = pd.read_csv(filename,chunksize=1000,sep=sep) 

for _ in range(1):
    df_chunk = next(df_reader)
#for df_chunk in df_reader:        
    
    df_partial_cies_count = pd.DataFrame()
    
    # get the areas
    df_partial_cies_count['area'] = df_chunk['Sixième ligne de l’adressage de l’établissement'].map(extract_area)
    
    # get the years of creation of the companies
    df_partial_cies_count['year'] = df_chunk['Année et mois de création de l\'établissement'].map(extract_year)
    
    # aggregate by areas and years
    print(df_partial_cies_count.groupby(['area','year']).count())
    df_partial_cies_count['count'] = df_partial_cies_count.groupby(['area','year']).count() 
    
    # set index of the partial dataframe
    df_partial_cies_count.set_index(['area','year'],inplace=True)
    df_partial_cies_count.sort_index()

    print(df_partial_cies_count)

#print(counts)

# Make bar plot of change: ax
ax = counts.plot(kind='barh')

# Customize the plot to improve readability
ax.set_ylabel("count of companies")
ax.set_title("Occitanie - companies by cities")

plt.margins(0.10)

# Display the plot
#plt.show()






