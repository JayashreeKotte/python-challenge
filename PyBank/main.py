#Import modules
import os
import csv

#Path to collect data from Resources folder 
budget_csv = os.path.join('Resources/budget_data.csv')

#Intialize variables to store analysis results
total_months = 0
total = 0 
net_change = 0
net_change_list = []
month_change = []
avg_change = 0
max_change = 0
min_change = 0
max_month = " "
min_month = " "
  
#Read the CSV file
with open(budget_csv, 'r') as budget: 
    budget_reader = csv.reader(budget, delimiter=',')
    
    #Omit the header line in csv file
    header = next(budget_reader)  
    
    #Save the first profit/loss value in a variable to aid in calculating net change
    first_row = next(budget_reader)
    prev_value = int(first_row[1])
    total_months = 1
    total = int(first_row[1])
    
    #Iterate and analyse the dataset
    for row in budget_reader:
        
        #Assign values to variables for readability
        month = row[0]
        value = int(row[1])
        
        #Calculate the total months 
        total_months += 1
        
        #Calculate total profit/loss value for the entire period
        total += value
        
        #Calculate the net change for each month in the dataset and append to a list
        net_change = value - prev_value
        prev_value = value
        net_change_list.append(net_change)
        
        #Add the months for net changes into a different list 
        month_change.append(month)

    #Calculate the average change in profits and round it to two decimal points       
    avg_change = round(sum(net_change_list)/len(net_change_list), 2)  

    #Extract the value and month for Greatest Increase in Profits
    max_change = max(net_change_list)
    max_month = month_change[net_change_list.index(max_change)]

    #Extract the value and month for Greatest Decrease in Profits  
    min_change = min(net_change_list)
    min_month = month_change[net_change_list.index(min_change)]
    
#Generate results and save them as variable: output 
output = (f"   \n"
    f"Financial Analysis \n"
    f"  \n"
    f"------------------------------\n"
    f"    \n"
    f"Total Months: {total_months} \n"
    f"    \n"
    f"Total: ${total} \n"
    f"    \n"
    f"Average Change: ${avg_change} \n" 
    f"    \n"
    f"Greatest Increase in Profits: {max_month} (${max_change}) \n" 
    f"    \n"
    f"Greatest Decrease in Profits: {min_month} (${min_change}) \n" )
    
#Print the final results to the terminal 
print(output)

#Path to save results(output) to Analysis folder
output_file = os.path.join('Analysis/budget_analysis.txt') 
    
#Export the financial analysis results as an output text file
with open(output_file, "w") as txt_file:
        txt_file.write(output)