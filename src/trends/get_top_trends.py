"""
Functions to explore trends in the last 5 years
"""

import pandas as pd


def top_trends(df, column, variable, n):
	"""
	Gets the top trends for the variable you're interested in.

	column = column to groupby (string)
	variable = column name of the variable you're interested to explore (string)
	n = how many of the top values do you want to see? (integer)
	"""
	top = df.groupby(column)[variable].value_counts(ascending = False).reset_index(name="count")
	return top.groupby(column).head(n)