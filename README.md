#Overview

Data exercise for LA Innovation Team interview.

## Executive Summary
Public health is centered on prevention. How do we build health populations by preventing illness? This work is rooted in one premise–that in order to care for your health, you have to first be safe from physical harm. I wanted to explore public health through the lens of public safety to imagine a healthy society.

## Problem Statment
Since COVID-19 hit, the number of calls to domestic violence helplines have increased. Many do not feel safe to "shelter in place." How has this been reflected in the crimes reported?

## Data 
Data is pulled from Los Angeles Crime Data set from [2010 to 2019](https://data.lacity.org/A-Safe-City/Crime-Data-from-2010-to-2019/63jg-8b9z) and [2020](https://data.lacity.org/A-Safe-City/Crime-Data-from-2020-to-Present/2nrs-mtv8). In total, there are over 2.2M rows of data in this timespan. Data is updated weekly by the LAPD. 

Code for pulling and cleaning the data was done in Python [here](./code/001_data_collection.py).

|Column|Type|Description|
|:---|:---|:---|
|dr_no|int64|Division of Records Number: Official file number made up of a 2 digit year, area ID, and 5 digits|
|date_rptd|datetime64[ns]|Date reported|
|date_occ|datetime64[ns[]|Date incident occurred|
|time_occ|int64|Time incident occurred in military time|
|area|int64|The LAPD has 21 Community Police Stations referred to as Geographic Areas within the department.|
|area_name|object|The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for.|
|rpt_dist_no|int64|A four-digit code that represents a sub-area within a Geographic Area. |
|part_1-2|int64||
|crm_cd|int64|Indicates the crime committed. (Same as Crime Code 1)|
|crm_cd_desc|object|Defines the Crime Code provided.|
|mocodes|object|Modus Operandi: Activities associated with the suspect in commission of the crime.|
|vict_age|int64|Victim's age|
|vict_sex|object|Victim's gender|
|vict_descent|object|Victim's ethnicity|
|premis_cd|float64|The type of structure, vehicle, or location where the crime took place.|
|premis_desc|object|Defines the Premise Code provided.|
|weapon_used_cd|float64|The type of weapon used in the crime.|
|weapon_desc|object|Defines the Weapon Used Code provided.|
|status|object|Status of the case. (IC, Invest Cont, is the default)|
|status_desc|object|Definse the status code provided.|
|crm_cd_1|float64|Indicates the crime committed. Crime Code 1 is the primary and most serious one. Crime Code 2, 3, and 4 are respectively less serious offenses. Lower crime class numbers are more serious.|
|crm_cd_2|float64|May contain a code for an additional crime, less serious than Crime Code 1.|
|crm_cd_3|float64|May contain a code for an additional crime, less serious than Crime Code 1.|
|crm_cd_4|float64|May contain a code for an additional crime, less serious than Crime Code 1.|
|location|object|Street address of crime incident rounded to the nearest hundred block to maintain anonymity.|
|cross_street|object|Cross Street of rounded Address|
|lat|float64|Latitude|
|lon|float64|Longitude|
|year|int64|Year of date reported|
|mocodes_1|int64|May contain a code for an additional MO|
|mocodes_2|int64|May contain a code for an additional MO|
|mocodes_3|int6|May contain a code for an additional MO|

## Exploring the Data

The data exploratory work answering the prompts was done in Python [here](./code/002_EDA.ipynb) and general exploration [here](./code/003_explore_trends.ipynb).


The top 5 crimes reported in the last 5 years were:
![top crimes](./plots/top_crimes.png)

The top 10 MO codes reported in the last 5 years were:
![top MO codes](./plots/top_mocodes.png)

Here's how the # of cases reported daily has changed over time:
![Rolling mean](./plots/daily_reports_rolling_means.png)

Overall, the % of violent crimes is increasing in these LAPD areas:
![Violent crimes](./plots/violent_crimes_area.png)


## Domestic Violence Cases

So far, the # of domestic violence cases reported in 2020 is on trend as previous years:
![DV cases](./plots/dv_cases.png)


Domestic violence cases where the victim is Asian American Pacific Islander may be underreported:
![DV AAPI](./plots/aapi_dv.png)


## Next Steps

Build a model to predict the likelihood of a case being closed. I imagine that it takes a lot of courage for victims to report their attacker, and they are looking for resolution. For cases to remain open for a long period of time, it may deter an individual (and community) from reporting.