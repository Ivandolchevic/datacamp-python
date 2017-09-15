'''
Created on Sep 12, 2017

@author: idolchevic
'''
import shapefile 
import numpy as np
import re

# Import figure from bokeh.plotting
from bokeh.plotting import figure 

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

#sf = shapefile.Reader('regions-20140306-100m.shp')
#sf = shapefile.Reader('communes-20150101-100m.shp')
sf = shapefile.Reader('cb_2016_us_state_20m.shp')
# Read the field descriptors for the database file
print('fields:',sf.fields)


 #will store the geometry separately
#first = geomet[0] #will extract the first polygon to a new object
#print(first.shape.points) #will show you the points of the polygon
#print(first.record) #will show you the attributes

def explore_records():
    geomets = sf.shapeRecords()
    for i in range(10):
        geomet = geomets[i]
        print(geomet.record)
            
def view_records_31():
    geomets = sf.shapeRecords()
    #for i in range(10):
    #    geomet = geomets[i]
    for geomet in geomets:        
        if re.match(r'^31',geomet.record[0]):
            print(geomet.record)

def plot_shapes():
    xs = []
    ys = []
    p = figure()
    
    geomets = sf.shapeRecords()
    # get the shapes
    for geomet in geomets:   
        if re.match(r'^31',geomet.record[0]):  
            xs.append([point[0] for point in geomet.shape.points])
            ys.append([point[1] for point in geomet.shape.points])
    
    p.patches(xs,ys, line_color='white')
    output_file('france_regions.html')
    show(p)
    
    
explore_records()
    