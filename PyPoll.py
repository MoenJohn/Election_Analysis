"""
PyPoll

The purpose of this program is to deliver the following information when run

    * Total number of votes cast
    * A complete list of candidates who received votes
    * Total number of votes each candidate received
    * Percentage of votes each candidate won
    * The winner of the election based on popular vote

To do this I will
"""
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
