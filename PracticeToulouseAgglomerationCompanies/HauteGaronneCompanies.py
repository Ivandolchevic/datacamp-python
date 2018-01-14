'''
Created on Sep 5, 2017

@author: idolchevic
'''

import pandas as pd
import re
import unidecode

# all cities of the toulouse area
toulouse_area = ['AIGREFEUILLE', 'AUCAMVILLE', 'AUSSONNE', 'AUZIELLE', 'BALMA', 'BEAUPUY', 'BEAUZELLE', 'BLAGNAC', 'BRAX', 'BRUGUIERES', 'CASTELGINEST', 'COLOMIERS', 'CORNEBARRIEU', 'CUGNAUX', 'DREMILLAFAGE', 'FENOUILLET', 'FLOURENS', 'FONBEAUZARD', 'GAGNACSURGARONNE', 'GRATENTOUR', 'LUNION', 'LABEGE', 'LAUNAGUET', 'LESPINASSE', 'MONDONVILLE', 'MONDOUZIL', 'MONS', 'MONTRABE', 'PIBRAC', 'PINBALMA','QUINTFONSEGRIVES', 'SAINTALBAN', 'SAINTJEAN', 'SAINTJORY', 'SAINTORENSDEGAMEVILLE', 'SAINTREMYDEPROVENCE', 'SEILH', 'TOULOUSE', 'TOURNEFEUILLE', 'VILLENEUVETOLOSANE']

# read the source file of companies 
df_base_sirene_reader = pd.read_csv('base-sirene.csv',chunksize=1000,sep=';') 

def format_city(ncc):
    '''Format the cities names for joining them with other datas'''
    accent_removed = unidecode.unidecode(ncc)
    special_chars_removed = accent_removed.replace('-','').replace('\'','').replace(' ','')
    result = re.sub(r'\sCEDEX\s[0-9]','',special_chars_removed)    
    result = re.sub(r'\sCEDEX','',result)
    result = re.sub(r'\sARMEES','',result)
    result = re.sub(r'^QUINT$','QUINTFONSEGRIVES',result)
    result = re.sub(r'ST\s','SAINT ',result)
    
    return result.upper()

def extract_area(value):
    if format_city(value) in toulouse_area:
        return 'TOULOUSE'
    else:
        return 'OTHERS'

no_year_count = 0;
def extract_year(value):
    try:
        return re.compile('[0-9]{4}').match(value).group()
    except TypeError:
        global no_year_count 
        no_year_count += 1            
        print('TypeError on ',value)

df_cies_count = pd.DataFrame()

#for _ in range(5):
#    df_chunk = next(df_base_sirene_reader)
for df_chunk in df_base_sirene_reader:        
    df_partial_cies_count = pd.DataFrame()
    
    # get the areas
    df_partial_cies_count['area'] = df_chunk['Libellé de la commune de localisation de l\'établissement'].map(extract_area)
    
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


















