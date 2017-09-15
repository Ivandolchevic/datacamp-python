'''
Created on Aug 16, 2017

@author: idolchevic
'''

import pandas as pd

filename = 'pennsylvania2012_turnout.csv'
election = pd.read_csv('pennsylvania2012_turnout.csv', index_col=0)
titanic = pd.read_csv('titanic.csv', index_col=0)
weather = pd.read_csv('pittsburgh2013.csv', index_col=0)
print(election.head())

print("---------------------------------------------------")
print("    Index ordering ")
print("---------------------------------------------------")

print(election.loc['Bedford','winner'])



print("---------------------------------------------------")
print("    Index ordering ")
print("---------------------------------------------------")

# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])


print("---------------------------------------------------")
print("    Indexing and column rearrangement ")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total','voters']]

# Print the output of results.head()
print(results.head())



print("---------------------------------------------------")
print("   Slicing rows  ")
print("---------------------------------------------------")

# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter',:]

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry':-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

print("---------------------------------------------------")
print("   Slicing columns  ")
print("---------------------------------------------------")

# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())



print("---------------------------------------------------")
print("    Subselecting DataFrames with lists ")
print("---------------------------------------------------")

# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows, cols]

# Print the three_counties DataFrame
print(three_counties)



print("---------------------------------------------------")
print("    Thresholding data ")
print("---------------------------------------------------")

# Create the boolean array: high_turnout
high_turnout = election.turnout > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)




print("---------------------------------------------------")
print("   Filtering columns using other columns  ")
print("---------------------------------------------------")

# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election.margin < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.winner[too_close] = np.nan

# Print the output of election.info()
print(election.info())



print("---------------------------------------------------")
print("    Filtering using NaNs ")
print("---------------------------------------------------")

# Select the 'age' and 'cabin' columns: df
df = titanic[['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Call .dropna() with thresh=1000 and axis='columns' and print the output of .info() from titanic
print(titanic.dropna(thresh=1000, axis='columns').info())




print("---------------------------------------------------")
print("    Using apply() to transform a column ")
print("---------------------------------------------------")

# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = weather[['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)

# Reassign the columns df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())



print("---------------------------------------------------")
print("   Using .map() with a dictionary  ")
print("---------------------------------------------------")

# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue','Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election.winner.map(red_vs_blue)

# Print the output of election.head()
print(election.head())



print("---------------------------------------------------")
print("   Using vectorized functions  ")
print("---------------------------------------------------")

# Import zscore from scipy.stats
from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore 

# Print the output of election.head()
print(election.head())
