import csv
import os

csvpath = os.path.join('..','Resources','budget_data.csv')


total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

with open(csvpath) as file:
#    ## excel_lines = file.read()
#    ## print(excel_lines)
#     print(type(excel_lines))
    
    csvreader = csv.reader(file, delimiter=',')
    print(csvreader)

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
        

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
            










