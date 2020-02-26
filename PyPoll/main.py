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


#number of voters
Num_of_Voters = len(Voter_ID)        

#print summary to screen
print(f"""Election Results
---------------------------------
Total Votes: {Num_of_Voters},
---------------------------------
""")

def unique(CandidateList):
    unique_Candidates = []

    for x in CandidateList: 
        # check if exists in unique_list or not 
        if x not in unique_Candidates: 
            unique_Candidates.append(x)

    for x in unique_Candidates: 
        
       count = Candidate.count(x)
       percent = round(count*100/Num_of_Voters,3)
       print(x,": ", percent,"% ", "(",count,")")  
unique(Candidate)
#print part 2 of summary to screen
print(f"""
---------------------------------
Winner: {""}
---------------------------------
""") 




# #write summary to text file
# Summary_File = open("Summarized_main.txt", "w")
# Summary_File.write(f"""Election Results
# ---------------------------------
# Total Votes: {Num_of_Voters},
# ---------------------------------
# """)
# Summary_File.write(x,": ", percent,"% ", "(",count,")")
# #print part 2 of summary to text file
# Summary_File.write(f"""
# ---------------------------------
# Winner: {""}
# ---------------------------------
# """) 
# Summary_File.close()








