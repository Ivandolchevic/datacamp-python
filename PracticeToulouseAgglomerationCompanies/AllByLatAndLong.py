'''
Created on Sep 5, 2017

@author: idolchevic
'''

import pandas as pd
import re
import seaborn as sns

sns.set()

df_base_sirene_reader = pd.read_csv('base-sirene.csv',chunksize=1000,sep=';') 

def extract_coordinate_lat(value):
    '''Extract the latitudes from the original coordinates'''    
    try:
        lat = float(value.split(',')[0].strip())
        if (lat < 42) | (lat > 44.2):
            return ''
        else :
            return str(lat) 
    except AttributeError:
        return ''         
    
def extract_coordinate_long(value):
    '''Extract the longitudes from the original coordinates'''    
    try:
        long = float(value.split(',')[1].strip())
        if (long < 0.2) | (long > 2.4):
            return ''
        else :
            return str(long) 
    except AttributeError:
        return ''         
            
def extract_year(value):
    try:
        return re.compile('[0-9]{4}').match(value).group()
    except TypeError:                
        return ''

def is_luchon(value):
    if 'LUCHON' in value.upper():
        print(value)
    

df_cies_by_latlong = pd.DataFrame()

#for _ in range(10):
#    df_chunk = next(df_base_sirene_reader)
for df_chunk in df_base_sirene_reader:        
    df_partial_cies = pd.DataFrame()    
    #df_chunk = df_chunk[df_chunk['Libellé de la commune de localisation de l\'établissement']== 'BAGNERES DE LUCHON']
    #df_chunk = df_chunk[df_chunk['Libellé de la commune de localisation de l\'établissement']== 'TOULOUSE']
    #df_chunk = df_chunk[df_chunk['Libellé de la commune de localisation de l\'établissement']== 'SAINT GAUDENS']
    
    # extract the latitudes    
    df_partial_cies['lat'] = df_chunk['coordonnees'].map(extract_coordinate_lat)
    
    # extract the longitudes
    df_partial_cies['long'] = df_chunk['coordonnees'].map(extract_coordinate_long)
        
    
    # get the years of creation of the companies
    df_partial_cies['year'] = df_chunk['Année et mois de création de l\'établissement'].map(extract_year)
    
    # merge with the global count
    df_cies_by_latlong = df_cies_by_latlong.append(df_partial_cies)
    
# delete rows without coordinates
df_cies_by_latlong.drop(df_cies_by_latlong[df_cies_by_latlong.lat == ''].index,inplace=True)
df_cies_by_latlong.drop(df_cies_by_latlong[df_cies_by_latlong.long == ''].index,inplace=True)

# delete rows without year
df_cies_by_latlong.drop(df_cies_by_latlong[df_cies_by_latlong.year == ''].index,inplace=True)

# sort by year
df_cies_by_latlong.sort_values(by='year', axis=0, ascending=True, inplace=True)
  
df_cies_by_latlong.to_csv('allbylatandlong.csv')
