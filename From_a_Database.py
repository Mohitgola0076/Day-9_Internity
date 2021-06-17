'''
The Pandas is a popular data analysis module that helps users to deal with structured data with simple commands. Using the Pandas dataframe, you can load data from CSV files or any database into the Python code and then perform operations on it.
'''
                # Create Pandas dataframe from SQL tables

import pandas
    import sqlalchemy
    
    # Create the engine to connect to the PostgreSQL database
    engine = sqlalchemy.create_engine('postgresql://postgres:test1234@localhost:5432/sql-shack-demo')
     
    # Read data from SQL table
    sql_data = pandas.read_sql_table('superstore',engine)
