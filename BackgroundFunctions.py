import csv
from statsapi import player_stats,player_stat_data,lookup_player
from baseball_scraper import playerid_lookup

def num_names(player_name):
    count=1
    for i in range(0,len(player_name)):
        if player_name[i] == " ":
            count+=1
    return count

def check_num_names(PlayerName):
    try:
        if num_names(PlayerName) == 3:
            pname0,pname1,pname2 = PlayerName.split(" ")
            PlayerFirstName = pname0 + " " + pname1
            PlayerLastName = pname2
        else:
            PlayerFirstName,PlayerLastName=PlayerName.split(" ")
        Player_ID_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)
        #print(Player_ID_Dataframe)
        return Player_ID_Dataframe

    except ValueError as e:
        print(f'Problem searching for {PlayerName}\nerror: {e}')

def Get_MLB_ID(PlayerName):
    "Because I'm Lazy"
    PlayerJson = lookup_player(PlayerName)
    PlayerID = PlayerJson[0]['id']
    return PlayerID

def Get_BBRef_ID(PlayerName):
    "Because now I'm thinking ahead"
    Player_ID_Dataframe = check_num_names(PlayerName)

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