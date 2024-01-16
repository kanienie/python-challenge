
import csv

budget_data = 'Resources/budget_data.csv'

total_months = 0
net_total_amount = 0
profit_loss = []
profit_loss_changes = []
dates = []

# Read csv file
with open(budget_data, 'r') as file: 
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)
    
    for row in csv_reader:
        
        # Total Number of months
        total_months += 1
        
        # Net total amount of profit/loss
        profit_loss_int = int(row[1])
        net_total_amount += profit_loss_int
        
        # Append profit/loss and dates to list
        profit_loss.append(profit_loss_int)
        dates.append(row[0])
    
    
# Calculating Changes
for index in range(1, len(profit_loss)):
    profit_loss_changes.append(profit_loss[index] - profit_loss[index - 1])

average_change = sum(profit_loss_changes)/len(profit_loss_changes)
average_change = round(average_change, 2)
    


greatest_increase = max(profit_loss_changes)

max_index = profit_loss_changes.index(greatest_increase)
greatest_increase_date = dates[max_index + 1]


greatest_decrease = min(profit_loss_changes)

min_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_date = dates[min_index + 1]


print('Financial Analysis\n')
print('--------------------------\n')
print('Total Months: ' + str(total_months) + '\n')
print('Total: $' + str(net_total_amount) + '\n')
print('Average Change: $' + str(average_change) + '\n')
print('Greatest Increase in Profits: ' + greatest_increase_date + '($' + str(greatest_increase) + ')\n')
print('Greatest Decrease in Profits: ' + greatest_decrease_date + '($' + str(greatest_decrease) + ')\n')


with open('Analysis/FinancialAnalysis.txt', 'w') as output:
    output.write('Financial Analysis\n\n')
    output.write('--------------------------\n\n')
    output.write('Total Months: ' + str(total_months) + '\n\n')
    output.write('Total: $' + str(net_total_amount) + '\n\n')
    output.write('Average Change: $' + str(average_change) + '\n\n')
    output.write('Greatest Increase in Profits: ' + greatest_increase_date + '($' + str(greatest_increase) + ')\n\n')
    output.write('Greatest Decrease in Profits: ' + greatest_decrease_date + '($' + str(greatest_decrease) + ')')

