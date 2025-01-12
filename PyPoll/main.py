#import modules
import  os
import csv

#Path to data file
election_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#open csv, set reader
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read and print header
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    #Define variables
    votes = []
    candidates = []
    #empty dictionary to hold lists
    candidate_total_votes = {}

    #calculate total votes
    for row in csv_reader:
        votes.append(row[2])
        #assign count of total votes to variable
        total_votes = len(votes)
        #if the candidate name in row is not in the list
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_total_votes[row[2]] = 1
            #continue adding to count if name has been appended to candidates list
        else:
            candidate_total_votes[row[2]] += 1


#Print text and total votes results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")

#print dictonary values and calculate percentage of votes
for candidates, votes, in candidate_total_votes.items():
    print(f'{candidates}: {round((votes/total_votes)*100,2)}% {votes}')

#define winner get value of winner name from dictionary
winner = max(candidate_total_votes, key=candidate_total_votes.get)
#print winner
print("--------------------------")
print(f'Winner: {winner}')
print("--------------------------")

#print output to text file
#set variable for output file
output_file = os.path.join('..', 'PyPoll', 'Analysis', 'final_analysis.txt')

#open output file and add reporting
with open(output_file, "w") as outfile:
    writer = csv.writer(outfile)

    outfile.write("Election Results\n")
    outfile.write("--------------------------\n")
    outfile.write((f"Total Votes: {total_votes}"))
    outfile.write('\n')
    outfile.write("--------------------------\n")
    #use for loop to print values from dictionary in table
    for candidates, votes, in candidate_total_votes.items():
        outfile.write(f'{candidates}: {round((votes/total_votes)*100,2)}% {votes}')
        outfile.write('\n')
    outfile.write("--------------------------\n")
    outfile.write(f'Winner: {winner}')