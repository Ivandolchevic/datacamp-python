'''
Created on Sep 12, 2017

@author: idolchevic
'''
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns
import statfunc.distribution as disfunc

sns.set()
np.random.seed(42)

filesnames = glob.glob("*.tsv")

def explore_file():
    # check file format 
    with open(filesnames[0], 'r', encoding = "ISO-8859-1") as file:
        for _ in range(10):
            print(file.readline())

df = pd.read_csv(filesnames[0],sep='\t')

def explore_dataframe():    
    print('\ndataframe:\n',df.head(),'\nformat:',df.info())

def convert_string_to_float(value):
    return float(str(value).replace(',','.').strip())

def convert_string_to_int(value):
    return int(''.join(re.findall('[0-9]',value)))    

# search results by household individualy in France
df_france = df[df['unit,hhtyp,geo\\time'] == 'PC_HH,A1,FR']

print(df_france) 
