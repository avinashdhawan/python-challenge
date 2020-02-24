#import os module
import os

#import csv module
import csv

csvdata = os.path.join('..', 'Resources', 'budget_data.csv')


MonthYear = []
ProfitorLoss = []
average_difference = []

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


#MaxIndex = max(ProfitorLoss).index

for i in range(len(ProfitorLoss)):
    
    previous = ProfitorLoss[i-1]

    current = ProfitorLoss[i]
        
    difference = current - previous
    average_difference.append(difference)


Average = (sum(average_difference) - average_difference[0]) / (int(Months) -1)
Maximum = max(average_difference)
Minimum = min(average_difference)
MaxIndex = average_difference.index(max(average_difference))
MinIndex = average_difference.index(min(average_difference))

#MaxIndex + 1 because average difference ignores first cell as difference of 2 cells
MaxDate = MonthYear[MaxIndex]
MinDate = MonthYear[MinIndex]

Summary_File = (MonthYear, ProfitorLoss, average_difference)

Output = os.path.join("Summarized_main.csv")

with open(Output, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(Summary_File)


print("Financial Analysis")
print('---------------------------------')
print("Total Months: ", Months)
print("Total: $", Total)
print("The Average Change: $", round(Average,2))
print("Greatest Increase in Profits: ", MaxDate, "($", Maximum,")")
print("Greatest Decrease in Profits: ", MinDate, "($", Minimum,")")
#print(MaxIndex)





