import csv
from numpy import True_
from statsapi import player_stats,player_stat_data,lookup_player
from baseball_scraper import playerid_lookup

def num_names(PlayerName):
    count=1
    for i in range(0,len(PlayerName)):
        if PlayerName[i] == " ":
            count+=1
    return count

#HACK There has to be a better way to do this
def Period_Check(PlayerName):
    if num_names(PlayerName) == 2:
        for i in range(0,len(PlayerName)):
            if PlayerName[i] == ".":
                PlayerFirstName,PlayerLastName = PlayerName.split(" ")
                idx = PlayerFirstName.index(".")+1
                PlayerFirstName = PlayerFirstName[:idx]+" "+PlayerFirstName[idx:]
                NewPlayerName = PlayerFirstName +" " + PlayerLastName
                return NewPlayerName
    return PlayerName

def Player_Dataframe_Fetch(PlayerName):
    PlayerName = Period_Check(PlayerName)
    try:
        if num_names(PlayerName) == 3:
            pname0,pname1,pname2 = PlayerName.split(" ")
            PlayerFirstName = pname0 + " " + pname1
            PlayerLastName = pname2
        else:
            PlayerFirstName,PlayerLastName=PlayerName.split(" ")
        Player_ID_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)
        return Player_ID_Dataframe
    except ValueError as e:
        print(f'Problem searching for {PlayerName}\nerror: {e}')

def Get_MLB_ID(PlayerName):
    "Because I'm Lazy"
    try:
        PlayerJson = lookup_player(PlayerName)
        PlayerID = PlayerJson[0]['id']
        return PlayerID
    except IndexError as e:
        print (f'Problem searching for {PlayerName}\nerror: {e}')
    

def Get_BBRef_ID(PlayerName):
    "Because now I'm thinking ahead"
    Player_ID_Dataframe = Player_Dataframe_Fetch(PlayerName)

    SanitizedIDFrame = Player_ID_Dataframe.loc[Player_ID_Dataframe['mlb_played_last']==2021]
    BBRefKey = SanitizedIDFrame['key_bbref']

    SanitizedBBRefKey = BBRefKey.to_string(index=False)
    return SanitizedBBRefKey

#print(Get_BBRef_ID("Chi Chi Gonzalez"))

#NOTE Don't know why self harmed the fuction
#NOTE Relies on external database; will need to be updated occasionally
def Find_Fangraph_ID(player_name):
    #loop through the csv list
    FanGraphsCSV = csv.reader(open('FanGraphs_Players_IDs_2021.csv', "r"), delimiter=",")
    for row in FanGraphsCSV: #Not reading in init file for some reason?
        #if current rows 2nd value is equal to input, print that row
        if player_name == row[0]:
            FGid = row[2]
            #print(FGid)
            return int(FGid)