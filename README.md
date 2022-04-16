# Election Analysis
This is an analysis of election results 

## Overview of Election Audit: Explain the purpose of this election audit analysis.
This election audit analysis was requested by the election commission, originaly to review a database of all votes and review which candidate had the most votes, and was later expanded to include voter turnouts by county as well. To do this I used a python script to read the contents of a voter results csv file, extract and analyze the relevent information inside, and write the results to an output file. With the information provided we can asses the number of total votes, votes by county, and candidate vote percentages and totals, all of which are detailed below. The raw election results file is kept in the _Resources_ directory, while the output or final analysis is written to the _analysis_ directory. 


## Election-Audit Results: 
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

* How many votes were cast in this congressional election?
    There were 369,711 Votes in this election. This was verified through counting every vote and can be seen as the final line in the raw data as well
    ["election_results_total_votes.png"]("Resources/election_results_total_votes.png")
    
   
* Breakdown of total votes by county

  |  County | # of Total Votes | % of Total Votes  |
  | ------------- | ------------- | ------------- |
  | Jefferson  | 38,855  | 10.5%  |
  | Denver  | 306,055  | 82.8%  |
  | Arapahoe  | 24,801  | 6.7%  |

* Which county had the largest number of votes?
    Denver county had by far the largest number of votes at 306,005, rougly a factor of ten greater than both Jefferson and Arapahoe counties

* Breakdown of total votes by candidate

  |  County | # of Total Votes | % of Total Votes  |
  | ------------- | ------------- | ------------- |
  | Charles Casper Stockham  | 85,213  | 23.0%   |
  | Diana DeGette  | 272,892  | 73.8%  |
  | Raymon Anthony Doane  | 11,606  |3.1%  |

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    According to my results the winner of the election was Diana DeGette, with a landslide victory of 73.8% of all votes and total vote count of 73.8%

# Election-Audit Summary: 
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

In summary, this code can be used for any sort of upcoming election as is as long as the format of the input data remains the same. However, there are a couple things that could be done to improve the code. For starters, by counting which votes for certain candidates came from which counties. This information doesn't influence the results of the election in anyway but it would extra data and insight into the demograhics of the candidates voters. This change would be possible with the amount of information we have available here, but if there was any additional data that the commity would like to see the program couldg be motified to show that as well. A couple examples would be voter data such as age for more demographic insights or the way the vote was cast (machine, vs by hand, vs machine read card) to see if there was any influence or coorolation with voting methods and results. Finaly, adding in county total population data would allow us to learn about voter turnout and participatino in each county.
