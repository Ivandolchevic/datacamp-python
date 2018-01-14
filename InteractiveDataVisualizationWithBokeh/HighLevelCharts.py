'''
Created on Sep 12, 2017

@author: idolchevic
'''

import pandas as pd
import toolbox

df = pd.read_csv('literacy_birth_rate.csv')
df.columns = ['Country', 'Continent', 'female_literacy', 'fertility', 'population']
df['female_literacy'] = df['female_literacy'].map(toolbox.convert_string_to_float)
df['fertility'] = df['fertility'].map(toolbox.convert_string_to_float)

print("---------------------------------------------------")
print("  A basic histogram  ")
print("---------------------------------------------------")

# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram, output_file, show

# Make a Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy')

# Set the x axis label
p.xaxis.axis_label = 'female literacy'

# Set the y axis label
p.yaxis.axis_label = 'count of female literacy'

# Specify the name of the output_file and show the result
output_file('histogram.html')
p.show()

print("---------------------------------------------------")
print("   Controlling the number of bins ")
print("---------------------------------------------------")
# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram, output_file, show

# Make the Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy', bins=40)

# Set axis labels
p.xaxis.axis_label = 'Female Literacy (% population)'
p.yaxis.axis_label = 'Number of Countries'

# Specify the name of the output_file and show the result
output_file('histogram.html')
show(p)


print("---------------------------------------------------")
print("  Generating multiple histograms at once  ")
print("---------------------------------------------------")

# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram, output_file, show

# Make a Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy',
              color='Continent', legend='top_left')

# Set axis labels
p.xaxis.axis_label = 'Female Literacy (% population)'
p.yaxis.axis_label = 'Number of Countries'

# Specify the name of the output_file and show the result
output_file('hist_bins.html')
show(p)

print("---------------------------------------------------")
print("   A basic box plot ")
print("---------------------------------------------------")

# Import BoxPlot, output_file, and show from bokeh.charts
from bokeh.charts import BoxPlot, output_file, show

# Make a box plot: p
p = BoxPlot(df, values='female_literacy', label='Continent',
            title='Female Literacy (grouped by Continent)', legend='bottom_right')

# Set the y axis label
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)

print("---------------------------------------------------")
print("   Color different groups differently ")
print("---------------------------------------------------")

# Import BoxPlot, output_file, and show
from bokeh.charts import BoxPlot, output_file, show

# Make a box plot: p
p = BoxPlot(df, values='female_literacy', label='Continent', color='Continent',
            title='Female Literacy (grouped by Continent)', legend='bottom_right')

# Set y-axis label
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)

print("---------------------------------------------------")
print("  A basic scatter plot  ")
print("---------------------------------------------------")

# Import Scatter, output_file, and show from bokeh.charts
from bokeh.charts import Scatter, output_file, show

# Make a scatter plot: p
p = Scatter(df, x='population', y='female_literacy',
            title='Female Literacy vs Population')

# Set the x-axis label
p.xaxis.axis_label = 'x axis'

# Set the y-axis label
p.yaxis.axis_label = 'y axis'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)

print("---------------------------------------------------")
print("   Using colors to group data ")
print("---------------------------------------------------")

# Import Scatter, output_file, and show from bokeh.charts
from bokeh.charts import Scatter, output_file, show

# Make a scatter plot such that each circle is colored by its continent: p
p = Scatter(df, x='population', y='female_literacy', color='Continent',
            title='Female Literacy vs Population')

# Set x-axis and y-axis labels
p.xaxis.axis_label = 'Population (millions)'
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)

print("---------------------------------------------------")
print("   Using shapes to group data ")
print("---------------------------------------------------")

# Import Scatter, output_file, and show from bokeh.charts
from bokeh.charts import Scatter, output_file, show

# Make a scatter plot such that each continent has a different marker type: p
p = Scatter(df, x='population', y='female_literacy', marker='Continent',
            title='Female Literacy vs Population')

# Set x-axis and y-axis labels
p.xaxis.axis_label = 'Population (millions)'
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)

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



