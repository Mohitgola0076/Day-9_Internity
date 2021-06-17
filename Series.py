'''
Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.
Creating a series from array: In order to create a series from array, we have to import a numpy module and have to use array() function.
'''

                # Example : 

# import pandas as pd
import pandas as pd
 
# import numpy as np
import numpy as np
 
# simple array
data = np.array(['g','e','e','k','s'])
 
ser = pd.Series(data)
print(ser)


                # Creating a series from Lists:
 # In order to create a series from list, we have to first create a list after that we can create a series from list.

import pandas as pd
 
# a simple list
list = ['g', 'e', 'e', 'k', 's']
  
# create series form a list
ser = pd.Series(list)
print(ser)


                # Accessing element of Series

# import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)
  
  
#retrieve the first element
print(ser[:5])


                # Accessing Element Using Label (index) :
   
# import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
  
  
# accessing a element using index element
print(ser[16])

