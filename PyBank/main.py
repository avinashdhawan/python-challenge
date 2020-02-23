#import os module
import os

#import csv module
import csv

csvdata = os.path.join('..', 'Resources', 'budget_data.csv')


MonthYear = []
ProfitorLoss = []

with open(csvdata) as csvfile:

#csv reader read file based on column separated values 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)



    for row in csvreader:
       #extract date 
       MonthYear.append(row[0])

       #extract profit or loss
       ProfitorLoss.append(int(row[1]))


Months = len(MonthYear)        
Total = sum(ProfitorLoss)
Average = Total / Months
Maximum = max(ProfitorLoss)
Minimum = min(ProfitorLoss)
MaxIndex = max(ProfitorLoss).index



print(Total)
print(Months)
print(round(Average))
print(Maximum)
print(Minimum)
print(MaxIndex)





