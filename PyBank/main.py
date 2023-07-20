import os
import csv

#Create path to access neccessary csv file

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []

Net_Total = []

Average_Change = []

#Open csv file and skip the header
with open (budget_data) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
#loop through each row and append the information in the proper list
    for row in csv_reader:
        
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        
#loop through total profit to calculate to Profit change but we subtract 1 to be within range
    for x in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[x+1] - total_profit[x])
        
#Calculate necessary variable to conduct Financial Anlysis
Net_Total.append(sum(total_profit))
Max_Value = max(monthly_profit_change)
Min_Value = min(monthly_profit_change)
Max_Month = monthly_profit_change.index(max(monthly_profit_change))
Min_Month = monthly_profit_change.index(min(monthly_profit_change))
Average_Change.append(round(sum(monthly_profit_change)/len(monthly_profit_change)))

#print results in terminal

print('Financial Analysis')
print('-------------------')
print(f'Total Months:{len(total_months)}')
print(f'Total:${sum(Net_Total)}')
print(f'Average Change {(sum(Average_Change))}')
print(f"Greatest Increase in Profits: {(total_months[Max_Month+1])} ${Max_Value}")
print(f'Greatest Decrease in Profits: {(total_months[Min_Month+1])} ${Min_Value}')

#Now create a path to output a text file with the results
Output_file = os.path.join("PyBank", "Resources", "Financial Analysis Text")

with open(Output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------")
    file.write("\n")
    file.write(f"Total Months: {(len(total_months))}")
    file.write("\n")
    file.write(f"Total:${sum(Net_Total)}")
    file.write("\n")
    file.write(f'Average Change {(sum(Average_Change))}')
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {(total_months[Max_Month+1])} ${Max_Value}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {(total_months[Min_Month+1])} ${Min_Value}")