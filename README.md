# Election_Analysis

## Purpose of Election Audit
A Colorado Board of Elections employee has asked us to complete the election audit of a recent local congressional election. If the audit is successfully automated using Python, the code will have the potential to be used to audit not only other congressional districts, but also senatorial districts and local elections. 

## Overview of Election Audit Tasks

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
### Total Votes
* There were **369,711 total votes** cast in this congressional election.

### County Breakdown

There were three counties in the precint: Jefferson, Denver, and Arapahoe.

The voter turnout for each county was:
  * Jefferson County had a 10.5% voter turnout with 38,855 voters.
  * Denver County had a 82.8% voter turnout with 306,055 voters.
  * Arapahoe County had a 6.7% voter turnout with 24,801 voters.

* The county with the **highest turnout** was **Denver** with an **82.8% voter turnout (306,055 voters)**.

### Candidate Breakdown

There were three candidates in the election: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.

The candidate results were:

  * Charles Casper Stockham recieved 23.0% of the votes (85,213 votes).
  * Diana DeGette recieved 73.8% of the vote (272,892 votes).
  * Raymon Anthony Doane recieved 3.1% of the vote (11,606 votes).

* The **winner** of the election was **Diana DeGette** who recieved **73.8%** of the vote, with **272,892 votes**.

![Election Audit Results]("https://user-images.githubusercontent.com/103080942/164946680-869237a7-b330-4fa6-a054-7bb2befbbd17.png")

## Election Audit Summary

In addition to completing the election audit of a recent local congressional election, we effectively automated the overall election audit process in Python. Our versatile script would be extremely beneficial for use by the election commission because it can be can be used for other congressional districts, senatorial districts, and local elections.

If you are seeking a similar summary of largest voter turnout and winner candidate, you can simply load your election data file at sections file_to_load and file_to_save. Our script will produce a succint summary reflecting your specific counties and candidates--with the ability to analyze a much larger pool of candidate and county options. 

This code also allows users the freedom to personalize it based on their unique needs. You might customize the script to specify, for example, your chosen geographic focus, by simply editing the variable names (i.e. to city or states). You might also choose to build upon our code with information such as voter demographics, by simply pulling in additional data from your file, and mirroring the steps we used to find candidate and county summaries. 
