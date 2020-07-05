"""
Functions to explore trends in the last 5 years
"""

import pandas as pd
import json
import os

# Read in crime code dictionary
with open("../data/crimecodes.json") as f:
                    mocodes_data = json.loads(f.read())
crime_dict = dict((int(k), v) for k, v in data.items())   

# Read in MO code dictionary
with open("../data/mocodes.json") as f:
                    mocodes_data = json.loads(f.read())
mocode_dict = dict((int(k), v) for k, v in data.items())                    




def get_names(df, column, dict):
	"""
	Get get the names of the code listed.
	
	column = column to get names for (string)
	dict = dictionary containing the names of each code. Use `crime` for crime codes `mo` for MO codes
	"""

	return df[column].apply(dict.get)