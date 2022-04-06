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

import csv
import os

# A direct path to the resource folder in case there are issues
#BASE = os.path.dirname(os.path.abspath(__file__))
#file_to_load = os.path.join(BASE, 'Resources', 'election_results.csv')

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()