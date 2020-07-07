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