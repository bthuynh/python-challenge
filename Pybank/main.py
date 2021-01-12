import os
import csv

Date = []
Profit = []
Changelist = []


csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        Date.append(row[0])
        Profit.append(int(row[1]))

for x in range(len(Profit)-1):
    Change = Profit[x+1] - Profit[x]
    Changelist.append(Change)

Total_Months = len(Date)
Total_Profits = sum(Profit)
Avg_Change = round(sum(Changelist)/len(Changelist), 2)
Increase = max(Changelist)
Decrease = min(Changelist)
Increaseindex = Changelist.index(Increase)
Decreaseindex = Changelist.index(Decrease)
MaxDate = Date[Increaseindex+1]
MinDate = Date[Decreaseindex+1]



print("Financial Analysis")
print("---------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Profits}")
print(f"Average Change: ${Avg_Change}")
print(f"Greatest Increase in Profits: {MaxDate} (${Increase})")
print(f"Greatest Decrease in Profits: {MinDate} (${Decrease})")


analysis = os.path.join("analysis","Pybank.txt")
file = open(analysis, 'w')

file.writelines("Financial Analysis"+'\n')
file.writelines("---------------------"+'\n')
file.writelines(f"Total Months: {Total_Months}"+'\n')
file.writelines(f"Total: ${Total_Profits}"+'\n')
file.writelines(f"Average Change: ${Avg_Change}"+'\n')
file.writelines(f"Greatest Increase in Profits: {MaxDate} (${Increase})"+'\n')
file.writelines(f"Greatest Decrease in Profits: {MinDate} (${Decrease})"+'\n')
