import os
import csv

election_data = os.path.join("election_data.csv")

candidates = []
number_votes = []
percent_votes = []
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1

    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(total_votes)}")
print("----------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print("----------------------------")
print(f"Winner: {winning_candidate}")
print("----------------------------")

analysis_text = open("analysis.txt", "w")
line1 = "Election Results"
line2 = "----------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "----------------------------"
analysis_text.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
    analysis_text.write('{}\n'.format(line))
line5 = "----------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "----------------------------"
analysis_text.write('{}\n{}\n{}\n'.format(line5,line6,line7))


