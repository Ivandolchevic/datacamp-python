'''
Created on Aug 14, 2017

@author: idolchevic
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("---------------------------------------------------")
print("     Reading and slicing times")
print("---------------------------------------------------")

filename = 'weather_data_austin_2010.csv'
df1 = pd.read_csv(filename)
df2 = pd.read_csv(filename, parse_dates=['Date'])
df3 = pd.read_csv(filename, index_col='Date', parse_dates=True)

print('\ndf1\n',df1.head(),'\n\nInformations\n',df1.info())
print('\ndf2\n',df2.head(),'\n\nInformations\n',df2.info())
print('\ndf3\n',df3.head(),'\n\nInformations\n',df3.info())

print(df3.loc['2010-Aug-01'])

print("---------------------------------------------------")
print("     Creating and using a DatetimeIndex ")
print("---------------------------------------------------")

date_list = pd.read_csv(filename)['Date']
temperature_list = pd.read_csv(filename, index_col='Date', parse_dates=True)['Temperature']

# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list , format=time_format)  

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list,index=my_datetimes)

ts0 = time_series

print("---------------------------------------------------")
print("     Partial string indexing and slicing ")
print("---------------------------------------------------")

# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']
print(ts2.head(10))

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['12/15/2010':'12/31/2010']

print(ts3.head(10))

print("---------------------------------------------------")
print("    Reindexing the Index  ")
print("---------------------------------------------------")

ts1_array = [['2016-07-01',0],['2016-07-02',1],['2016-07-03',2],['2016-07-04',3],['2016-07-05',4],['2016-07-06',5],['2016-07-07',6],['2016-07-08',7],['2016-07-09',8],['2016-07-10',9],['2016-07-11',10],['2016-07-12',11],['2016-07-13',12],['2016-07-14',13],['2016-07-15',14],['2016-07-16',15],['2016-07-17',16]]

keys = pd.to_datetime(pd.DataFrame(ts1_array)[0].values)
values = pd.DataFrame(ts1_array)[1].values
ts1 = pd.Series(values,index=keys)

# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index,method="ffill")

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4

print(sum12)
print(sum13)
print(sum14)

print("---------------------------------------------------")
print("     Resampling and frequency ")
print("---------------------------------------------------")

df = pd.read_csv(filename, index_col='Date', parse_dates=True)

# Downsample to 6 hour data and aggregate by mean: df1
df1 = df.Temperature.resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df.Temperature.resample('D').count()

print("df1 resampling => ",df1)
print("\n\ndf2 resampling => ",df2)


print("---------------------------------------------------")
print("    Separating and resampling  ")
print("---------------------------------------------------")

# Extract temperature data for August: august
august = df['August 2010']['Temperature']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['February 2010']['Temperature']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

print(february_lows)
print("---------------------------------------------------")
print("     Rolling mean and frequency ")
print("---------------------------------------------------")


# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()


print("---------------------------------------------------")
print("    Resample and roll with it ")
print("---------------------------------------------------")

# Extract the August 2010 data: august
august = df['Temperature']['August 2010']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)




print("---------------------------------------------------")
print("     Method chaining and filtering ")
print("---------------------------------------------------")

df = pd.read_csv('austin_airport_departure_data_2015_july.csv',skiprows=14,index_col='Date (MM/DD/YYYY)', parse_dates=True,keep_default_na=False)

# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()
print(stats)




print("---------------------------------------------------")
print("   Missing values and interpolation  ")
print("---------------------------------------------------")

ts1_array = [['2016-07-01',0],['2016-07-02',1],['2016-07-03',2],['2016-07-04',3],['2016-07-05',4],['2016-07-06',5],['2016-07-07',6],['2016-07-08',7],['2016-07-09',8],['2016-07-10',9],['2016-07-11',10],['2016-07-12',11],['2016-07-13',12],['2016-07-14',13],['2016-07-15',14],['2016-07-16',15],['2016-07-17',16]]
ts2_array = [['2016-07-01',0],['2016-07-04',1],['2016-07-05',2],['2016-07-06',3],['2016-07-07',4],['2016-07-08',5],['2016-07-11',6],['2016-07-12',7],['2016-07-13',8],['2016-07-14',9],['2016-07-15',10]]

keys = pd.to_datetime(pd.DataFrame(ts1_array)[0].values)
values = pd.DataFrame(ts1_array)[1].values
ts1 = pd.Series(values,index=keys)

keys = pd.to_datetime(pd.DataFrame(ts2_array)[0].values)
values = pd.DataFrame(ts2_array)[1].values
ts2 = pd.Series(values,index=keys)

# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = np.abs(ts1 -ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())



print("---------------------------------------------------")
print("     Time zones and conversion ")
print("---------------------------------------------------")
df = pd.read_csv('austin_airport_departure_data_2015_july.csv',skiprows=14, parse_dates=True,keep_default_na=False)
df.columns = df.columns.str.strip()

# Buid a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime(la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'])

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

print("---------------------------------------------------")
print("      ")
print("---------------------------------------------------")

df = pd.read_csv('weather_data_austin_2010.csv',usecols=['Temperature','Date'])

# Plot the raw data before setting the datetime index
df.plot()
plt.show()

# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date)

# Set the index to be the converted 'Date' column
df.set_index('Date',inplace=True)

# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()


print("---------------------------------------------------")
print("     Plotting date ranges, partial indexing ")
print("---------------------------------------------------")

# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].rolling(window=96).mean().plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].rolling(window=24).mean().plot()
plt.show()
plt.clf()



