'''
from sqlalchemy import create_engine
engine = create_engine('sqllite://Northwind.sqlite')

table_names = engine.table_names()
print(table_names)
'''

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
file_path = './data/Chinook.sqlite'
engine = create_engine('sqlite:///' + file_path)

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
