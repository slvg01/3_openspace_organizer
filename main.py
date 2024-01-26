import pandas as pd
from src.table import Table
from src.openspace import OpenSpace_df

# protect the main script 
if __name__ == "__main__":
    # import the liste of colleagues 
    colleagues_list = pd.read_csv('colleagues.csv')['Name']
    
    #create the OpenSpace instance (that will itself create the table instance)
    a = OpenSpace_df()

    #divide the people accross table/chair  
    a.random_allocate(colleagues_list)
  
    # store output 
    b = a.openspace_df
   
    # show output
    print(b)


