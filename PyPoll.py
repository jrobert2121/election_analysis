# Data needed to retrieve
# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election by popular vote

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to an indirect path to save the file
file_to_save = os.path.join("analysis","election_analysis.txt")

# Create total vote counter
total_votes = 0

# Create list of candidates
candidate_options = []

#Create dictionary of candidates vote totals
candidate_votes = {}

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        # get the candidate name from each row
        candidate_name = row[2]

        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)

            # Tracking for candidates vote counts
            candidate_votes[candidate_name] = 0
    
        # add votes to that candidates count 
        candidate_votes[candidate_name] +=1

# Save results to text file
with open (file_to_save, "w") as txt_file:
    # print results to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    # Save the final vote count to text file
    txt_file.write(election_results)

        
    # print candidate vote dictionary
    #print(candidate_votes)

    # Determine percentage of votes by looping through the counts
    # Go through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve candidate vote count
        votes = candidate_votes[candidate_name]

        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Create variable for candidate results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print candidate results to terminal
        print(candidate_results)

        # print candidates results to text file
        txt_file.write(candidate_results)
        
            # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                
            # If true then set winning count = votes and winning percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate = to candidate name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"_________________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"_________________________\n")
    #print(winning_candidate_summary)






  

