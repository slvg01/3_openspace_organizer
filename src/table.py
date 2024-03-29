import pandas as pd
import json


class Table:
    """
    Allows creating Table instances of a tables with n seats in the form of a n(nb of seats)*1(column) DataFrame.
    the instances are initialized with None values everywhere
    """

    def __init__(self, config_file="config.json"):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f).get("Table", {})
        self.capacity = config.get("capacity", 4)
        self.table_df = pd.DataFrame(
            {f"Table": [None] * self.capacity for i in range(1, self.capacity + 1)},
            index=range(1, self.capacity + 1),
        )

    def __str__(self):
        # allow to get human readdbale output when printing the object
        return (
            f"This is on of the table fitted in the room. it has {self.capacity} chairs"
        )
