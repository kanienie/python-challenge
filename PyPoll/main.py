
import csv

election_data = 'Resources/election_data.csv'

total_ballots = 0
votes_by_candidate = {}

# Read csv file
with open(election_data, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Assuming the first row contains headers
    headers = next(csv_reader)

    # Total Number of Votes and Votes by Candidate
    for row in csv_reader:
        total_ballots += 1

        # List of Candidates who received votes
        candidate_index = headers.index("Candidate")
        candidate = row[candidate_index]

        # Update votes for each candidate
        if candidate in votes_by_candidate:
            votes_by_candidate[candidate] += 1
        else:
            votes_by_candidate[candidate] = 1

# Print the total number of ballots
print(f"Total Ballots: {total_ballots}")

# Get unique names of candidates using set
unique_candidates = set(votes_by_candidate.keys())

# Print the unique names of candidates
print("Unique Candidates:", unique_candidates)

# Print the percentage of votes each candidate won
for candidate in unique_candidates:
    percentage = (votes_by_candidate[candidate] / total_ballots) * 100
    print(f"{candidate}: {percentage:.3f}%({votes_by_candidate[candidate]})")

# Winner of the election based on popular vote
winner = max(votes_by_candidate, key=votes_by_candidate.get)
print(f"\nWinner: {winner} (Based on Popular Vote)")


with open('analysis/ElectionData.text','w' ) as output:
    output.write(f"Total Ballots: {total_ballots}\n")
    output.write(f"Unique Candidates:{unique_candidates} \n")
    
    for candidate in unique_candidates:
      percentage = (votes_by_candidate[candidate] / total_ballots) * 100
      output.write(f"{candidate}: {percentage:.3f}%({votes_by_candidate[candidate]})\n")
    
    output.write(f"Winner: {winner} (Based on Popular Vote)") 


    






