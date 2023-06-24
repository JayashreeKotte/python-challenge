#Import modules
import os
import csv

#Path to collect data from Resources folder 
election_csv = os.path.join('PyPoll/Resources/election_data.csv')

#Intialize variables to store analysis results
total_votes = 0
candidates_list = []
candidate_votes = {}
individual_votes = []
percentages = []
election_winner = ''

#Read the CSV file
with open(election_csv, 'r') as election: 
    election_reader = csv.reader(election, delimiter=',')
    
    #Omit the header line in csv file
    header = next(election_reader)
    
    #Calculate the total number of votes cast 
    for row in election_reader:
        total_votes += 1
        
        #Create a list of all candidates from Candidate colum in the csv file
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            
            #Initialize the number of votes for each candidate to 0
            candidate_votes[row[2]] = 0
        
        #Track the number of votes each candidate received 
        candidate_votes[row[2]] = candidate_votes[row[2]] + 1
    
    #Extract the total votes per candidate into a list
    individual_votes = [*candidate_votes.values()] 
    
    #Compute percentage of votes per candidate using List comprehension
    percentages = [round((i/total_votes)*100, 3) for i in individual_votes]
    
    #Extract the name of the candidate with maximum votes as the winner
    election_winner = max(candidate_votes, key=candidate_votes.get)

#Generate the results of the analysis and save them in a variable
output = (f"                            \n"
      f"Election Results \n"
      f"                            \n"
      f"----------------------------\n"
      f"                            \n"
      f"Total Votes: {total_votes} \n"
      f"                            \n"
      f"----------------------------\n"
      f"                            \n"
      f"{candidates_list[0]}: {percentages[0]}% ({individual_votes[0]})\n"
      f"{candidates_list[1]}: {percentages[1]}% ({individual_votes[1]})\n"
      f"{candidates_list[2]}: {percentages[2]}% ({individual_votes[2]})\n"
      f"                            \n"
      f"----------------------------\n"
      f"                            \n"
      f"Winner: {election_winner}"
      f"                            \n")

#Print the final results to the terminal 
print(output)

#Specify path to store the output file 
output_file = os.path.join('PyPoll/Analysis/election_results.txt')

#Open and Write the final results to the output text file 
with open(output_file, "w") as txt_file:
    txt_file.write(output)