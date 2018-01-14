'''
Created on Sep 5, 2017

@author: idolchevic
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns


df_cies_count = pd.read_csv('cies_count.csv', index_col=[0,1])


# get all areas
all_areas = list(df_cies_count.index.get_level_values('area').unique())

# get all years since 1968 to 2016
all_years_since_1968 = [year for year in range(1968,2017)]

# build the [area,year] array
dict_areas_and_years = [[a,y] for a in all_areas for y in all_years_since_1968]

# initialize the dataframe
df_all_areas_and_years = pd.DataFrame(dict_areas_and_years, columns=['area','year'])

# add count column
df_all_areas_and_years['count'] = 0

# remove the current index
df_all_areas_and_years.set_index(['area','year'],inplace=True)
df_all_areas_and_years.sort_index()

# prepare pop_count dataframe for the merge operation 
df_cies_count.sort_index()

# merge the dataframes
df_tobesmoothed = df_all_areas_and_years.join(other=df_cies_count, lsuffix='_all',rsuffix='_calculated',how='left')

# convert the population count to integer
df_tobesmoothed['count'] = df_tobesmoothed['count_calculated'] 

# remove unused columns
del df_tobesmoothed['count_calculated']
del df_tobesmoothed['count_all']

# interpolate
df_smoothed = df_tobesmoothed.interpolate(how='slinear',axis=0)
df_smoothed['count'] = df_smoothed['count'].map(int) 

df_smoothed.to_csv('cies_count_smoothed.csv')



