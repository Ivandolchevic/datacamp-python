'''
Created on Sep 12, 2017

@author: idolchevic
'''

from bokeh.plotting import ColumnDataSource
import pandas as pd
import numpy as np
from bokeh.plotting import figure 
from bokeh.io import output_file, show
from statfunc import toolbox
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
from ____ import ____

# Create a blank figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add circle scatter to the figure p1
p1.circle('fertility', 'female_literacy', source=source)

# Create a new blank figure: p2


# Add circle scatter to the figure p2


# Put plots p1 and p2 in a column: layout


# Specify the name of the output_file and show the result
output_file('fert_column.html')
show(layout)

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



print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")



print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")



print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")



