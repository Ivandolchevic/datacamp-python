'''
Created on Aug 8, 2017

@author: idolchevic
'''

from sqlalchemy import create_engine
import pandas as pd 

print("---------------------------------------------------")
print("      Creating a database engine")
print("---------------------------------------------------")



# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')


print("---------------------------------------------------")
print("      What are the tables in the database?")
print("---------------------------------------------------")
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)


print("---------------------------------------------------")
print("     FREE TEST ")
print("---------------------------------------------------")

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con :
    rs = con.execute('SELECT EmployeeId,FirstName,Email FROM Employee ORDER BY Email ASC')
    df = pd.DataFrame(rs.fetchmany(10))
    df.columns = rs.keys()

print(df)



print("---------------------------------------------------")
print("     Pandas and The Hello World of SQL Queries! ")
print("---------------------------------------------------")


# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?
print(df.equals(df1))


print("---------------------------------------------------")
print("     Pandas for more complex querying ")
print("---------------------------------------------------")
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY Birthdate',engine)

# Print head of DataFrame
print(df.head())




print("---------------------------------------------------")
print("    The power of SQL lies in relationships between tables: INNER JOIN  ")
print("---------------------------------------------------")

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Album.Title, Artist.Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID ")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())



print("---------------------------------------------------")
print("    Filtering your INNER JOIN  ")
print("---------------------------------------------------")
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000',engine)

# Print head of DataFrame
print(df.head())
