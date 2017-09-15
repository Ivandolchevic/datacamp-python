'''
Created on Aug 17, 2017

@author: idolchevic
'''

import pandas as pd
from pandas.compat import parse_date

titanic = pd.read_csv('titanic.csv', index_col=0)

print("---------------------------------------------------")
print("   Grouping by multiple columns  ")
print("---------------------------------------------------")

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)

life_fname = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1650/datasets/life_expectancy.csv'
regions_fname = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1650/datasets/regions.csv'

print("---------------------------------------------------")
print("    Grouping by another series ")
print("---------------------------------------------------")

# Read life_fname into a DataFrame: life
# life = pd.read_csv(life_fname, index_col='Country')

# Read regions_fname into a DataFrame: regions
# regions = pd.read_csv(regions_fname, index_col='Country')

# Group life by regions['region']: life_by_region
# life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
# print(life_by_region['2010'].mean())


print("---------------------------------------------------")
print("   Computing multiple aggregates of multiple columns  ")
print("---------------------------------------------------")

# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:, ('fare','median')])


print("---------------------------------------------------")
print("    Aggregating on index levels/fields ")
print("---------------------------------------------------")

# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder_tidy.csv', index_col=['Year','region','Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level=['Year','region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))


print("---------------------------------------------------")
print("    Grouping on a function of the index ")
print("---------------------------------------------------")

# Read file: sales
sales = pd.read_csv('sales-feb-2015.csv', index_col='Date',parse_dates=True)

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)



print("---------------------------------------------------")
print("    Detecting outliers with Z-Scores ")
print("---------------------------------------------------")


gapminder_2010 = gapminder.loc[2010]

# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)



print("---------------------------------------------------")
print("    Filling missing data (imputation) by group ")
print("---------------------------------------------------")

# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex','pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class.age.transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))


print("---------------------------------------------------")
print("    Other transformations with .apply ")
print("---------------------------------------------------")

gapminder = pd.read_csv('gapminder_tidy.csv', index_col='Country').sort_index()
year_2010 = gapminder.Year == 2010
gapminder_2010 = gapminder[year_2010]

def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States', 'United Kingdom', 'China']])

print("---------------------------------------------------")
print("    Grouping and filtering with .apply() ")
print("---------------------------------------------------")

def c_deck_survival(gr):

    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()

# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival and print the result
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)


print("---------------------------------------------------")
print("   Grouping and filtering with .filter() ")
print("---------------------------------------------------")

# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales-feb-2015.csv', index_col='Date',parse_dates=True)

# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(by_com_filt)


print("---------------------------------------------------")
print("   Filtering and grouping with .map()  ")
print("---------------------------------------------------")

# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10,'pclass'])['survived'].mean()
print(survived_mean_2)


