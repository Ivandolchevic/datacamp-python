'''
Created on Sep 12, 2017

@author: idolchevic
'''
from numpy.random import random
import numpy as np
import pandas as pd
from bokeh.layouts import row,column
import math
import toolbox
from bokeh.models import ColumnDataSource, Select

print("---------------------------------------------------")
print("   Using the current document ")
print("---------------------------------------------------")

# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line(x=[1,2,3,4,5],y=[2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)

print("---------------------------------------------------")
print("   Add a single slider ")
print("---------------------------------------------------")

# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create a slider: slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create a widgetbox layout: layout
layout = widgetbox(slider)

# Add the layout to the current document
curdoc().add_root(layout)


print("---------------------------------------------------")
print("   Multiple sliders in one document ")
print("---------------------------------------------------")

# Perform necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(title='slider1', start=0, end=10, step=0.1,value=2)

# Create second slider: slider2
slider2 = Slider(title='slider2', start=10, end=100, step=1,value=20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1, slider2)

# Add the layout to the current document
curdoc().add_root(layout)

print("---------------------------------------------------")
print("   How to combine Bokeh models into layouts ")
print("---------------------------------------------------")

from bokeh.layouts import column
from bokeh.models import  ColumnDataSource
N = 300
curdoc().clear()
plot = figure()
x=np.sort(random(N))
y=np.sin(x)

slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x':x,'y':y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# Create a column layout: layout
layout = column(widgetbox(slider),plot)

# Add the layout to the current document
curdoc().add_root(layout)

print("---------------------------------------------------")
print("  Learn about widget callbacks  ")
print("---------------------------------------------------")


curdoc().clear()

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x) 

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)

print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")

curdoc().clear()

df = pd.read_csv('literacy_birth_rate.csv')

# world
female_literacy = [value for value in list(df['female literacy'].map(toolbox.convert_string_to_float)) if not math.isnan(value)][:100]
fertility = [value for value in list(df['fertility'].map(toolbox.convert_string_to_float)) if not math.isnan(value)][:100]
population = [value for value in list(df['population'].map(toolbox.convert_string_to_float)) if not math.isnan(value)][:100]

# Perform necessary imports
from bokeh.models import ColumnDataSource, Select

# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy': 
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
        }

# Create a dropdown Select widget: select    
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)


print("---------------------------------------------------")
print("   Synchronize two dropdowns ")
print("---------------------------------------------------")

curdoc().clear()



# Create two dropdown Select widgets: select1, select2
select1 = Select(title='First', options=['A', 'B'], value='A')
select2 = Select(title='Second', options=['1', '2', '3'], value='1')

# Define a callback function: callback
def callback(attr, old, new):
    # If select1 is 'A' 
    if new == 'A':
        # Set select2 options to ['1', '2', '3']
        select2.options = ['1', '2', '3']

        # Set select2 value to '1'
        select2.value = '1'
    else:
        # Set select2 options to ['100', '200', '300']
        select2.options = ['100', '200', '300']

        # Set select2 value to '100'
        select2.value = '100'

# Attach the callback to the 'value' property of select1
select1.on_change('value', callback)

# Create layout and add to current document
layout = widgetbox(select1, select2)
curdoc().add_root(layout)


print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")
from bokeh.models import Button
curdoc().clear()
x = x * 10
y = np.sin(x)

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    new_y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x':x,'y':new_y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)

print("---------------------------------------------------")
print("   Button styles ")
print("---------------------------------------------------")

curdoc().clear()

# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.models import  CheckboxGroup, RadioGroup, Toggle

# Add a Toggle: toggle
toggle = Toggle(button_type='success',label='Toggle button')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1','Option 2','Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1','Option 2','Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))

