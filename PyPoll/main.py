import os
import csv
electioncsv= os.path.join("Resources","election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
votes = []
vote_percent = []

with open(electioncsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
        
    for can in set(candidatelist):
        unique_candidate.append(can)
        i = candidatelist.count(can)
        votes.append(i)
        j = (i/count)*100
        vote_percent.append(j)
        
    winning_vote_count = max(votes)
    winner = unique_candidate[votes.index(winning_vote_count)]
    
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(votes[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

results = os.path.join("analysis", "election_data.txt")
with open(results, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(votes[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")