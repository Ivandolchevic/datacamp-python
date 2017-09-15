'''
Created on Sep 1, 2017

@author: idolchevic
'''
import numpy as np
import pandas as pd
import re


def get_special_char_count(line):
    '''Get the count of special chars into a row'''
    return {char:line.count(char) for char in ''.join(set(line)) if re.compile('[;|,|\t|\s{4,6}]').match(char)}

def get_column_separator(file,n=20):
    '''Get the count of special chars of each first n rows '''
    # initialize the special char count array
    counts = {}
    
    # for each line
    for i in range(n):
        line = file.readline()
        counts[i] = get_special_char_count(line)
            
    return pd.DataFrame(counts)


#check file format
with open('fr-esr-insertion_professionnelle-master.csv') as file:
    df_counts = get_column_separator(file)
    df_counts.index.name = 'char'

print(df_counts.unstack(level='char').groupby('char').mean())