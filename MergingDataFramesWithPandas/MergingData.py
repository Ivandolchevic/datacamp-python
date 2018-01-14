'''
Created on Aug 18, 2017

@author: idolchevic
'''
from unittest.mock import inplace
'''
Created on Aug 18, 2017

@author: idolchevic
'''

import pandas as pd

print("---------------------------------------------------")
print("    Merging company DataFrames ")
print("---------------------------------------------------")

revenue = pd.DataFrame([['Austin',100],['Denver',83],['Springfield',4]], columns=['city','revenue'])
managers = pd.DataFrame([['Austin','Charlers'],['Denver','Joel'],['Mendocino','Brett']],columns=['city','manager'])

combined = pd.merge(revenue, managers, on='city')
print(combined)

print("---------------------------------------------------")
print("   Merging on a specific column  ")
print("---------------------------------------------------")

revenue.loc[len(revenue)] = ['Mendocino',200]
revenue['branch_id'] = [10,20,30,47]

managers.loc[len(managers)] = ['Springfield','Sally']
managers['branch_id'] = [10,20,47,31]

print(managers)


# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)

print("---------------------------------------------------")
print("   Merging on columns with non-matching labels  ")
print("---------------------------------------------------")

revenue['state'] = ['TX','CO','IL','CA']
managers['state'] = ['TX','CO','CA','MO']
managers = managers.rename(columns={'city': 'branch'})


# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, left_on='city',right_on='branch')

# Print combined
print(combined)

del revenue['state']
del managers['state']
managers = managers.rename(columns={'branch': 'city'})

print("---------------------------------------------------")
print("   Merging on multiple columns  ")
print("---------------------------------------------------")

# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['city','branch_id','state'])

# Print combined
print(combined)

print("---------------------------------------------------")
print("    Joining by Index ")
print("---------------------------------------------------")

revenue_values = [['Austin', 100, 'TX'], ['Denver', 83, 'CO'], ['Springfield', 4, 'IL'], ['Mendocino', 200, 'CA']]
managers_values = [['Austin', 'Charlers', 'TX'], ['Denver', 'Joel', 'CO'], ['Mendocino', 'Brett', 'CA'], ['Springfield', 'Sally', 'MO']]
revenue_index = [10, 20, 30, 47]
managers_index =   [10, 20, 47, 31]


revenue = pd.DataFrame(data=revenue_values, index=revenue_index,columns=['city','revenue','state'])
revenue.index.name = 'branch_id'
managers = pd.DataFrame(data=managers_values, index=managers_index,columns=['branch','manager','state'])
managers.index.name = 'branch_id'

#print("\n\npd.merge(revenue, managers, on='branch_id')\n", pd.merge(revenue, managers, on='branch_id'))
print("\n\npd.merge(managers, revenue, how='left').\n", pd.merge(managers, revenue, how='left'))
print("\n\nrevenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer')\n", revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer'))
print("\n\nmanagers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left')\n", managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left') )     


print("---------------------------------------------------")
print("    Choosing a joining strategy ")
print("---------------------------------------------------")

print('Simple question')

print("---------------------------------------------------")
print("   Left & right merging on multiple columns  ")
print("---------------------------------------------------")

print(revenue.reset_index(level=0))
print(managers.reset_index(level=0))

sales_values = [['Mendocino', 'CA', 1], ['Denver', 'CO', 4], ['Austin', 'TX', 2], ['Springfield', 'MO', 5], ['Springfield', 'IL', 1]]
sales = pd.DataFrame(data=sales_values,columns=['city','state','units'])

print(sales)

# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales,how='right',on=['city','state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, how='left',left_on=['city','state'],right_on=['branch','state'])

# Print sales_and_managers
print(sales_and_managers)

print("---------------------------------------------------")
print("   Merging DataFrames with outer join  ")
print("---------------------------------------------------")

# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers, revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers, revenue_and_sales,how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales,how='outer', on=['city','state'])

# Print merge_outer_on
print(merge_outer_on)

print("---------------------------------------------------")
print("   Using merge_ordered()  ")
print("---------------------------------------------------")
from dateutil import parser

austin_values=  [[parser.parse('2016-01-01 00:00:00'), 'Cloudy'], [parser.parse('2016-02-08 00:00:00'), 'Cloudy'], [parser.parse('2016-01-17 00:00:00'), 'Sunny']]
houston_values = [[parser.parse('2016-01-04 00:00:00'), 'Rainy'], [parser.parse('2016-01-01 00:00:00'), 'Cloudy'], [parser.parse('2016-03-01 00:00:00'), 'Sunny']]

austin = pd.DataFrame(austin_values, columns=['date','ratings'])
houston = pd.DataFrame(houston_values, columns=['date','ratings'])

# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin, houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin, houston,on='date', suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin, houston,on='date', suffixes=['_aus','_hus'],fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)

print("---------------------------------------------------")
print("   Using merge_asof()  ")
print("---------------------------------------------------")

auto = pd.read_csv('automobiles.csv',parse_dates=['yr'])
oil = pd.read_csv('oil_price.csv',parse_dates=['Date'])

# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr',right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# print yearly.corr()
print(yearly.corr())
