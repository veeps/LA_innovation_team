"""
Functions to explore trends in the last 5 years
"""

import pandas as pd
import json
import os

# Read in crime code dictionary
with open("../assets/crime_codes.json") as f:
                    crime_data = json.loads(f.read())
crime_dict = dict((int(k), v) for k, v in crime_data.items())   

# Read in violent crime code dictionary
with open("../assets/violent_crime_codes.json") as f:
                    violent_crime_data = json.loads(f.read())
violent_crime_dict = dict((int(k), v) for k, v in violent_crime_data.items())    

# Read in MO code dictionary
with open("../assets/mo_codes.json") as f:
                    mocode_data = json.loads(f.read())
mocode_dict = dict((int(k), v) for k, v in mocode_data.items())                    


def get_names(df, column, dict):
	"""
	Get get the names of the code listed.
	
	column = column to get names for (string)
	dict = dictionary containing the names of each code. Use `crime` for crime codes `mo` for MO codes
	"""

	return df[column].apply(dict.get)