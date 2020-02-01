# Subreddit_Recommender
based on your subreddit usage, which other subreddits might you like? 

Requirements: 
    deliver a recommender system
    use a clustering algorithm somewhere in the process (with too much data)
        would have to 'joblib' save and train the model
    Functional Programming (pipelines)
    implement a custom module
    command line application - argument for number of subreddits (input() function), based on those entries, recommends the subreddits to the user, set a cap on the number of subreddits returned
    error handling so program doesn't crash
    Github Repo

database structure
Username | subreddit | Timestamp of comment
14m Rows
22,610 Users
34,967 subreddit

Reference Material: https://towardsdatascience.com/build-your-own-clustering-based-recommendation-engine-in-15-minutes-bdddd591d394


Process:
Create Github Repo - Ramon
Import the data - 
Exploratory Data Analysis - class balance (distribution), 


Build
Final Product

SQL Script
    import the data to CSV (save the SQL Script for the code review)
         our SQL query was designed to Group by User, count of UTC, 

clean.py - Pipeline
    try/except to import the CSV outputted by the SQL Script. If not found, run the SQL Script.
        pipepline to clean the data .lower()
        export to CSV
        
        
cluster.py
    try/except to take that CSV and run the selected Clustering Model on it. Evaluate the Model. Pickle that Trained Model


main.py - our command-line interface, accepting the inputted arguments
    error handling on the inputs
    try/except to import that pickled model from cluster.py <!-- our clustered module -->
    import the inputted arguments from the command line, return the desired number of results

