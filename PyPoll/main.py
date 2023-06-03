import csv
import os

CSVPATH = os.path.join('Resources','election_data.csv')
ANALYSISPATH = os.path.join('Analysis','elections_analysis.txt')

total_votes = 0

candidates_votes = {}
candidate_options = []
percentage_of_votes = 0
winner = ""
winning_count = 0


os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(CSVPATH) as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    header = next(csvreader)


    for row in csvreader:
        candidate_name = str(row[2]) 
        total_votes += 1

        if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)
             candidates_votes[candidate_name] = 0
    
        candidates_votes[candidate_name] += 1

with open(ANALYSISPATH, 'w') as analysis_file:
    analysis_file.write(f'Election Results\n')
    analysis_file.write(f'----------------------------\n')
    analysis_file.write(f'Total Votes: {total_votes}\n')
    analysis_file.write(f'----------------------------\n')

    for candidate, votes in candidates_votes.items():
        percentage_of_votes = (votes / total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winner = candidate

        analysis_file.write(f'{candidate}: {percentage_of_votes:.3f}% ({votes})\n')

    analysis_file.write(f'----------------------------\n')
    analysis_file.write(f'Winner: {winner}\n')
    analysis_file.write(f'----------------------------\n')


with open(ANALYSISPATH, 'r') as analysis_file:
    print(analysis_file.read())



        
        
       


             



        

