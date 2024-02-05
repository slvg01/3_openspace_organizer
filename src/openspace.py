import json
import pandas as pd
import random
from src.table import Table
from src.table import Seat


class OpenSpace:

    """Allow  :
    to create an openspace of n Table instance , counting free anc occupied Seats instance
    and allow randomized allocation of the loaded people list (in main), display and store
    the final result in a csv file.
    """

    def __init__(self, config_file="config.json"):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f).get("OpenSpace", {})
            self.nb_tables = config.get("nb_tables", 6)
            self.tables_list = [Table(i) for i in range(1, self.nb_tables + 1)]

    def count_situation(self):
        # Count and print the total free and taken spots in the the whole openspace
        total_free = sum(table.capacity_left() for table in self.tables_list)
        total_taken = sum(
            table.capacity - table.capacity_left() for table in self.tables_list
        )
        print("Total Free Spots:", total_free)
        print("Total Taken Spots:", total_taken, "\n")

    def organize(self, names):
        """allocaterandomly a list of names throuh the openspace and
        take care of over capacity colleagues
        """

        names = list(names)

        while names:
            name = names.pop(0)
            seat_allocated = False

            # Shuffle the tables order in each iteration
            randomized_table_list = random.sample(
                self.tables_list, k=len(self.tables_list)
            )
            # loop to attempt allocating the load to a free spot
            for table in randomized_table_list:
                if table.assign_seat(name):
                    seat_allocated = True
                    self.count_situation()
                    break
            # take care of the extra people versus the available total space
            if not seat_allocated:
                print(
                    f"Sorry {name}, there is no more seat available here. Please check yourself if the second room.",
                    "\n",
                )
                # Re-add the name to the list to try again if it was skipped (taken seat)
                continue
                names.append(name)

    def display(self, capacity=4, nb_tables=6):
        # to display the different tables and their occupants in a nice and readable way
        table_data = {}
        for table in self.tables_list:
            table_data[f"Table {table.table_id}"] = {
                f"Seat {i + 1}": seat.occupant for i, seat in enumerate(table.seats)
            }
        self.openspace_df = pd.DataFrame(table_data)
        print(self.openspace_df)

    def store(self, filename):
        # to store the repartition in csv  file
        final_output = f"{filename}.csv"
        self.openspace_df.to_csv(final_output)
