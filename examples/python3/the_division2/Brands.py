from Slots import Slots
import sqlite3
import pandas as pd


class Brand:


    def __init__(self, name,slot_bonus_1,slot_bonus_2, slot_bonus_3, df):

        self.name = name
        self.slot_bonus_1 = slot_bonus_1
        self.slot_bonus_2 = slot_bonus_2
        self.slot_bonus_3 = slot_bonus_3
        self.__make_slots(df)



    def __make_slots(self,df):
        if (df.mask == 1):
            self.mask = True
        else:
            self.mask = False
        if (df.backpack ==1).values[0]:
            self.backpack = True

        else:
            self.backpack = False

        if (df.vest == 1).values[0]:
            self.vest = True
        else:
            self.vest = False

        if (df.gloves ==1).values[0]:
            self.gloves = True
        else:
            self.gloves = False

        if (df.holster == 1).values[0]:
            self.holster = True
        else:
            self.holster = False

        if (df.kneepads == 1).values[0]:
            self.kneepads = True
        else:
            self.kneepads = False



conn = sqlite3.connect(r"gear.db")
brands_df = pd.read_sql_query("select * from Brand", conn)

five_11_df = brands_df.where(brands_df.id == '7a234731-2738-4e27-9caf-2c21ece1f92b').dropna()
five_11 = Brand(five_11_df.name.values[0], five_11_df.set_bonus_1.values[0],five_11_df.set_bonus_2.values[0],five_11_df.set_bonus_2.values[0], five_11_df)

def update_brands():
    conn = sqlite3.connect(r"gear.db")
    brands_df = pd.read_sql_query("select * from Brand", conn)
    five_11_df = brands_df.where(brands_df.id == '7a234731-2738-4e27-9caf-2c21ece1f92b').dropna()
    five_11 = Brand(five_11_df.name.values[0], five_11_df.set_bonus_1.values[0],five_11_df.set_bonus_2.values[0],five_11_df.set_bonus_2.values[0], five_11_df)




