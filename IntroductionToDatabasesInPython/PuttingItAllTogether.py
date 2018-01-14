'''
Created on Aug 22, 2017

@author: idolchevic
'''

from sqlalchemy import MetaData,create_engine,update,and_,func,desc
import csv

print("---------------------------------------------------")
print("    ")
print("---------------------------------------------------")

# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()



print("---------------------------------------------------")
print("   Create the Table to the Database ")
print("---------------------------------------------------")

# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age',Integer()),
               Column('pop2000',Integer()),
               Column('pop2008',Integer()))

# Create the table in the database
metadata.create_all(engine)



print("---------------------------------------------------")
print("    Reading the Data from the CSV")
print("---------------------------------------------------")

csvfile = open('census.csv')
csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Create an empty list: values_list
values_list = []
 
# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age':row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    # Append the dictionary to the values list
    values_list.append(data)


csvfile.close()

print("---------------------------------------------------")
print("   Load Data from a list into the Table ")
print("---------------------------------------------------")

connection = create_engine('sqlite:///chapter5.sqlite')
metadata = MetaData(bind=None)
census = Table('census',metadata,autoload=True, autoload_with=connection)

# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt,values_list)

# Print rowcount
print(results.rowcount)



print("---------------------------------------------------")
print("   Build a Query to Determine the Average Age by Population ")
print("---------------------------------------------------")


# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
stmt = select([census.columns.sex,
                (func.sum(census.columns.pop2008 * census.columns.age) /
                func.sum(census.columns.pop2008)).label('average_age')
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for row in results:
    print(row.sex, row.average_age)


print("---------------------------------------------------")
print("   Build a Query to Determine the Percentage of Population by Gender and State ")
print("---------------------------------------------------")

# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)



print("---------------------------------------------------")
print("   Build a Query to Determine the Difference by State from the 2000 and 2008 Censuses ")
print("---------------------------------------------------")

# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
     (census.columns.pop2008-census.columns.pop2000).label('pop_change')
])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))

