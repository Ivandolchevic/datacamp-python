'''
Created on Aug 14, 2017

@author: idolchevic
'''

import pandas as pd
import matplotlib.pyplot as plt
from calendar import month

print("---------------------------------------------------")
print("    Reading in a data file")
print("---------------------------------------------------")


# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv('data.csv')

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv('data.csv', header=None)

# Print the output of df_headers.head()
print(df_headers.head())


print("---------------------------------------------------")
print("   Re-assigning column names  ")
print("---------------------------------------------------")


# Split on the comma to create a list: column_labels_list
#column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
#df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
#df_dropped = df.drop(list_to_drop, axis='columns')
    
    # Print the output of df_dropped.head()
#print(df_dropped.head())



print("---------------------------------------------------")
print("   Cleaning and tidying datetime data  ")
print("---------------------------------------------------")
df_dropped_columns = ['Wban', 'date', 'Time', 'StationType', 'sky_condition',       'sky_conditionFlag', 'visibility', 'visibilityFlag',       'wx_and_obst_to_vision', 'wx_and_obst_to_visionFlag', 'dry_bulb_faren',       'dry_bulb_farenFlag', 'dry_bulb_cel', 'dry_bulb_celFlag',       'wet_bulb_faren', 'wet_bulb_farenFlag', 'wet_bulb_cel',       'wet_bulb_celFlag', 'dew_point_faren', 'dew_point_farenFlag',       'dew_point_cel', 'dew_point_celFlag', 'relative_humidity',       'relative_humidityFlag', 'wind_speed', 'wind_speedFlag',       'wind_direction', 'wind_directionFlag', 'value_for_wind_character',       'value_for_wind_characterFlag', 'station_pressure',       'station_pressureFlag', 'pressure_tendency', 'pressure_tendencyFlag',       'presschange', 'presschangeFlag', 'sea_level_pressure',       'sea_level_pressureFlag', 'record_type', 'hourly_precip',       'hourly_precipFlag', 'altimeter', 'altimeterFlag', 'junk'] 
df_dropped = pd.read_csv('NOAA_QCLCD_2011_hourly_13904.txt', header=None)

df_dropped.columns = df_dropped_columns
print(df.head())

# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date'] + df_dropped['Time']  

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(df_clean.head())


print("---------------------------------------------------")
print("   Cleaning the numeric columns  ")
print("---------------------------------------------------")

# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-06-20 08:00:00':'2011-06-20 09:00:00', 'dry_bulb_faren'])

# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-06-20 08:00:00':'2011-06-20 09:00:00', 'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')

print(df_clean.head())

print("---------------------------------------------------")
print("  Signal min, max, median   ")
print("---------------------------------------------------")

# Print the median of the dry_bulb_faren column
print(df_clean.dry_bulb_faren.median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-Jan', 'dry_bulb_faren'].median())


print("---------------------------------------------------")
print("    Signal variance ")
print("---------------------------------------------------")

df_climate = pd.read_csv('weather_data_austin_2010.csv',index_col='Date', parse_dates=True)

# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('D').mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index()['Temperature']

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())



print("---------------------------------------------------")
print("  Sunny or cloudy  ")
print("---------------------------------------------------")

# Select days that are sunny: sunny
sunny = df_clean.loc[df_clean['sky_condition'].str.contains('CLR')]

# Select days that are overcast: overcast
overcast = df_clean.loc[df_clean['sky_condition'].str.contains('OVC')]

# Resample sunny and overcast, aggregating by maximum daily temperature
sunny_daily_max = sunny.resample('D').max()
overcast_daily_max = overcast.resample('D').max()

# Print the difference between the mean of sunny_daily_max and overcast_daily_max
print(sunny_daily_max.mean() - overcast_daily_max.mean())



print("---------------------------------------------------")
print("   Weekly average temperature and visibility  ")
print("---------------------------------------------------")

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean.loc[:,['visibility', 'dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()


print("---------------------------------------------------")
print("    Daily hours of clear sky ")
print("---------------------------------------------------")

# Create a Boolean Series for sunny days: sunny
sunny = df_clean['sky_condition'].str.contains('CLR')

# Resample the Boolean Series by day and compute the sum: sunny_hours
sunny_hours = sunny.resample('D').sum()

# Resample the Boolean Series by day and compute the count: total_hours
total_hours = sunny.resample('D').count()

# Divide sunny_hours by total_hours: sunny_fraction
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()


print("---------------------------------------------------")
print("   Heat or humidity ")
print("---------------------------------------------------")

# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean.loc[:,['dew_point_faren', 'dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist', bins=8, alpha=0.5, subplots=True)

# Show the plot
plt.show()


print("---------------------------------------------------")
print("    Probability of high temperatures ")
print("---------------------------------------------------")

# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = df_climate.loc['2010-Aug','Temperature'].max()
print(august_max)

# Resample the August 2011 temperatures in df_clean by day and aggregate the maximum value: august_2011
august_2011 = df_clean.loc['2011-Aug','dry_bulb_faren'].resample('D').max()

# Filter out days in august_2011 where the value exceeded august_max: august_2011_high
august_2011_high = august_2011.loc[august_2011 > august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(kind='hist',bins=25, normed=True,cumulative=True)

# Display the plot
plt.show()
