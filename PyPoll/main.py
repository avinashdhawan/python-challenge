#*****PYTHON POLL*****

#import os module
import os

#import csv module
import csv

csvdata = os.path.join('..', 'Resources', 'election_data.csv')


Voter_ID = []
County = []
Candidate = []


with open(csvdata) as csvfile:

#csv reader read file based on column separated values 
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)



    for row in csvreader:
       #extract Voter ID 
       Voter_ID.append(row[0])

       #extract County
       County.append(row[1])
       
       #extract Candidate
       Candidate.append(row[2])


#csvlength = len(csvreader)
Num_of_Voters = len(Voter_ID)        
Num_of_Counties = len(County)
Num_of_Candidates = len(Candidate)

print(Num_of_Voters)
print(Num_of_Counties)
print(Num_of_Candidates)
#print(csvreader)


def unique(CandidateList):
    unique_Candidates = []

    for x in CandidateList: 
        # check if exists in unique_list or not 
        if x not in unique_Candidates: 
            unique_Candidates.append(x)

    for x in unique_Candidates: 
        
        count = Candidate.count(x)
        percent = round(count*100/Num_of_Voters,3)
        winner = count.index(max(count)
        print(x, percent, count) 

unique(Candidate)


#MaxIndex = max(ProfitorLoss).index

# for i in range(len(ProfitorLoss)):
    
#     previous = ProfitorLoss[i-1]

#     current = ProfitorLoss[i]
        
#     difference = current - previous
#     average_difference.append(difference)


# Average = (sum(average_difference) - average_difference[0]) / (int(Months) -1)
# Maximum = max(average_difference)
# Minimum = min(average_difference)
# MaxIndex = average_difference.index(max(average_difference))
# MinIndex = average_difference.index(min(average_difference))

# #MaxIndex + 1 because average difference ignores first cell as difference of 2 cells
# MaxDate = MonthYear[MaxIndex]
# MinDate = MonthYear[MinIndex]

# # print("Financial Analysis")
# # print('---------------------------------')
# # print("Total Months: ", Months)
# # print("Total: $", Total)
# # print("The Average Change: $", round(Average,2))
# # print("Greatest Increase in Profits: ", MaxDate, "($", Maximum,")")
# # print("Greatest Decrease in Profits: ", MinDate, "($", Minimum,")")

# #print summary to screen
# print(f"""Financial Analysis
# ---------------------------------
# Total Months: {Months}
# Total: ${Total}
# The Average Change: $ {round(Average,2)}
# Greatest Increase in Profits: {MaxDate} ($ {Maximum} )
# Greatest Decrease in Profits: {MinDate} ($ {Minimum} )
# """)

# #write summary to text file
# Summary_File = open("Summarized_main.txt", "w")
# Summary_File.write(f"""Financial Analysis
# ---------------------------------
# Total Months: {Months}
# Total: ${Total}
# The Average Change: $ {round(Average,2)}
# Greatest Increase in Profits: {MaxDate} ($ {Maximum})
# Greatest Decrease in Profits: {MinDate} ($ {Minimum})
# """)
# Summary_File.close()








