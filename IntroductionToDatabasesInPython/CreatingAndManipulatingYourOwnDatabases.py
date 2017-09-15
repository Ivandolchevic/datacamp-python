'''
Created on Aug 22, 2017

@author: idolchevic
'''

from sqlalchemy import MetaData,create_engine,update,and_,func
import csv

print("---------------------------------------------------")
print("   Creating Tables with SQLAlchemy ")
print("---------------------------------------------------")

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()
 
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))
 

print("---------------------------------------------------")
print("   Constraints and Data Defaults ")
print("---------------------------------------------------")

metadata = MetaData()

# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))



print("---------------------------------------------------")
print("  Inserting a single row with an insert() statement  ")
print("---------------------------------------------------")

metadata = MetaData()
connection = create_engine('sqlite:///:memory:')
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)
metadata.create_all(connection)

#metadata = MetaData()
#data = Table('data', metadata, autoload=True, autoload_with=connection)

# Import insert and select from sqlalchemy
from sqlalchemy import insert,select

# Build an insert statement to insert a record into the data table: stmt
stmt = insert(data).values(name='Anna', count=1, amount=1000.0, valid=True)

# Execute the statement via the connection: results
results = connection.execute(stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(connection.execute(stmt).first())



print("---------------------------------------------------")
print("   Inserting Multiple Records at Once ")
print("---------------------------------------------------")

stmt = data.delete(data.columns.name == 'Anna')
connection.execute(stmt)

# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.0, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.0, 'valid': False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)



print("---------------------------------------------------")
print("   Loading a CSV into a Table ")
print("---------------------------------------------------")


metadata = MetaData(bind=None)
connection = create_engine('sqlite:///:memory:')
census = Table('census', metadata,
             Column('state', String(30)),
             Column('sex', String(1)),
             Column('age', Integer()),
             Column('pop2000', Integer()),
             Column('pop2008', Integer())
)
metadata.create_all(connection)
csvfile = open('census.csv')
csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')




# Create a insert statement for census: stmt
stmt = insert(census)

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    
    #create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)

csvfile.close()

print("---------------------------------------------------")
print("  Updating individual records  ")
print("---------------------------------------------------")

connection = create_engine('sqlite:///census.sqlite',echo=False)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=connection)

# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state = 36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())



print("---------------------------------------------------")
print("   Updating Multiple Records ")
print("---------------------------------------------------")

# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)



print("---------------------------------------------------")
print("   Correlated Updates ")
print("---------------------------------------------------")
metadata = MetaData(bind=None)
flat_census = Table('flat_census',metadata,
                    Column('state_name', String(length=256)),
                     Column('fips_code', String(length=256)))

metadata.create_all(connection)

# Build a statement to select name from state_fact: stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to Match the fips_state to flat_census fips_code
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state  == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt: update_stmt
update_stmt = update(flat_census).values(state_name = fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)



print("---------------------------------------------------")
print("   Deleting all the records from a table ")
print("---------------------------------------------------")

from shutil import copyfile
copyfile('census.sqlite', 'census_delete.sqlite')
connection = create_engine('sqlite:///census_delete.sqlite',echo=False)
census = Table('census', metadata, autoload=True, autoload_with=connection)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=connection)


# Import delete, select
from sqlalchemy import delete,select

# Build a statement to empty the census table: stmt
stmt = delete(census)

# Execute the statement: results
results = connection.execute(stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table
stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(stmt).fetchall())



print("---------------------------------------------------")
print("  Deleting specific records  ")
print("---------------------------------------------------")
copyfile('census.sqlite', 'census_delete.sqlite')
connection = create_engine('sqlite:///census_delete.sqlite',echo=False)
census = Table('census', metadata, autoload=True, autoload_with=connection)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=connection)

# Build a statement to count records using the sex column for Men ('M') age 36: stmt
stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(stmt).scalar()

# Build a statement to delete records from the census table: stmt_del
stmt_del = delete(census)

# Append a where clause to target Men ('M') age 36
stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)


print("---------------------------------------------------")
print("  Deleting a Table Completely  ")
print("---------------------------------------------------")
copyfile('census.sqlite', 'census_delete.sqlite')
engine = create_engine('sqlite:///census_delete.sqlite',echo=False)
metadata = MetaData(bind=None)
census = Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Drop the state_fact table
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))



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




