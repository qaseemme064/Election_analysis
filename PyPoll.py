# the data we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. the percentage of votes each candidates won 
# 4. the total number of each candidate won 
# 5. the winner of the election based on popular vote


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt") 

# 1. Initialize a total vote counter.
total_votes = 0

#Candiates option
candidate_options = []

#declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes +=1
        #print candidate name from each row
        candidate_name=row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print the candidate list.        
    #print(candidate_votes)
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        votes_percentage=float(votes)/float(total_votes) * 100
        #print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (votes_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent=vote_percentage.
            winning_count = votes
            winning_percentage = votes_percentage
        #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    #print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)