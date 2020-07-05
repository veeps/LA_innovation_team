"""
Functions to explore trends in the last 5 years
"""

import pandas as pd


crime ={
110: "Homicide",
113: "Manslaughter",
121: "Rape",
122: "Attempted Rape",
815: "Sexual Penetration w/ Foreign Object",
820: "Oral Copulation",
821: "Sodomy",
210: "Robbery",
220: "Robbery - attempted",
230: "ADW",
231: "ADW against LAPD Police Officer",
235: "Child beating",
236: "Spousal beating",
250: "Shots Fired",
251: "Shots fired inhabited dwelling",
761: "Brandishing",
926: "Train Wrecking",
435: "Lynching",
436: "Lynching - attempted",
437: "Resisting Arrest",
622: "Battery on Firefighter",
623: "Battery on Police Officer",
624: "Battery - misdemeanor",
625: "Other Misd. Assault",
626: "Spousal/Cohab Abuse - Simple Assault",
627: "Child Abuse - Simple Assault",
647: "Throwing substance at vehicle",
763: "Stalking",
928: "Threatening Phone Calls / Letters",
930: "Criminal Threats",
310: "Burglary",
320: "Burglary - attempted",
510: "Stolen Vehicle",
520: "Stolen Vehicle - attempted",
433: "DWOC",
330: "Burg from Vehicle",
331: "Theft from vehicle - $950.01 & over",
410: "Burg from Vehicle - attempted",
420: "Theft from vehicle - $950 & under",
421: "Theft from vehicle attempted",
350: "Theft from person ",
351: "Pursesnatch",
352: "Pickpocket",
353: "Drunkroll",
450: "Theft from person - attempted ",
451: "Pursesnatch - attempted",
452: "Pickpocket - attempted",
453: "Drunkroll - attempted",
341: "Theft - $950.01 & over",
343: "Shoplifting - $950.01 & over",
345: "Dishonest employee - grand theft ",
440: "Theft - $950 & under",
441: "Theft - attempted",
442: "Shoplifting - $950 & under",
443: "Shoplifting - attempted",
444: "Dishonest employee - petty theft",
445: "Dishonest Employee - attempted",
470: "Till Tap - $950.01 & over",
471: "Till Tap - $950 & under",
472: "Till Tap - attempted",
473: "Theft from coin m/c - $950.01 & over",
474: "Theft from coin m/c - $950 & under",
475: "Theft from coin m/c - attempted",
480: "Bicycle - stolen",
485: "Bicycle - attempted stolen",
487: "Boat - stolen",
491: "Boat - attempted stolen"}

def get_names(df, column, dict):
	"""
	Get get the names of the code listed.
	
	column = column to get names for (string)
	dict = dictionary containing the names of each code. Use `crime` for crime codes `mo` for MO codes
	"""
	return df[column].apply(dict.get)