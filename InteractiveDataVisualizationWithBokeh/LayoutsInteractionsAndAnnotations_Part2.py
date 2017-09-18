# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 08:33:54 2017

@author: Laurent
"""

import pandas as pd
import numpy as np

from bokeh.io import output_file, show
import toolbox
import math
from bokeh.plotting import ColumnDataSource, figure 
from bokeh.layouts import column,row
from bokeh.layouts import gridplot
from bokeh.models.widgets import Panel,Tabs


df = pd.read_csv('literacy_birth_rate.csv')
source = ColumnDataSource(df)

print("---------------------------------------------------")
print("   Linked brushing ")
print("---------------------------------------------------")


# Create ColumnDataSource: source
source = ColumnDataSource(df)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select')

# Add a circle glyph to p1
p1.circle('fertility','female literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select')

# Add a circle glyph to p2
p2.circle('fertility','population', source=source)

# Create row layout of figures p1 and p2: layout
layout = row(p1,p2)

# Specify the name of the output_file and show the result
# output_file('linked_brush.html')
# show(layout)


print("---------------------------------------------------")
print("   How to create legends ")
print("---------------------------------------------------")

df = pd.read_csv('literacy_birth_rate.csv')
df.columns = ['Country', 'Continent', 'female_literacy', 'fertility', 'population']
df['female_literacy'] = df['female_literacy'].map(toolbox.convert_string_to_float)
df['fertility'] = df['fertility'].map(toolbox.convert_string_to_float)

p = figure(x_axis_label='fertility', y_axis_label='female literacy')

# Latin America
latin_america  = ColumnDataSource(df[df['Continent'] == 'LAT'])

#Africa
africa = ColumnDataSource(df[df['Continent'] == 'AF'])

# Add the first circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=africa, size=10, color='blue', legend='Africa')

# Specify the name of the output_file and show the result
# output_file('fert_lit_groups.html')
# show(p)


print("---------------------------------------------------")
print("   Positioning and styling legends ")
print("---------------------------------------------------")

# Assign the legend to the bottom left: p.legend.location
p.legend.location = 'bottom_left'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p.legend.background_fill_color = 'lightgray'

# Specify the name of the output_file and show the result
# output_file('fert_lit_groups.html')
# show(p)


print("---------------------------------------------------")
print("  Adding a hover tooltip  ")
print("---------------------------------------------------")

# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Country','@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)
