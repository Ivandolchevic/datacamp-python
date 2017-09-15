'''
Created on Aug 11, 2017

@author: idolchevic
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv

df = pd.read_csv('yahoo_financial.csv',sep=';')


print("---------------------------------------------------")
print("     pandas line plots")
print("---------------------------------------------------")

# Create a list of y-axis column names: y_columns
#y_columns = ['AAPL','IBM']

# Generate a line plot
#df.plot(x='Month',y=y_columns)

# Add the title
#plt.title('Monthly stock prices')

# Add the y-axis label
#plt.ylabel('Price ($US)')

# Display the plot
#plt.show()
df = pd.read_csv('auto-mpg.csv')

sizes=np.array([51.12044694,56.78387977,49.15557238,49.06977358,49.52823321,78.4595872,78.93021696,77.41479205,81.52541106,61.71459825,52.85646225,54.23007578,58.89427963,39.65137852,23.42587473,33.41639502,32.03903011,27.8650165,18.88972581,14.0196956,29.72619722,24.58549713,23.48516821,20.77938954,29.19459189,88.67676838,79.72987328,79.94866084,93.23005042,18.88972581,21.34122243,20.6679223,28.88670381,49.24144612,46.14174741,45.39631334,45.01218186,73.76057586,82.96880195,71.84547684,69.85320595,102.22421043,93.78252358,110.,36.52889673,24.14234281,44.84805372,41.02504618,20.51976563,18.765772,17.9095202,17.75442285,13.08832041,10.83266174,14.00441945,15.91328975,21.60597587,18.8188451,21.15311208,24.14234281,20.63083317,76.05635059,80.05816704,71.18975117,70.98330444,56.13992036,89.36985382,84.38736544,82.6716892,81.4149056,22.60363518,63.06844313,69.92143863,76.76982089,69.2066568,35.81711267,26.25184749,36.94940537,19.95069229,23.88237331,21.79608472,26.1474042,19.49759118,18.36136808,69.98970461,56.13992036,66.21810474,68.02351436,59.39644014,102.10046481,82.96880195,79.25686195,74.74521151,93.34830013,102.05923292,60.7883734,40.55589449,44.7388015,36.11079464,37.9986264,35.11233175,15.83199594,103.96451839,100.21241654,90.18186347,84.27493641,32.38645967,21.62494928,24.00218436,23.56434276,18.78345471,22.21725537,25.44271071,21.36007926,69.37650986,76.19877818,14.51292942,19.38962134,27.75740889,34.24717407,48.10262495,29.459795,32.80584831,55.89556844,40.06360581,35.03982309,46.33599903,15.83199594,25.01226779,14.03498009,26.90404245,59.52231336,54.92349014,54.35035315,71.39649768,91.93424995,82.70879915,89.56285636,75.45251972,20.50128352,16.04379287,22.02531454,11.32159874,16.70430249,18.80114574,18.50153068,21.00322336,25.79385418,23.80266582,16.65430211,44.35746794,49.815853,49.04119063,41.52318884,90.72524338,82.07906251,84.23747672,90.29816462,63.55551901,63.23059357,57.92740995,59.64831981,38.45278922,43.19643409,41.81296121,19.62393488,28.99647648,35.35456858,27.97283229,30.39744886,20.57526193,26.96758278,37.07354237,15.62160631,42.92863291,30.21771564,36.40567571,36.11079464,29.70395123,13.41514444,25.27829944,20.51976563,27.54281821,21.17188565,20.18836167,73.97101962,73.09614831,65.35749368,73.97101962,43.51889468,46.80945169,37.77255674,39.6256851,17.24230306,19.49759118,15.62160631,13.41514444,55.49963323,53.18333207,55.31736854,42.44868923,13.86730874,16.48817545,19.33574884,27.3931002,41.31307817,64.63368105,44.52069676,35.74387954,60.75655952,79.87569835,68.46177648,62.35745431,58.70651902,17.41217694,19.33574884,13.86730874,22.02531454,15.75091031,62.68013142,68.63071356,71.36201911,76.80558184,51.58836621,48.84134317,54.86301837,51.73502816,74.14661842,72.22648148,77.88228247,78.24284811,15.67003285,31.25845963,21.36007926,31.60164234,17.51450098,17.92679488,16.40542438,19.96892459,32.99310928,28.14577056,30.80379718,16.40542438,13.48998471,16.40542438,17.84050478,13.48998471,47.1451025,58.08281541,53.06435374,52.02897659,41.44433489,36.60292926,30.80379718,48.98404972,42.90189859,47.56635225,39.24128299,54.56115914,48.41447259,48.84134317,49.41341845,42.76835191,69.30854366,19.33574884,27.28640858,22.02531454,20.70504474,26.33555201,31.37264569,33.93740821,24.08222494,33.34566004,41.05118927,32.52595611,48.41447259,16.48817545,18.97851406,43.84255439,37.22278157,34.77459916,44.38465193,47.00510227,61.39441929,57.77221268,65.12675249,61.07507305,79.14790534,68.42801405,54.10993164,64.63368105,15.42864956,16.24054679,15.26876826,29.68171358,51.88189829,63.32798377,42.36896092,48.6988448,20.15170555,19.24612787,16.98905358,18.88972581,29.68171358,28.03762169,30.35246559,27.20120517,19.13885751,16.12562794,18.71277385,16.9722369,29.85984799,34.29495526,37.54716158,47.59450219,19.93246832,30.60028577,26.90404245,24.66650366,21.36007926,18.5366546,32.64243213,18.5366546,18.09999962,22.70075058,36.23351603,43.97776651,14.24983724,19.15671509,14.17291518,35.25757392,24.38356372,26.02234705,21.83420642,25.81458463,28.90864169,28.58044785,30.91715052,23.6833544,12.82391671,14.63757021,12.89709155,17.75442285,16.24054679,17.49742615,16.40542438,20.42743834,17.41217694,23.58415722,19.96892459,20.33531923,22.99334585,28.47146626,28.90864169,43.43816712,41.57579979,35.01567018,35.74387954,48.5565546,57.77221268,38.98605581,49.98882458,28.25412762,29.01845599,23.88237331,27.60710798,26.54539622,31.14448175,34.17556473,16.3228815,17.0732619,16.15842026,18.80114574,18.80114574,19.42557798,20.2434083,20.98452475,16.07650192,16.07650192,16.57113469,36.11079464,37.84783835,27.82194848,33.46359332,29.5706502,23.38638738,36.23351603,32.40968826,18.88972581,21.92965639,28.68963762,30.80379718])
print("---------------------------------------------------")
print("   pandas scatter plots  ")
print("---------------------------------------------------")

# Generate a scatter plot
#df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
#plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
#plt.xlabel('Horse-power')

# Add the y-axis label
#plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
#plt.show()


print("---------------------------------------------------")
print("   pandas box plots  ")
print("---------------------------------------------------")

# Make a list of the column names to be plotted: cols
#cols = ['weight', 'mpg']

# Generate the box plots
#df[cols].plot(kind='box',subplots=True)

# Display the plot
#plt.show()

#df = pd.read_csv('tips.csv')

print("---------------------------------------------------")
print("   pandas hist, pdf and cdf  ")
print("---------------------------------------------------")

# This formats the plots such that they appear on separate rows
#fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
#df.fraction.plot(ax=axes[0], kind='hist', bins=30, normed=True, range=(0,.3))
#plt.show()

# Plot the CDF
#df.fraction.plot(ax=axes[1], kind='hist',bins=30, normed=True, cumulative=True, range=(0,.3))
#plt.show()



print("---------------------------------------------------")
print("    Fuel efficiency ")
print("---------------------------------------------------")

print(df.mpg.median())

df = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

print("---------------------------------------------------")
print("  Bachelor's degrees awarded to women   ")
print("---------------------------------------------------")

# Print the minimum value of the Engineering column
print(df.Engineering.min())

# Print the maximum value of the Engineering column
print(df.Engineering.max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()

df = pd.read_csv('titanic.csv')

print("---------------------------------------------------")
print("     Median vs mean")
print("---------------------------------------------------")

# Print summary statistics of the fare column with .describe()
print(df.fare.describe())

# Generate a box plot of the fare column
df.fare.plot(kind='box')

# Show the plot
plt.show()

df = pd.read_csv('life_expectancy_at_birth.csv')

print("---------------------------------------------------")
print("   Quantiles  ")
print("---------------------------------------------------")

# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05,0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()

print("---------------------------------------------------")
print("   Standard deviation of temperature")
print("---------------------------------------------------")

df = pd.read_csv('weather_data_austin_2010.csv',parse_dates=['Date'])

january = df[(df['Date'] > '2010-01-01') & (df['Date'] < '2010-02-01')].loc[:,['Date','Temperature']]
march = df[(df['Date'] > '2010-03-01') & (df['Date'] < '2010-04-01')].loc[:,['Temperature','Date']]

# Print the mean of the January and March data
print(january.mean(),march.mean())

# Print the standard deviation of the January and March data
print(january.std(),march.std())


print("---------------------------------------------------")
print("   Filtering and counting")
print("---------------------------------------------------")

df = pd.read_csv('auto-mpg.csv')

asian_cars = df[df.origin == 'Asia']
us_cars = df[df.origin == 'US']

print("ASIAN CARS", asian_cars.describe())
print("\nUS CARS", us_cars.describe())

print("---------------------------------------------------")
print("  Separate and summarize ")
print("---------------------------------------------------")

# Compute the global mean and global standard deviation: global_mean, global_std
global_mean = df.mean()
global_std = df.std()

# Filter the US population from the origin column: us
us = df[df.origin == 'US']

# Compute the US mean and US standard deviation: us_mean, us_std
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean - global_mean)
print(us_std - global_std)


print("---------------------------------------------------")
print("  Separate and plot ")
print("---------------------------------------------------")

titanic = pd.read_csv('titanic.csv')

# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')

# Display the plot
plt.show()





