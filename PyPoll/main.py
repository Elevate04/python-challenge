import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

Total_Votes = []
Candidates = []
Charles_Casper_Stockham_Vote_Total = []
Charles = 0
Diana_DeGette_Vote_Total = []
Diana = 0
Raymon_Anthony_Doane_Vote_Total = []
Raymon = 0


with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for row in csv_reader:
        Total_Votes.append(row[0])
        Candidates.append(row[2])
        
        if (row[2]) == "Charles Casper Stockham":
            Charles = Charles + 1
        elif (row[2]) == "Diana DeGette":
            Diana = Diana + 1
        else:
            Raymon = Raymon + 1
        
    Charles_Casper_Stockham_Vote_Total = (Charles/len(Total_Votes)) * 100
    Charles_Casper_Stockham_Vote_Total = round(Charles_Casper_Stockham_Vote_Total, 3)
    
    Diana_DeGette_Vote_Total = (Diana/len(Total_Votes)) * 100
    Diana_DeGette_Vote_Total = round(Diana_DeGette_Vote_Total, 3)
    
    Raymon_Anthony_Doane_Vote_Total = (Raymon/len(Total_Votes) * 100)
    Raymon_Anthony_Doane_Vote_Total = round(Raymon_Anthony_Doane_Vote_Total, 3)
    
    if Charles > Diana and Charles > Raymon:
        Winner = "Winner: Charles Casper Stockham"
    elif Diana > Charles and Diana > Raymon:
        Winner = "Winner: Diana DeGette"
    else:
        Winner = "Winner: Raymon Anthony Doane"
        
    
    print("Election Results")
    print("-----------------")
    print(f"Total Votes: {(len(Total_Votes))}")
    print("-----------------")
    print(f"Charles Casper Stockham:{Charles_Casper_Stockham_Vote_Total}% {Charles}")
    print(f"Diana DeGette:{Diana_DeGette_Vote_Total}% {Diana}")
    print(f"Raymon Anthony Doane:{Raymon_Anthony_Doane_Vote_Total}% {Raymon}")
    print("-----------------")
    print(Winner)
    
output_file = os.path.join("PyPoll", "Resources", "election_data_text")

with open (output_file, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------")
    file.write("\n")
    file.write(f"Total Votes: {(len(Total_Votes))}")
    file.write("\n")
    file.write(f"Charles Casper Stockham:{Charles_Casper_Stockham_Vote_Total}% {Charles}")
    file.write("\n")
    file.write(f"Diana DeGette:{Diana_DeGette_Vote_Total}% {Diana}")
    file.write("\n")
    file.write(f"Raymon Anthony Doane:{Raymon_Anthony_Doane_Vote_Total}% {Raymon}")
    file.write("\n")
    file.write("----------------")
    file.write("\n")
    file.write(Winner)
    