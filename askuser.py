"""
This file is designed get the new user's input data, process that input in a similar fashion to
"""


# DEPENDENCIES
import pandas as pd
import numpy as np

# IMPORT THE MODEL

# IMPORT THE MAPPER
from pull import sr_map

# GLOBAL VARIABLES


# DEFINE FUNCTIONS


# Ask the user's input
def getSubreddits():
    """This function will iterate through requesting 5 Subreddits from the user, 
    and running data validation on each"""

    print("We will be asking you for 5 Subreddits that interest you")
    
    preferred_subreddits = [] # create an empty list

    while len(preferred_subreddits) < 5: # while we have less than 5 subreddits entered, keep running

        sr1 = input("Please enter a Subreddit you enjoy\n").lower().strip() # 
        if sr1 in sr_map.values() and sr1 not in preferred_subreddits: # mapper was already lowered
            preferred_subreddits.append(sr1)
        # try:
        #     if sr1 in inv_dict_sub.values():

        # except:
        #     Print("I'm sorry, I don't recognize that Subreddit. Please try again.")

        # preferred_subreddits.append(sr1)
        print(f"You have entered {len(preferred_subreddits)} of 5")
    
    return preferred_subreddits

new_user = getSubreddits()

print(new_user)

# pass the user's input through the same data "processing" that the model's data was done

