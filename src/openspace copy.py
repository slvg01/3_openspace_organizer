import pandas as pd
import numpy as np

    
class OpenSpace_df:        
    def __init__ (self, capacity =4, nb_tables=6):
        self.capacity = capacity
        self.table_df = pd.DataFrame({f'Table {i}': [None] * self.capacity for i in range(1, self.capacity + 1)}, 
                                     index=range(1, self.capacity + 1))
        
b = OpenSpace_df()
c = b.table_df
print(b)
print(c)   

""" class Table:
    #allow to create instance of table of 4 spots
    def __init__(self, capacity=4):
         self.capacity = capacity

class OpenSpace_df:
    def __init__ (self, nb_tables=6):
        self.tables_list = [Table().table_df  for i in range (nb_tables)]
        self.openspace_df = self.make_openspace_df()
        
        #self.openspace = self.make_openspace_pd()

    def make_openspace_df (self):
        #data = {f"Table {i+1}" : self.tables_list[i] for i in range (len(self.tables_list))}
        data = {f"Table {i + 1}": table_df for i, table_df in enumerate(self.tables_list)}
        df = pd.concat([d for d in data.values()], axis=1)
        #df.columns = [f"table {i+1}" for i in range (self.capacity)]
        return df
        
a= OpenSpace_df()
b = a.make_openspace_df()
print(b)



#nb_tables=6
#data = {f"Table{i+1}" : tables_list[i] for i in range (len(tables_list))}
# print(data)
#index = [f"row_{i}" for i in range(4)]
# df = pd.DataFrame(data, index = [f"row_{i}" for i in range(4)])
"""