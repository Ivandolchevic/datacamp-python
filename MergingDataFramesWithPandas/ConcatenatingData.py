'''
Created on Aug 18, 2017

@author: idolchevic
'''
'''
Created on Aug 18, 2017

@author: idolchevic
'''

import pandas as pd

print("---------------------------------------------------")
print("   Appending Series with nonunique Indices  ")
print("---------------------------------------------------")

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv', index_col='Country')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv', index_col='Country')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv', index_col='Country')

combined = bronze.append(silver)

print(len(combined))
print(combined.loc['United States'])

print("---------------------------------------------------")
print("   Appending pandas Series  ")
print("---------------------------------------------------")

# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv',index_col='Date',parse_dates=True)

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv',index_col='Date',parse_dates=True)

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv',index_col='Date',parse_dates=True)

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])


# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())

print("---------------------------------------------------")
print("   Concatenating pandas Series along row axis  ")
print("---------------------------------------------------")

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units,axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])



print("---------------------------------------------------")
print("    Appending DataFrames with ignore_index ")
print("---------------------------------------------------")

names_1881 = pd.read_csv('names1881.csv',names=['name','gender','count'])
names_1981 = pd.read_csv('names1981.csv',names=['name','gender','count'])

# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981,ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names.name == 'Morgan'])


print("---------------------------------------------------")
print("   Concatenating pandas DataFrames along column axis  ")
print("---------------------------------------------------")

weather_max = pd.DataFrame([[68],[89],[91],[84]],index=['Jan','Apr','Jul','Oct'],columns=['Max TemperatureF'])
weather_max.index.name = 'Month'

weather_mean = pd.DataFrame([[53.100000],[70.000000],[34.935484],[28.714286],[32.354839],[72.870968],[70.133333],[35.000000],[62.612903],[39.800000],[55.451613],[63.766667]],index=['Apr','Aug','Dec','Feb','Jan','Jul','Jun','Mar','May','Nov','Oct','Sep'],columns=['Mean TemperatureF'])
weather_mean.index.name = 'Month'

# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max, weather_mean], axis=1)
# Print weather
print(weather)

print("---------------------------------------------------")
print("    Reading multiple files to build a DataFrame ")
print("---------------------------------------------------")
medals = []
medal_types = ['bronze', 'silver', 'gold']
for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name,header=0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis='columns')

# Print medals
print(medals)

print("---------------------------------------------------")
print("    Concatenating vertically to get MultiIndexed rows ")
print("---------------------------------------------------")

medals=[]

for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)

print("---------------------------------------------------")
print("    Slicing MultiIndexed DataFrames ")
print("---------------------------------------------------")

# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'],:])



print("---------------------------------------------------")
print("   Concatenating horizontally to get MultiIndexed columns  ")
print("---------------------------------------------------")

dataframes = []
sales_types = ['Service','Hardware','Software']

for sales in sales_types:

    file_name = "feb-sales-%s.csv" % sales
    
    # Read file_name into a DataFrame: medal_df
    sales_df = pd.read_csv(file_name, index_col='Date',parse_dates=True)
    
    # Append medal_df to medals
    dataframes.append(sales_df)

# Concatenate dataframes: february
february = pd.concat(dataframes, keys=['Hardware', 'Software', 'Service'],axis=1)

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb. 2, 2015':'Feb. 8, 2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)


print("---------------------------------------------------")
print("    Concatenating DataFrames from a dict ")
print("---------------------------------------------------")

jan = pd.read_csv('sales-jan-2015.csv',index_col=0)
feb = pd.read_csv('sales-feb-2015.csv',index_col=0)
mar = pd.read_csv('sales-mar-2015.csv',index_col=0)


# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb),  ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])


print("---------------------------------------------------")
print("    Concatenating DataFrames with inner join ")
print("---------------------------------------------------")

# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list,keys=['bronze', 'silver','gold'],axis=1,join='inner') 

# Print medals
print(medals)


print("---------------------------------------------------")
print("    Resampling & concatenating DataFrames with inner join ")
print("---------------------------------------------------")

china = pd.read_csv('gdp_china.csv',index_col='Year',header=None,skiprows=1,parse_dates=True,names=['Year','China'])
usa = pd.read_csv('gdp_usa.csv',index_col='Year',header=None,skiprows=1,parse_dates=True,names=['Year','US'])


# Resample and tidy china: china_annual
china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = usa.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],join='inner',axis=1)

# Resample gdp and print
print(gdp.resample('10A').last())
