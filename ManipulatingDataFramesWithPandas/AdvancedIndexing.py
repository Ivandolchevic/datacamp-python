'''
Created on Aug 17, 2017

@author: idolchevic
'''

import pandas as pd

sales = pd.read_csv('sales.csv', index_col=0)

print("---------------------------------------------------")
print("   Changing index of a DataFrame ")
print("---------------------------------------------------")

# Create the list of new indexes: new_idx
new_idx = [sale.upper() for sale in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

print("---------------------------------------------------")
print("   Changing index name labels ")
print("---------------------------------------------------")

# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)


print("---------------------------------------------------")
print("    Building an index, then a DataFrame")
print("---------------------------------------------------")

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)


print("---------------------------------------------------")
print("  Extracting data with a MultiIndex ")
print("---------------------------------------------------")

sales = pd.read_csv('sales_multiindex.csv',index_col=['state','month'])

# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales['CA':'TX'])



print("---------------------------------------------------")
print("   Setting & sorting a MultiIndex ")
print("---------------------------------------------------")

sales = pd.read_csv('sales_multiindex.csv',index_col=None)

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)


print("---------------------------------------------------")
print("   Using .loc[] with nonunique indexes ")
print("---------------------------------------------------")

sales = pd.read_csv('sales_multiindex.csv',index_col=None)

# Set the index to the column 'state': sales
sales = sales.set_index('state')

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])


print("---------------------------------------------------")
print("   Indexing multiple levels of a MultiIndex ")
print("---------------------------------------------------")

sales = pd.read_csv('sales_multiindex.csv',index_col=['state','month'])

# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY',1),:]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(('CA','TX'),2),:]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None),2),:]

print('\n',NY_month1)
print('\n',CA_TX_month2)
print('\n',all_month2)
print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")


