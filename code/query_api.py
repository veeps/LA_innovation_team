# Import libraries
import requests
import pandas as pd
import datetime as dt
import time


# custom function to query api multiple times

def query(n_samples):
    base_url = 'https://data.lacity.org/resource/63jg-8b9z.json' # base url for api
    list_posts = []
    oldest_post = None
    
    while len(list_posts) < n_samples: # n_samples exceeds the api limit of 2000
        
        res = requests.get(base_url) # request reddit info
            
        posts = res.json() # create list from json
        
        if len(posts) == 0:
            oldest_post = None # for the first time running this, before will be None
            list_posts.extend(posts) # add batch of posts to list_posts     
        else:
            time.sleep(3) # wait 3 seconds before querying again
            oldest_post = pd.to_datetime(res.json()[-1]["date_occ"].split("T")[0]) # take the oldest time from the list and pull posts before that time
            list_posts.extend(posts) # add batch of posts to list_posts
            print(f'Collected {len(list_posts)} rows') # status check
    return pd.DataFrame(list_posts) # return pandas dataframe