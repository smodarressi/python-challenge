#Dependencies/Modules
import os
import csv

#path to election data to open csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

#open csv data to report on
with open(election_data_csv, newline='') as election_data:
    election_reader = csv.reader(election_data, delimiter=',')
    
    #save header if I need it, and move cursor past header row
    election_header = next(election_reader)

    #this for loop is the vote counter, and appends all voted candidates to a list
    #could omit the counter and call a len() on the created list, but i kept it for learning purposes

    vote_counter = 0
    all_candidates_voted_on = []
    for num_vote in election_reader:
        vote_counter += 1
        all_candidates_voted_on.append(num_vote[2])
        
    #use set to get a unique tuple of candidates
    #this set is unordered, it's only used to get a list of unique candidates from the list
    candidates_set = set(all_candidates_voted_on)

    #convert to list to iterate
    candidates_set_list = list(candidates_set)

    #used len() to tell me how many candidates in my list
    number_of_candidates = len(candidates_set_list)

    #created 2 for loops
    #first loop creates a dictionary to count into 
    #second loop creates a dictionary from the first dictionary loop to evalue to percentage
    #second loop will also find highest percentage and the winner based on that percentage
    candidate_votes = dict()
    candidate_vote_percentage = dict()
    highest_percent = 0
    winner = ""
    for candidate in all_candidates_voted_on:
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
    for candidate in candidates_set_list:
        candidate_vote_percentage[candidate] = (candidate_votes[candidate]/vote_counter * 100)
        if (highest_percent < candidate_vote_percentage[candidate]):
            highest_percent = candidate_vote_percentage[candidate]
            winner = candidate

#used f notation for election results
#.2f is a float to two decimal places
election_results = (f"""    
Election Results
-------------------------
Total Votes: {vote_counter}
-------------------------
Khan: {candidate_vote_percentage["Khan"]:.2f}% ({candidate_votes["Khan"]})
Correy: {candidate_vote_percentage["Correy"]:.2f}% ({candidate_votes["Correy"]})
Li: {candidate_vote_percentage["Li"]:.2f}% ({candidate_votes["Li"]})
O'Tooley: {candidate_vote_percentage["O'Tooley"]:.2f}% ({candidate_votes["O'Tooley"]})
-------------------------
Winner: {winner}
-------------------------
```
""")

#prints election results to terminal
print(election_results)

#writes election_result.txt to same folder as main.py
with open('election_result.txt', 'w', newline='') as election_result:
      election_result.write(election_results)

#print test of each value
# print(all_candidates_voted_on[0:5])
# print(candidates_set_list)
# print(vote_counter)
# print(number_of_candidates)
# print(candidate_votes)
# print(candidate_vote_percentage)
# print(candidate_vote_percentage.items())
# print(highest_percent)
# print(winner)
