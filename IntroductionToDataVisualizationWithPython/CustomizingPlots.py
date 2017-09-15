'''
Created on Aug 22, 2017

@author: idolchevic
'''

print("---------------------------------------------------")
print("  Multiple plots on single axis  ")
print("---------------------------------------------------")
import numpy as np
year = np.array([1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011])
physical_sciences = np.array([13.800000000000001, 14.9, 14.800000000000001, 16.5, 18.199999999999999, 19.100000000000001, 20.0, 21.300000000000001, 22.5, 23.699999999999999, 24.600000000000001, 25.699999999999999, 27.300000000000001, 27.600000000000001, 28.0, 27.5, 28.399999999999999, 30.399999999999999, 29.699999999999999, 31.300000000000001, 31.600000000000001, 32.600000000000001, 32.600000000000001, 33.600000000000001, 34.799999999999997, 35.899999999999999, 37.299999999999997, 38.299999999999997, 39.700000000000003, 40.200000000000003, 41.0, 42.200000000000003, 41.100000000000001, 41.700000000000003, 42.100000000000001, 41.600000000000001, 40.799999999999997, 40.700000000000003, 40.700000000000003, 40.700000000000003, 40.200000000000003, 40.100000000000001])
computer_science = np.array([13.6, 13.6, 14.9, 16.399999999999999, 18.899999999999999, 19.800000000000001, 23.899999999999999, 25.699999999999999, 28.100000000000001, 30.199999999999999, 32.5, 34.799999999999997, 36.299999999999997, 37.100000000000001, 36.799999999999997, 35.700000000000003, 34.700000000000003, 32.399999999999999, 30.800000000000001, 29.899999999999999, 29.399999999999999, 28.699999999999999, 28.199999999999999, 28.5, 28.5, 27.5, 27.100000000000001, 26.800000000000001, 27.0, 28.100000000000001, 27.699999999999999, 27.600000000000001, 27.0, 25.100000000000001, 22.199999999999999, 20.600000000000001, 18.600000000000001, 17.600000000000001, 17.800000000000001, 18.100000000000001, 17.600000000000001, 18.199999999999999])
print(type(computer_science))

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()



print("---------------------------------------------------")
print("  Using axes()  ")
print("---------------------------------------------------")


# Create plot axes for the first line plot
plt.axes([0.05,0.05,0.425,0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([0.525,0.05,0.425,0.9])


# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()



print("---------------------------------------------------")
print("   Using subplot() (1) ")
print("---------------------------------------------------")

# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()




print("---------------------------------------------------")
print("   Using subplot() (2) ")
print("---------------------------------------------------")

health = np.array([77.099999999999994, 75.5, 76.900000000000006, 77.400000000000006, 77.900000000000006, 78.900000000000006, 79.200000000000003, 80.5, 81.900000000000006, 82.299999999999997, 83.5, 84.099999999999994, 84.400000000000006, 84.599999999999994, 85.099999999999994, 85.299999999999997, 85.700000000000003, 85.5, 85.200000000000003, 84.599999999999994, 83.900000000000006, 83.5, 83.0, 82.400000000000006, 81.799999999999997, 81.5, 81.299999999999997, 81.900000000000006, 82.099999999999994, 83.5, 83.5, 85.099999999999994, 85.799999999999997, 86.5, 86.5, 86.0, 85.900000000000006, 85.400000000000006, 85.200000000000003, 85.099999999999994, 85.0, 84.799999999999997])
education = np.array([74.535327580000001, 74.149203689999993, 73.554519959999993, 73.501814429999996, 73.336811429999997, 72.801854480000003, 72.166524710000004, 72.456394810000006, 73.192821339999995, 73.821142339999994, 74.981031520000002, 75.845123450000003, 75.843649139999997, 75.950601230000004, 75.869116009999999, 75.923439709999997, 76.143015160000004, 76.963091680000005, 77.627661770000003, 78.111918720000006, 78.866858590000007, 78.991245969999994, 78.435181909999997, 77.267311989999996, 75.814932639999995, 75.125256210000003, 75.035199210000002, 75.163701299999985, 75.486160269999999, 75.838162060000002, 76.692142840000002, 77.375229309999995, 78.644243939999996, 78.544948149999996, 78.65074774, 79.067121729999997, 78.686305509999997, 78.72141311, 79.196326740000003, 79.532908700000007, 79.618624510000004, 79.432811839999999])

# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the top right subplot active in the current 2x2 subplot grid 
plt.subplot(2,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()




print("---------------------------------------------------")
print("  Using xlim(), ylim()  ")
print("---------------------------------------------------")


# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red') 
plt.plot(year, physical_sciences, color='blue')

# Add the axis labels
plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Set the x-axis range
plt.xlim((1990,2010))

# Set the y-axis range
plt.ylim((0,50))

# Add a title and display the plot
plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')

# Save the image as 'xlim_and_ylim.png'
plt.savefig('xlim_and_ylim.png',dpi=100)

plt.show()


print("---------------------------------------------------")
print("  Using axis()  ")
print("---------------------------------------------------")

# Plot in blue the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color='blue')

# Plot in red the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences,color='red')

# Set the x-axis and y-axis limits
plt.axis((1990,2010,0,50))

# Save the figure as 'axis_limits.png'
plt.savefig('axis_limits.png', dpi=100)

# Show the figure
plt.show()


print("---------------------------------------------------")
print("   Using legend() ")
print("---------------------------------------------------")

# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science') 

# Specify the label 'Physical Sciences' 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc='lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()




print("---------------------------------------------------")
print("  Using annotate()  ")
print("---------------------------------------------------")

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='bottom right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max , cs_max),xytext=(yr_max+5 , cs_max+5),arrowprops=dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()



print("---------------------------------------------------")
print("   Modifying styles ")
print("---------------------------------------------------")

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Set the style to 'ggplot'
plt.style.use('ggplot')

# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1) 

# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))

# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()

