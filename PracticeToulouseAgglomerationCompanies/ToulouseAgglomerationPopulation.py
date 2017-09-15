'''
Created on Sep 4, 2017

@author: idolchevic
'''

import pandas as pd
import re
import unidecode
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()

#df = pd.read_excel(io='Fichier_poplegale_6814.xls',index_col=0,sheetname='2014',skiprows=6)
#print(df[df.NCC == 'Toulouse'])
xl = pd.ExcelFile('Fichier_poplegale_6814.xls')

# extract years from sheet names
years = [sheetname for sheetname in xl.sheet_names if bool(re.compile('[0-9]{4}').match(sheetname)) ]

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
    

pop_count = pd.DataFrame()
toulouse_area = ['AIGREFEUILLE', 'AUCAMVILLE', 'AUSSONNE', 'AUZIELLE', 'BALMA', 'BEAUPUY', 'BEAUZELLE', 'BLAGNAC', 'BRAX', 'BRUGUIERES', 'CASTELGINEST', 'COLOMIERS', 'CORNEBARRIEU', 'CUGNAUX', 'DREMILLAFAGE', 'FENOUILLET', 'FLOURENS', 'FONBEAUZARD', 'GAGNACSURGARONNE', 'GRATENTOUR', 'LUNION', 'LABEGE', 'LAUNAGUET', 'LESPINASSE', 'MONDONVILLE', 'MONDOUZIL', 'MONS', 'MONTRABE', 'PIBRAC', 'PINBALMA','QUINTFONSEGRIVES', 'SAINTALBAN', 'SAINTJEAN', 'SAINTJORY', 'SAINTORENSDEGAMEVILLE', 'SAINTREMYDEPROVENCE', 'SEILH', 'TOULOUSE', 'TOURNEFEUILLE', 'VILLENEUVETOLOSANE']
print('Toulouse area count ',len(toulouse_area), ' cities.')

# get datas from each excel sheets
for year in years:
#for year in ['2014']:    
    #load the sheet datas
    df = xl.parse(sheetname=year,skiprows=6)    
    df['city'] = df['NCC'].map(format_city)    
    df = df.set_index('city')
    df.sort_index()
    
    # remove unused columns
    del df['NCC']    
    del df['COM']    
    
    # rename the population count column
    df.columns = ['count']
    
    # keep the series only
    sr = df['count'].map(int)
    
    # remove duplicates
    sr = sr.groupby('city').max()
    sr = sr.filter(items=toulouse_area, axis=0)
    
    # add the new year column
    df_population = pd.DataFrame(sr)    
    df_population['year'] = year    
    
    
    
    if pop_count.empty:
        pop_count = df_population[:]
    else:
        pop_count = pop_count.append(df_population)
        
        
def classify_in_area(city):
    if city == 'TOULOUSE':
        return city
    else:
        return 'AGGLOMERATION'
    
# remove the previous index
pop_count.reset_index(level='city',inplace=True)
pop_count['area'] = pop_count['city'].apply(classify_in_area)

# remove the city column
del pop_count['city']

# calculate the population by areas
pop_count = pop_count.groupby(['area','year']).sum()

# create an index on area and year
#pop_count.set_index(['area','year'],inplace=True)   
pop_count.sort_index(inplace=True)
pop_count.to_csv('pop_count.csv')
print("---------------------------------------------------")
print("     Get the five more populated top cities ")
print("---------------------------------------------------")

#pop_top = pop_count.reset_index(inplace=False)
#del pop_top['year']
#top_cities = list(pop_top.groupby('city')['count'].sum().sort_values(ascending=False)[:5].index)
#print(top_cities)

print("---------------------------------------------------")
print("    Visualize the distribution of the population ")
print("---------------------------------------------------")

for area in ['TOULOUSE', 'AGGLOMERATION']:    
    _ = plt.plot(pop_count.loc[area],label=area)    

plt.legend(loc='lower right')    
plt.show()


    