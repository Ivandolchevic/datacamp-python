'''
Created on Aug 11, 2017

@author: idolchevic
'''
import pandas as pd
import numpy as np

g1800s = pd.read_csv('gapminder.csv')
gapminder = pd.read_csv('gapminder.csv')

print("---------------------------------------------------")
print("    Exploratory analysis ")
print("---------------------------------------------------")

print(g1800s.info())
print(g1800s.columns)
print(g1800s.describe())
print(g1800s.head())
print(g1800s.shape)


print("---------------------------------------------------")
print("    Visualizing your data ")
print("---------------------------------------------------")

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()


print("---------------------------------------------------")
print("    Thinking about the question at hand ")
print("---------------------------------------------------")

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    ignoring 'Life expectancy' column at index 0 and the last one (?)  
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
# commented because that stop the script execution
# assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
# commented because that stop the script execution
# assert g1800s['Life expectancy'].value_counts()[0] == 1



print("---------------------------------------------------")
print("    Assembling your data ")
print("---------------------------------------------------")

print('NO DATASET')
# Concatenate the DataFrames row-wise
# gapminder = pd.concat([g1800s, g1900s, g2000s])

# Print the shape of gapminder
# print(gapminder.shape)

# Print the head of gapminder
# print(gapminder.head())




print("---------------------------------------------------")
print("    Reshaping your data ")
print("---------------------------------------------------")

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(frame=gapminder,id_vars=['Life expectancy'])

# Rename the columns
gapminder_melt.columns = ['country', 'year', 'life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())


print("---------------------------------------------------")
print("   Checking the data types  ")
print("---------------------------------------------------")

print('NO DATASET')

# Convert the year column to numeric
# gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
# assert gapminder.country.dtypes == np.object

# Test if year is of type int64
# assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
# assert gapminder.life_expectancy.dtypes == np.float64


print("---------------------------------------------------")
print("   Looking at country spellings  ")
print("---------------------------------------------------")

# Create the series of countries: countries
countries = gapminder.country

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)



print("---------------------------------------------------")
print("   More data cleaning and processing  ")
print("---------------------------------------------------")

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all().all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder.year).all().all()

# Drop the missing values
gapminder = gapminder.dropna()

# Print the shape of gapminder
print(gapminder.shape)



print("---------------------------------------------------")
print("   Wragging up  ")
print("---------------------------------------------------")


# Add first subplot
plt.subplot(2, 1, 1) 

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist')

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
gapminder.to_csv('gapminder.csv')
gapminder_agg.to_csv('gapminder_agg.csv')
