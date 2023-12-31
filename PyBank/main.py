import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

months=[]
changes=[]


TotalProfitLoss=0
CurrentPL=0
LastProfitLoss=0
TotalProfitChange=0
MonthCount = 0
PLChange= 0

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    header= next(csvfile)

    for row in csv_reader:
        MonthCount += 1

        CurrentPL = int(row[1])
        TotalProfitLoss += CurrentPL

        if (MonthCount ==1) :
            LastProfitLoss = CurrentPL

            continue

        else: 
            months.append(row[0])
            PLChange = CurrentPL - LastProfitLoss
            changes.append(PLChange)
            LastProfitLoss =CurrentPL

ChangeSum= sum(changes)
AverageChange= round(ChangeSum/(MonthCount-1),2)

max_change= max(changes)
max_loss= min(changes)
max_change_index=changes.index(max_change)
max_loss_index=changes.index(max_loss)
best_month= months[max_change_index]
worst_month=months[max_loss_index]

print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {MonthCount}\n")
print(f"Total: ${TotalProfitLoss}\n")
print(f"Average Change: ${AverageChange}/n")
print(f"Greatest Increase in Profits: {best_month} (${max_change})\n")
print(f"Greatest Decrease in Losses: {worst_month} (${max_loss})\n")
                      
newbudget_file= os.path.join("Analysis", "budget_data.txt")
with open(newbudget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {MonthCount}\n")
    outfile.write(f"Total:  ${TotalProfitLoss}\n")
    outfile.write(f"Average Change:  ${AverageChange}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${max_loss})\n")
