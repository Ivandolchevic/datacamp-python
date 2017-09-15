'''
Created on Sep 5, 2017

@author: idolchevic
'''
import pandas as pd
import numpy as np
import re
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


    
# Import packages
import requests

# Specify url
#url = 'https://www.data.gouv.fr/fr/datasets/open-damir-base-complete-sur-les-depenses-dassurance-maladie-inter-regimes'
url = 'https://www.igdb.com/games/the-witcher-3-wild-hunt/credits'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc,"html.parser")

# Print the title of Guido's webpage
print(soup.title)

div_credits = soup.find(id='credits-employees')

who = ''
what = ''
team = ''
    
df_thewitcher3 = pd.DataFrame()
    
for row in div_credits.find_all('tr'):        
    who = ''
    what = ''
    try:
        who = row.find('td').find('a').get_text()
        what = row.find_all('td')[1].get_text()
    except AttributeError:
        None
    except IndexError:
        team = row.find('td').get_text()
    
    if (who != '') & (what != ''):
        dict_row = {'team':team,'who':who, 'what':what}
        df_row = pd.DataFrame([dict_row],dict_row.keys())        
        df_thewitcher3 = df_thewitcher3.append(df_row)
    

df_thewitcher3.reset_index(inplace=True)
print(df_thewitcher3)

# get total count
total_count = df_thewitcher3.count()

# get count of teams 
team_count = len(df_thewitcher3.team.unique())

# get role count
job_count = len(df_thewitcher3.what.unique()) 

print('\ntotal_count:',total_count,'\nteam_count:',team_count,'\njob_count:',job_count)

