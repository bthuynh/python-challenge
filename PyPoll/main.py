# You will be give a set of poll data called election_data.csv.
# The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------


import os
import csv


votes = []
candidate = []
kvote = 0
cvote = 0
lvote = 0
ovote = 0
name1 = "Khan"
name2 = "Correy"
name3 = "Li"
name4 = "O'Tooley"



csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        votes.append(row[0])
        candidate.append(row[2])


for name in candidate:
    if name == name1:
        kvote = kvote + 1
    elif name == name2:
        cvote = cvote + 1
    elif name == name3:
        lvote = lvote + 1
    elif name == name4:
        ovote = ovote + 1

def most_frequent(candidate): 
    return max(set(candidate), key = candidate.count)


total_votes = len(votes)
winner = most_frequent(candidate)
knumber = round(int(kvote) / int(total_votes),2)
cnumber = round(int(cvote) / int(total_votes),2)
lnumber = round(int(lvote) / int(total_votes),2)
onumber = round(int(ovote) / int(total_votes),2)
kpercent = "{:.0%}".format(knumber)
cpercent = "{:.0%}".format(cnumber)
lpercent = "{:.0%}".format(lnumber)
opercent = "{:.0%}".format(onumber)




print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print(f"Khan: {kpercent} ({kvote})")
print(f"Correy: {cpercent} ({cvote})")
print(f"Li: {lpercent} ({lvote})")
print(f"O'Tooley: {opercent} ({ovote})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")


analysis = os.path.join("analysis","Pypoll.txt")
file = open(analysis, 'w')

file.writelines("Election Results"+'\n')
file.writelines("--------------------------"+'\n')
file.writelines(f"Total Votes: {total_votes}"+'\n')
file.writelines(f"Khan: {kpercent} ({kvote})"+'\n')
file.writelines(f"Correy: {cpercent} ({cvote})"+'\n')
file.writelines(f"Li: {lpercent} ({lvote})"+'\n')
file.writelines(f"O'Tooley: {opercent} ({ovote})"+'\n')
file.writelines("--------------------------"+'\n')
file.writelines("Winner: Khan"+'\n')
file.writelines("--------------------------"+'\n')