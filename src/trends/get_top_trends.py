"""
Functions to explore trends in the last 5 years
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib import dates as mdates
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

def top_trends(df, column, variable, n):
	"""
	Gets the top trends for the variable you're interested in.

	column = column to groupby (string)
	variable = column name of the variable you're interested to explore (string)
	n = how many of the top values do you want to see? (integer)
	"""
	top = df.groupby(column)[variable].value_counts(ascending = False).reset_index(name="count")
	return top.groupby(column).head(n)

# Code to plot time series

def plot_series(df, cols=None, title='Title', xlab=None, ylab=None, steps=1):
    
    # Set figure size to be (18, 9).
    plt.figure(figsize=(22,10))
    
    # Iterate through each column name.
    for col in cols:
            
        # Generate a line plot of the column name.
        # You only have to specify Y, since our
        # index will be a datetime index.
        plt.plot(df[col])
        
    # Generate title and labels.
    plt.title(title, fontsize=26)
    plt.xlabel(xlab, fontsize=5)
    plt.ylabel(ylab, fontsize=18)
    
    
    # Enlarge tick marks.
    plt.yticks(fontsize=18)
    plt.xticks(df.index[0::steps], fontsize=18);


# Code to plot time series

def plot_rolling_series(df, cols=None, title='Title', xlab=None, ylab=None, steps=1):
    
    # Set figure size 
    fig, ax = plt.subplots(figsize=(24, 10))    
    
    # Iterate through each column name.
    for col in cols: 
            
        # Generate a line plot of the column name.
        # You only have to specify Y, since our
        # index will be a datetime index.
        ax.plot(df[col])
        
    # Generate title and labels.
    plt.title(title, fontsize=26)
    plt.xlabel(xlab, fontsize=5)
    plt.ylabel(ylab, fontsize=18)
    
    
    # set x ticks to years
    years = mdates.YearLocator()   
    yearsFmt = mdates.DateFormatter('%Y')
    monthsFmt = mdates.DateFormatter('%b')
    months = mdates.MonthLocator((4,7,10))



    # set major ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    
    # set minor ticks
    ax.xaxis.set_minor_locator(months)
    ax.xaxis.set_minor_formatter(monthsFmt)

    # add minor ticks quarterly
    #ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.grid(which='minor', color='#cccccc', linestyle=':')
    
    # Enlarge tick marks.
    plt.yticks(fontsize=18)
    plt.xticks(fontsize=18);