# python-challenge
This is my first Python assignment that I have completed for the RICE University Virtual DataAnalytics Bootccamp. This assignment was challenging but also enabled me to practice my ability to import and read files as cvs, write 
 forloops,  utilize variables, use "f"function, use a [set], practice using "\n" add files in Git Bash and push them to GitHub. Print to the terminal, and write the output of the code into text file. This was a an amaizing introduction to Python and a real motivation to keep practicing, step out of my comfort zone and move forward with Python language. I am encouraged and motivated to move forward with  RICE University Virtual DataAnalytics Bootccamp. I had to commit many hours to put this together and I can say that I have enjoyed the journey. It's quite an achievement when I can see everything come together as I had envisioned.
I completed this assignment using python,csv, Git Bash and jupyter notebook.

# PyBank
In this portion of the project, i was required to create blank lists that were to be appended using a forloop that would then iterate throught the csv file that was provided. The results from that data was then applied the different functions that were in variables that had been created while running the syntax. A new file was created and the reults of the date was then saved in this file.

# PyPoll
For this portion, I used Jupyter notebook to write out my code. I find that this is easier for me to visualize and catch syntax errors. once I am done with my coding, I save the file as a Python file then take that file and add it to folders that were already created in Git Bash before I can push the files to GitHub. I was able to utilize these functions: forloop, index, "f", unique, average formulas and percentages. You can see below a quick snap on how everything was utilized.

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

 # Thank you for Reading My ReadMe.
 I appreciate your time to read my Readme. I am Looking for a career and also welcome different ideas, positive criticism and feedback.
