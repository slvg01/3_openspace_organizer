import pandas as pd
import numpy as np
from src.table import Table


class OpenSpace_df:

    """Allow  :
    to create a representation of the open space in data frame of n(seats/table)*N(nb of tables)
    To randomaize the allocation of colleagues to available seast in the room
    while counting/displayin the current capacity status
    and Taking care of over capacity
    """

    def __init__(self, nb_tables=6):
        # Create a list of all Table instances to represent each table in the open space
        self.tables_list = [Table().table_df for i in range(nb_tables)]
        # Ensure we can get access to the final DataFrame right from the OpenSpace instance
        self.openspace_df = self.make_openspace_df()

    def make_openspace_df(self, nb_tables=6):
        # Concatenate table instances in a single DF being the full initial empty openspace
        data = {
            f"Table {i + 1}": table_df for i, table_df in enumerate(self.tables_list)
        }
        df = pd.concat(list(data.values()), axis=1)
        df.columns = [f"Table {i}" for i in range(1, nb_tables + 1)]
        return df

    def random_allocate(self, names):
        """allocation randomly a list of names throuh the openspace and
        take care of over capacity colleagues
        """
        df = self.openspace_df
        allocated_names = list()

        for n in range(len(names)):
            # check if the openspace is full
            if df.isna().sum().sum() == 0:
                print(
                    f"Sorry {names[n]}, there is no more seat availalbe here, pleasecheck yourself if the second room"
                )
            else:
                while True:
                    # calculate a random spot
                    random_row = np.random.randint(0, df.shape[0])
                    random_column = np.random.randint(0, df.shape[1])
                    random_spot = df.iloc[random_row, random_column]

                    # Check if the selected random spot is empty
                    if pd.isna(random_spot) == True:
                        df.iloc[random_row, random_column] = names[n]
                        allocated_names.append(names[n])
                        print(
                            f"Dear {names[n]}, please sit on table {random_column + 1} at place {random_row + 1}"
                        )
                        self.count_situation()
                        break
                    # Allow to reinsert potentially rejected people to the list (because of taken seat)
                    elif df.isna().sum().sum() == 0 and names[n] not in allocated_names:
                        break

    def count_situation(self):
        ### Count and print the total free and taken spots in the open space
        df = self.openspace_df
        total_free = df.isna().sum().sum()
        total_taken = df.shape[0] * df.shape[1] - total_free
        self.total_free = total_free
        self.total_taken = total_taken
        print("Total Free Spots:", total_free)
        print("Total Taken Spots:", total_taken)
