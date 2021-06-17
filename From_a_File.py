'''
    # Python Pandas Read CSV – Load Data from CSV Files : 

CSV (comma-separated value) files are a common file format for transferring and storing data. The ability to read, manipulate, and write data to and from CSV files using Python is a key skill to master for any data scientist or business analysis
'''

                # Load CSV files to Python Pandas
               
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("filename.csv") 

# Preview the first 5 lines of the loaded data 
data.head()
