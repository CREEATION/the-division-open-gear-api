import pandas as pd
import sqlite3


class Brands:

    def __init__(self):
        self.conn = sqlite3.connect(r"C:\pybridgeacc\td2_api\gear.db")
        self.brands  = pd.read_sql_query("select * from Brand", self.conn)
        self.five_11 = self.brands.where(self.brands.id == '7a234731-2738-4e27-9caf-2c21ece1f92b').dropna()