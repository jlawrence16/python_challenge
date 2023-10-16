import os
import csv

# path to data file

csvpath = os.path.join('Resources', 'election_data.csv')

# import data from /Resources/election_data.csv 

with open(csvpath) as csvfile:

    election_data = csv.reader(csvfile, delimiter=',')  
    next(election_data, None)
     
# loop through the data
    total_votes=0
    votes_stockham = 0
    votes_degette = 0
    votes_doane = 0
    votes_other = 0
    
    for row in election_data:

        # calculate total number of votes
        
        total_votes += 1  

        # adding one vote to a candidates total each time their name appears

        if row[2] == ("Charles Casper Stockham"):
            votes_stockham +=1
        elif row[2] == ("Diana DeGette"):
            votes_degette +=1
        elif row[2]== ("Raymon Anthony Doane"):
            votes_doane +=1
        else:
            votes_other +=1

# calculate percentages

percent_stockham = votes_stockham/total_votes*100
percent_degette = votes_degette/total_votes*100
percent_doane = votes_doane/total_votes*100

# calculate winner

election_results = {'Charles Casper Stockham': votes_stockham, 'Diana DeGette': votes_degette, 'Raymon Anthony Doane': votes_doane}
winner=max(election_results, key=election_results.get)


# print out results

print("Election Results")
print("---------------------------")
print(f'Total votes: {total_votes}')
print("---------------------------")
print(f'Charles Casper Stockham: {round(percent_stockham, 3)}% ({votes_stockham})')
print(f'Diana DeGette: {round(percent_degette, 3)}% ({votes_degette})')
print(f'Raymon Anthony Doane: {round(percent_doane, 3)}% ({votes_doane})')
print("---------------------------")
print(f'Winner: {winner}')
print("---------------------------")



# export text file with results

results_path = os.path.join('Analysis', "election_results.txt")

with open(results_path, 'w') as text:
    text.write("Election Results")
    text.write('\n')
    text.write("---------------------------")
    text.write('\n')
    text.write(f'Total votes: {total_votes}')
    text.write('\n')
    text.write("---------------------------")
    text.write('\n')
    text.write(f'Charles Casper Stockham: {round(percent_stockham, 3)}% ({votes_stockham})')
    text.write('\n')
    text.write(f'Diana DeGette: {round(percent_degette, 3)}% ({votes_degette})')
    text.write('\n')
    text.write(f'Raymon Anthony Doane: {round(percent_doane, 3)}% ({votes_doane})')
    text.write('\n')
    text.write("---------------------------")
    text.write('\n')
    text.write(f'Winner: {winner}')
    text.write('\n')
    text.write("---------------------------")
    text.write('\n')

    text.close()