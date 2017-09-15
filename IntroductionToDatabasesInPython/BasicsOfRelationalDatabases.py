'''
Created on Aug 22, 2017

@author: idolchevic
'''
 
print("---------------------------------------------------")
print("   Engines and Connection Strings ")
print("---------------------------------------------------")

# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite',echo=False)

# Print table names
print(engine.table_names())



print("---------------------------------------------------")
print("   Autoloading Tables from a Database ")
print("---------------------------------------------------")

from sqlalchemy import MetaData

metadata = MetaData(bind=None)



# Import Table
from sqlalchemy import Table

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))




print("---------------------------------------------------")
print("   Viewing Table Details ")
print("---------------------------------------------------")

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine,echo=False)

# Print the column names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))


print("---------------------------------------------------")
print("   Selecting data from a Table: raw SQL ")
print("---------------------------------------------------")

connection = create_engine('sqlite:///census.sqlite',echo=False)

# Build select statement for census table: stmt
stmt = 'SELECT * FROM census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print Results
print(results)


print("---------------------------------------------------")
print("   Selecting data from a Table with SQLAlchemy ")
print("---------------------------------------------------")

# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
print(connection.execute(stmt).fetchall())



print("---------------------------------------------------")
print("  Handling a ResultSet  ")
print("---------------------------------------------------")


# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by using an index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])
