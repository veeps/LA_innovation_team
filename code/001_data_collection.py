"""
Loading Crime Data from 2010 to 2019 and 2020 for Los Angeles.
Data source for 2010 to 2019: https://data.lacity.org/A-Safe-City/Crime-Data-from-2010-to-2019/63jg-8b9z
Data source for 2020: https://data.lacity.org/A-Safe-City/Crime-Data-from-2020-to-Present/2nrs-mtv8
"""
import pandas as pd
import pickle
import numpy as np

# read in data from 2010-2019
df_2019 = pd.read_csv("https://data.lacity.org/api/views/63jg-8b9z/rows.csv")

# read in data from 2020
df_2020 = pd.read_csv("https://data.lacity.org/api/views/2nrs-mtv8/rows.csv")

# check if column names are the same
df_2020.columns == df_2019.columns

# remove trailing space in 'AREA' so the column names match between the two dataframes
df_2019.rename(columns={"AREA ": "AREA"}, inplace = True)

# combine data into one dataframe
df = pd.concat([df_2019, df_2020])

######################
### data cleaning ####

# Map the lowering function to all column names
df.columns = map(str.lower, df.columns)

# Remove spaces from column names
df.columns = df.columns.str.replace(" ", "_")

# Convert date columns to date objects
df["date_rptd"] = pd.to_datetime(df["date_rptd"])
df["date_occ"]= pd.to_datetime(df["date_occ"])

# Create a date year column
df['year'] = pd.DatetimeIndex(df['date_rptd']).year


# Convert MO codes to numerics
df["mocodes"] = df["mocodes"].str.replace("-", "0") # remove dash
df["mocodes_1"] = df["mocodes"].str.split(" ").str[0].fillna(0).astype(int)
df["mocodes_2"] = df["mocodes"].str.split(" ").str[1].fillna(0).astype(int)
df["mocodes_3"] = df["mocodes"].str.split(" ").str[2].fillna(0).astype(int)

# save data for later use
pickle.dump(df, open("../data/crime_data.pkl", "wb"))