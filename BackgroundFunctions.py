import csv

def num_names(player_name):
    count=1
    for i in range(0,len(player_name)):
        if player_name[i] == " ":
            count+=1
    return count

#Don't know why self harmed the fuction
def Find_Fangraph_ID(player_name):
    #loop through the csv list
    FanGraphsCSV = csv.reader(open('FanGraphs_Players_IDs_2021.csv', "r"), delimiter=",")
    for row in FanGraphsCSV: #Not reading in init file for some reason?
        #if current rows 2nd value is equal to input, print that row
        if player_name == row[0]:
            FGid = row[2]
            #print(FGid)
            return int(FGid)