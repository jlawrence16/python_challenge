import os
import csv

# Path to collect data

csvpath = os.path.join('Resources', 'budget_data.csv')

# Import data from /Resources/budget_data.csv (checked..works)

with open(csvpath) as csvfile:

    budget_data = csv.reader(csvfile, delimiter=',')  
    next(budget_data, None)
    

# Loop through the data
    total_amount=0
    total_months=0
    change_list=[]
    name_list=[]
    previous_value=1088983

    for row in budget_data:

        # Calculate total number of months
        
        total_months += 1

        # The net total amount of "Profit/Losses"
        total_amount +=int(row[1])

        #The changes in "Profit/Losses"
        
        current_value = int(row[1])
        change_list.append(current_value-previous_value)

        name_list.append(row[0])

        previous_value= int(row[1])


# Calculate changes in "Profit/Losses"

ave_change = round(sum(change_list)/(total_months-1),2)

# Calculate the greatest increase in profits (date and amount)

max_increase=max(change_list)
max_increase_index=change_list.index(max_increase)
max_increase_date=name_list[max_increase_index]

# Calculate the greatest decrease in profits (date and amount)

max_decrease=min(change_list)
max_decrease_index=change_list.index(max_decrease)
max_decrease_date=name_list[max_decrease_index]

# print out results

print("Financial Analysis")
print("---------------------------")
print(f'Total months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average change: $ {ave_change}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

# export text file with results

results_path = os.path.join('Analysis', "financial_analysis.txt")

with open(results_path, 'w') as text:
        text.write("Financial Analysis")
        text.write('\n')
        text.write('\n')
        text.write("---------------------------")
        text.write('\n')
        text.write(f'Average change: $ {ave_change}')
        text.write('\n')
        text.write(f'Total: ${total_amount}')
        text.write('\n')
        text.write(f'Average change: $ {ave_change}')
        text.write('\n')
        text.write(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
        text.write('\n')
        text.write(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')
        
        text.close()