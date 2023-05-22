import csv
import os
import pandas as pd


CSVPATH = os.path.join('Resources','budget_data.csv')
ANALYSISPATH = os.path.join('Analysis','analysis.txt')

total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(CSVPATH) as csvfile:
#    ## excel_lines = file.read()
#    ## print(excel_lines)
#     print(type(excel_lines))
    
    csvreader = csv.reader(csvfile, delimiter=',')
  

    header = next(csvreader)
    first_row = next(csvreader)
    current_profit_loss = int(first_row[1])
    
    total_profit_loss += current_profit_loss

    previous_profit_loss = current_profit_loss

    total_months += 1

    for row in csvreader:
        
        total_months += 1
        current_profit_loss = int(row[1])
        
        total_profit_loss += current_profit_loss

        change = current_profit_loss - previous_profit_loss
        changes.append(change)
        
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        
        elif change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
        previous_profit_loss = current_profit_loss
 
average_change = sum(changes) / len(changes)
        
msg =(
        "Financial Analysis\n"
        "-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_loss}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)



with open(ANALYSISPATH, 'w') as analysis_file:
    analysis_file.write(msg)

print(msg)




