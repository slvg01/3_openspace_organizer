import pandas as pd
from src.table import Table
from src.openspace import OpenSpace


# protect the main script
if __name__ == "__main__":
    # import the liste of colleagues
    colleagues_list = pd.read_csv("colleagues.csv")["Name"]

    # create the OpenSpace instance (that will itself create the table instance)
    a = OpenSpace()

    # divide the people accross table/chairs in the openspace
    a.organize(colleagues_list)

    # store output
    a.display()

    # show output
    a.store("output_file")
