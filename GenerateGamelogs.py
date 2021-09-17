## imports
import sys
from pandas.core.frame import DataFrame
from statsapi import player_stats,player_stat_data,lookup_player
import pandas as pd
from BackgroundFunctions import CheckPosition, Get_MLB_ID, rosterPlayers, playerid_lookup
from baseball_scraper import espn
from datetime import datetime, timedelta
Today = datetime.today()
Tomorrow = datetime.today() + timedelta(days=1)

from BackgroundFunctions import Get_BBRef_and_MLB_ID, Check_batting_or_pitching, rosterPlayers
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
def GenerateGamelogCSV(PlayerName = None,BBRefID=None,MLBID=None,year=CurrentYear):
    if BBRefID == None:
        BBRefID,MLBID = Get_BBRef_and_MLB_ID(PlayerName)
    PlayerGameLogs = GenerateGamelog(PlayerName,BBRefID,MLBID,year)
    if PlayerGameLogs is None:
        print("Problem finding GameLogs for {}".format(PlayerName))
        print("Double check for possible errors")
        return
    else:
        PlayerGameLogs.to_csv("GameLogs "+ MLBID + " " + PlayerName + ".csv",index=False)
        print("Returning GameLogs for {}".format(PlayerName))


def GenerateGamelog(PlayerName = None,BBRefID=None,MLBID=None,year=CurrentYear):
    errorID = 'Series([], )'
    if BBRefID == errorID:
        return
    if BBRefID == None:
        BBRefID,MLBID = Get_BBRef_and_MLB_ID(PlayerName)

    batting_or_pitching, bat_or_pitch,b_or_p = Check_batting_or_pitching(MLBID)

    GameLogsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3F\
id%3D{}%26t%3D{}%26year%3D{}&div=div_{}_gamelogs'''.format(BBRefID,b_or_p,year,batting_or_pitching)

    ## removes the junk out of the gamelogs
    PlayerGameLogs=pd.read_html(GameLogsURL)[0].query('R != "R"')\
        .drop('Unnamed: 5', axis=1)\
        .apply(partial(pd.to_numeric, errors='ignore'))\
        .reset_index(drop=True)

    PlayerGameLogs = PlayerGameLogs[PlayerGameLogs["Tm"].str.contains('|'.join("Player went from"))==False]
    #PlayerGameLogs[PlayerGameLogs["Tm"].str.contains("Player went from")==False]

    return PlayerGameLogs

def GenerateGamelogRosterCSV(MLBTeamID = None):
    RosterList = rosterPlayers(MLBTeamID)
    for player in RosterList:
        try:
            GenerateGamelogCSV(player[0])
        #FIXME not catching error of player who exists with no gamelogs, crashes instead
        except OSError:
            print("Could not print " + player[0])


#Testing Fuctions
if __name__ == '__main__':
    # #GenerateGamelogRosterCSV(121)
    PlayerList = ["Clayton Kershaw","Buster Posey","Luke DeSando"]
    
    for player in PlayerList:
        GenerateGamelogCSV(player)

    # GenerateGamelogRosterCSV(ESPNTeamIDtoMLBTeamID('WSH'))

#PrintGamelog("Javier Baez")
#GenerateGamelogCSV("Javier Baez")

#Get_BBRef_ID("JD Davis")
#print(Get_BBRef_ID("J. D. Davis"))
#GenerateGamelogCSV("J. D. Davis")

#Check_batting_or_pitching(Get_BBRef_ID('Patrick Corbin'))

# for player in PlayerList:
#     GenerateGamelogCSV(player)
#     PrintGamelog(player)
#     print(GenerateGamelog(player))