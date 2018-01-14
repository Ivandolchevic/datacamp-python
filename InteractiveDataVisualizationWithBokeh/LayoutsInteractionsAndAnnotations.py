

from bokeh.plotting import ColumnDataSource
import pandas as pd
import numpy as np
from bokeh.plotting import figure 
from bokeh.io import output_file, show
import toolbox
import math

print("---------------------------------------------------")
print("  Creating rows of plots  ")
print("---------------------------------------------------")

df = pd.read_csv('literacy_birth_rate.csv')
source = ColumnDataSource(df)
# world
female_literacy = [value for value in list(df['female literacy'].map(toolbox.convert_string_to_float)) if not math.isnan(value)]
fertility = [value for value in list(df['fertility'].map(toolbox.convert_string_to_float)) if not math.isnan(value)]
population = [value for value in list(df['population'].map(toolbox.convert_string_to_float)) if not math.isnan(value)]



# Import row from bokeh.layouts
from bokeh.layouts import row

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p1
p1.circle('fertility', 'female literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p2
p2.circle('population', 'female literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1,p2)

# Specify the name of the output_file and show the result
output_file('fert_row.html')
show(layout)


print("---------------------------------------------------")
print("   Creating columns of plots ")
print("---------------------------------------------------")

# Import column from the bokeh.layouts module
from bokeh.layouts import column

# Create a blank figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p1
p1.circle('fertility', 'female literacy', source=source)

# Create a new blank figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p2
p2.circle('population', 'female literacy', source=source)

# Put plots p1 and p2 in a column: layout
layout = row(column(p1,p2))

# Specify the name of the output_file and show the result
output_file('fert_column.html')
show(layout)

print("---------------------------------------------------")
print("  Nesting rows and columns of plots ")
print("---------------------------------------------------")

# Read in the CSV file: df
df = pd.read_csv('auto.csv')
mpg_hp = figure(x_axis_label='mpg', y_axis_label='hp')
mpg_weight = figure(x_axis_label='mpg', y_axis_label='weight')
avg_mpg = figure(x_axis_label='avg', y_axis_label='mpg')

source = ColumnDataSource(df)
mpg_hp.circle('mpg', 'hp', source=source)
mpg_weight.circle('mpg', 'weight', source=source)
avg_mpg.circle('mpg', 'yr', source=source)

# Import column and row from bokeh.layouts
from bokeh.layouts import column,row

# Make a column layout that will be used as the second row: row2
row2 = column([mpg_hp, mpg_weight], sizing_mode='scale_width')

# Make a row layout that includes the above column layout: layout
layout = row([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)

print("---------------------------------------------------")
print("  Creating gridded layouts  ")
print("---------------------------------------------------")

df = pd.read_csv('literacy_birth_rate.csv')

# Latin America, Africa, Asia and Europe.
p1 = figure(x_axis_label='fertility', y_axis_label='female literacy')
source_lat = ColumnDataSource(df[df['Continent'] == 'LAT'])
p1.circle(x='fertility',y='female literacy',source=source_lat)

#Africa
p2 = figure(x_axis_label='fertility', y_axis_label='female literacy')
source_af = ColumnDataSource(df[df['Continent'] == 'AF'])
p2.circle(x='fertility',y='female literacy',source=source_af)

# Asia
p3 = figure(x_axis_label='fertility', y_axis_label='female literacy')
source_as = ColumnDataSource(df[df['Continent'] == 'ASI'])
p3.circle(x='fertility',y='female literacy',source=source_as)

# Europe
p4 = figure(x_axis_label='fertility', y_axis_label='female literacy')
source_eu = ColumnDataSource(df[df['Continent'] == 'EUR'])
p4.circle(x='fertility',y='female literacy',source=source_eu)

# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1,p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3,p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1, row2])

# Specify the name of the output_file and show the result
output_file('grid.html')
show(layout)

print("---------------------------------------------------")
print("   Starting tabbed layouts ")
print("---------------------------------------------------")

# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Latin America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Africa')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Asia')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')

print("---------------------------------------------------")
print("  Displaying tabbed layouts  ")
print("---------------------------------------------------")

# Import Tabs from bokeh.models.widgets
from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)

print("---------------------------------------------------")
print("   Linked axes ")
print("---------------------------------------------------")


# Link the x_range of p2 to p1: p2.x_range
p2.x_range = p1.x_range

# Link the y_range of p2 to p1: p2.y_range
p2.y_range = p1.y_range

# Link the x_range of p3 to p1: p3.x_range
p3.x_range = p1.x_range

# Link the y_range of p4 to p1: p4.y_range
p4.y_range = p1.y_range

# Specify the name of the output_file and show the result
output_file('linked_range.html')
show(layout)


