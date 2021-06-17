'''
The Pandas Series Object
A Pandas Series is a one-dimensional array of indexed data. It can be created from a list or array as follows:
'''
  
                # Example : 

data = pd.Series([0.25, 0.5, 0.75, 1.0])
data

    # Output : 
0    0.25
1    0.50
2    0.75
3    1.00
dtype: float64
    
            # Series as specialized dictionary
        
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
population

    # Output : 
California    38332521
Florida       19552860
Illinois      12882135
New York      19651127
Texas         26448193
dtype: int64

   
                    # Constructing Series objects : 
    
pd.Series([2, 4, 6])

    # Output :
0    2
1    4
2    6
dtype: int64
    
    
