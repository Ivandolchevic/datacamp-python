'''
Created on Aug 18, 2017

@author: idolchevic
'''
'''
Created on Aug 18, 2017

@author: idolchevic
'''
print("---------------------------------------------------")
print("    Loading Olympic edition DataFrame ")
print("---------------------------------------------------")

#Import pandas
import pandas as pd

# Create file path: file_path
file_path = 'Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path, sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City',  'Country']]

# Print editions DataFrame
print(editions)

print("---------------------------------------------------")
print("   Loading IOC codes DataFrame  ")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Create the file path: file_path
file_path = 'Summer Olympic medalists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country','NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())

print("---------------------------------------------------")
print("    Building medals DataFrame ")
print("---------------------------------------------------")

import numpy as np

summer = pd.read_csv('Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv',sep='\t',skiprows=4)
for year in np.nditer(summer.Edition.unique()):
    filename = 'summer_%s.csv' % year
    summer.loc[summer.Edition == year].to_csv(filename)

# Import pandas
import pandas as pd

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:

    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)
    
    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)
    
    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]
    
    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year
    
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict,ignore_index=True)

# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())

print("---------------------------------------------------")
print("    Counting medals by country/edition in a pivot table ")
print("---------------------------------------------------")

# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition',columns='NOC', values='Athlete', aggfunc='count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())

print("---------------------------------------------------")
print("   Computing fraction of medals per Olympic edition ")
print("---------------------------------------------------")

# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']
print(totals)
# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals,axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())

print("---------------------------------------------------")
print("   Computing percentage change in fraction of medals won  ")
print("---------------------------------------------------")

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change() * 100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())

print("---------------------------------------------------")
print("    Building hosts DataFrame ")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, ioc_codes, how='left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition','NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)

print("---------------------------------------------------")
print("    Reshaping for analysis ")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped.loc[reshaped['NOC'] == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())

print("---------------------------------------------------")
print("    Merging to compute influence ")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts,how='inner')

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())

print("---------------------------------------------------")
print("    Plotting influence of host country ")
print("---------------------------------------------------")

# Import pyplot
import matplotlib.pyplot as plt

# Extract influence['Change']: change
change = influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()
