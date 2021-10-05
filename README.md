# Election Audit Analysis

## Overview
The Colorado Board of Elections needs an election audit completed on a U.S. congressional district's votes.  The dataset will include votes from three sources: hand counted mail in ballots, machine counted punch card ballots, and computer counted Direct Recording Electronic ballots.  These three voting methods will determine the election results.  Instead of completing the election audit using excel, the audit will be conducted using a Python script to automate the process for future elections.

### Purpose
The purpose of the project is to automate the analysis of the election results and declare a winner by popular vote.

## Resources

- Data Source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.8.8, Visual Studio Code 1.60.2

## Process
A preliminary review of the data source showed a header row and then each subsequent row contained a unique Ballot ID, the county name in which the ballot was cast, and the candidate's name that was voted for. By using Python, a script was developed to automate the audit of the election.  Utilizing existing Python dependencies, it is possible to load and read the csv file programmatically to begin the analysis.

- In order to calculate the total votes within the congressional precinct, it was necessary to create a total vote counter that started with zero, skip the header row, iterate through each row and add to the vote counter.
```
    # Initialize a total vote counter.
    total_votes = 0
```
```
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Read the header
        header = next(reader)

        # For each row in the CSV file.
        for row in reader:

            # Add to the total vote count
            total_votes = total_votes + 1
```
- To obtain voter turnout information at the county level, a list of county names and a dictionary of county votes were created to aid in the calculations.
```
# Create a county list and county votes dictionary.
county_options = []
county_votes = {}
```
  - While iterating through the rows to obtain total votes, the county name was extracted from each row and if necessary added to our county list before adding votes to our county votes dictionary.
```
# county does not match any existing county in the county list.
        if county_name not in county_options:
            
            # Add the existing county to the list of counties.
            county_options.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
  - Using a for loop, we can then retrieve the vote totals and calculate percentages at the county level.
  ```
  for county_name in county_votes:
        # Retrieve the county vote count.
        votes_by_county = county_votes.get(county_name)
        # Calculate the percentage of votes for the county.
        vote_percentage_by_county = float(votes_by_county) / float(total_votes) * 100
   ```

- Then we can determine the county with the largest voter turnout with an if statement nested into the above for loop.
```
          if (votes_by_county > largest_turnout_count):
            largest_turnout_count = votes_by_county
            largest_turnout_county = county_name
```

- Candidate results are calculated similar to those of the county level results.
  - Create a list of possible candidates and a dictionary of candidate votes.
```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
```
  - While While iterating through the rows, candidate names are extracted and added to the candidate options list if they are not already there and then vote tallies are stored in the candidate votes dictionary.
```
# If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```
- Then we can utilize the data stored in list and dictionary to run calculations for each candidate.
```
# Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```

- We can now determine the winning candidate with the total vote count and percentage of votes.
``` 
# Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```

## [Results](analysis/election_analysis.txt)

- The total votes cast were 369,711.  

- The total number of votes can be further broken down into their respective counties.
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)

- Denver County had the largest number of votes.

- Three candidates received votes across the precinct.
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

- The Winning Election Results:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%


## Summary



provide a business proposal to the election commission on how this script can be used - with some modifications - for any election.  give at least 2 examples of how this script can be modified to be used for other elections.