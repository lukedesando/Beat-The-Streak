## imports
from BackgroundFunctions import Get_BBRef_ID, Check_batting_or_pitching, rosterPlayers
import pandas as pd
from functools import partial
from datetime import date

#PlayerList = ['Casey Mize', "Juan Soto",'Robbie Ray']
CurrentYear = date.today().year
#PlayerName = "Juan Soto"
#batting_or_pitching = "pitching"
#year = 2021

#PlayerID = "corbipa01"

#XXX Reduce testing time by a few seconds by not going through the get ID function
def GenerateGamelogCSV(PlayerName = None,BBRefID=None,year=CurrentYear):
    BBRefID = Get_BBRef_ID(PlayerName)
    PlayerGameLogs = GenerateGamelog(PlayerName=PlayerName,BBRefID=BBRefID)

    PlayerGameLogs.to_csv("GameLogs "+ PlayerName + " " + BBRefID + ".csv",index=False)

def PrintGamelog(PlayerName = None,BBRefID=None,year=CurrentYear):
    BBRefID = Get_BBRef_ID(PlayerName)
    PlayerGameLogs = GenerateGamelog(PlayerName=PlayerName,BBRefID=BBRefID)
    print(PlayerGameLogs)


def GenerateGamelog(PlayerName = None,BBRefID=None,year=CurrentYear):
    if BBRefID == None:
        BBRefID = Get_BBRef_ID(PlayerName)

    batting_or_pitching, bat_or_pitch,b_or_p = Check_batting_or_pitching(BBRefID)

    GameLogsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3F\
id%3D{}%26t%3D{}%26year%3D{}&div=div_{}_gamelogs'''.format(BBRefID,b_or_p,year,batting_or_pitching)

    ## removes the junk out of the gamelogs
    PlayerGameLogs=pd.read_html(GameLogsURL)[0].query('R != "R"')\
        .drop('Unnamed: 5', axis=1)\
        .apply(partial(pd.to_numeric, errors='ignore'))\
        .reset_index(drop=True)

    PlayerGameLogs[PlayerGameLogs["Tm"].str.contains("Player went from")==False]

    return PlayerGameLogs

def GenerateGamelogRoster(MLBTeamID = None):
    RosterList = rosterPlayers(MLBTeamID)
    for player in RosterList:
        try:
            GenerateGamelogCSV(player[0])
        except OSError:
            print("Could not print " + player[0])

PrintGamelog("Javier Baez")
GenerateGamelogCSV("Javier Baez")
#GenerateGamelogRoster(121)
#Get_BBRef_ID("JD Davis")
#print(Get_BBRef_ID("J. D. Davis"))
#GenerateGamelogCSV("J. D. Davis")

#Check_batting_or_pitching(Get_BBRef_ID('Patrick Corbin'))

# for player in PlayerList:
#     GenerateGamelogCSV(player)
#     PrintGamelog(player)
#     print(GenerateGamelog(player))