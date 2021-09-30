# Data needed to retrieve
# 1. The total number of votes 369711
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election by popular vote

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to an indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Create total vote counter
total_votes = 0

# Create list of candidates
candidate_options = []

#Create dictionary of candidates vote totals
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

	# print each row in the csv file
    for row in file_reader:
		# add to the total vote count
        total_votes += 1

		# print the candidate name from each row
        candidate_name = row[2]

        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
			#add candidate name to candidate list
            candidate_options.append(candidate_name)

			# Tracking for candidates vote counts
            candidate_votes[candidate_name] = 0
	
	    # add votes to that candidates count 
        candidate_votes[candidate_name] +=1


        
# print candidate vote dictionary
print(candidate_votes)

# Determine percentage of votes by looping through the counts
# Go through the candidate list
for candidate_name in candidate_votes:
    # Retrieve candidate vote count
	votes = candidate_votes[candidate_name]

	# Calculate percentage of votes
	vote_percentage = float(votes) / float(total_votes) * 100

	# Print candidate name and percentage of votes
	print(f"{candidate_name}: received {vote_percentage:4.1f}% of the vote")







  

