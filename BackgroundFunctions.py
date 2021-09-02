import csv
import json
from numpy import True_
from statsapi import player_stats,player_stat_data,lookup_player, roster,schedule
from baseball_scraper import playerid_lookup,playerid_reverse_lookup
import pandas as pd
from datetime import date, datetime,timedelta
from statsapi import get

Today = date.today()
Tomorrow = date.today() + timedelta(days=1)
CurrentYear = date.today().year


def num_names(PlayerName):
    count=PlayerName.count(" ")+1
    return count

#HACK There has to be a better way to do this
def Name_Check(PlayerName):
    namesNum = num_names(PlayerName)
    if namesNum == 2:
        if "." in PlayerName:
            PlayerFirstName,PlayerLastName = PlayerName.split(" ")
            idx = PlayerFirstName.index(".")+1
            PlayerFirstName = PlayerFirstName[:idx]+" "+PlayerFirstName[idx:]
            PlayerName = PlayerFirstName +" " + PlayerLastName
    return namesNum, PlayerName

#FIXME: calls numnames twice, once through period check and next through calling it
def Player_Dataframe_Fetch(PlayerName):
    namesNum, PlayerName = Name_Check(PlayerName)
    try:
        if namesNum == 3:
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
    
def CheckPosition(PlayerNameorMLBID):
    try:
        PlayerJson = lookup_player(PlayerNameorMLBID)
        PlayerPosition = PlayerJson[0]['primaryPosition']
        PlayerAbb = PlayerPosition['abbreviation']
        return PlayerAbb
    except IndexError as e:
        print (f'Problem searching for {PlayerNameorMLBID}\nerror: {e}')

def Get_BBRef_ID(PlayerName):
    "First Name, Last Name"
    Player_ID_Dataframe = Player_Dataframe_Fetch(PlayerName)

    SanitizedIDFrame = Player_ID_Dataframe.loc[Player_ID_Dataframe['mlb_played_last']==2021]
    BBRefKey = SanitizedIDFrame['key_bbref']

    SanitizedBBRefKey = BBRefKey.to_string(index=False)
    return SanitizedBBRefKey

def Get_BBRefID_From_MLBID(MLBID):
    "Needs to import MLBID as a list"
    if not isinstance(MLBID,list):
        MLBID = [MLBID]
    Player_ID_Dataframe = playerid_reverse_lookup(MLBID)
    SanitizedIDFrame = Player_ID_Dataframe.loc[Player_ID_Dataframe['mlb_played_last']==2021]
    BBRefKey = SanitizedIDFrame['key_bbref']
    SanitizedBBRefKey = BBRefKey.to_string(index=False)
    return SanitizedBBRefKey

#print(Get_BBRef_ID("Chi Chi Gonzalez"))

#NOTE Relies on external database; will need to be updated occasionally
#FIXME depreciated
def Find_Fangraph_ID(player_name):
    #loop through the csv list
    FanGraphsCSV = csv.reader(open('FanGraphs_Players_IDs_2021.csv', "r"), delimiter=",")
    for row in FanGraphsCSV: #Not reading in init file for some reason?
        #if current rows 2nd value is equal to input, print that row
        if player_name == row[0]:
            FGid = row[2]
            #print(FGid)
            return int(FGid)

#FIXME: Need input of MLBID to run faster
def Check_batting_or_pitching(BBRefPlayerID,year=CurrentYear):
    '''Widget exists only for pitchers. If it exists, player is pitcher. If not, player is hitter\n
    Returns 3 values'''
    try:
        SplitsSeasonTotalsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_total_extra'''.format(BBRefPlayerID,year)
        pd.read_html(SplitsSeasonTotalsPitchersURL)
        return "pitching","pitch","p"
    except ImportError:
        return "batting","bat","b"

def Check_bat_or_pitch(BBRefPlayerID,year=CurrentYear):
    "Returns 1 value"
    try:
        SplitsSeasonTotalsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_total_extra'''.format(BBRefPlayerID,year)
        pd.read_html(SplitsSeasonTotalsPitchersURL)
        return "pitch"
    except ImportError:
        return "bat"

def ConfirmList(MyString):
    if not isinstance(MyString,list):
        MyString = [MyString]
    return MyString

def rosterPlayers(teamId, rosterType=None, season=datetime.now().year, date=None):
    """Get the roster for a given team."""
    if not rosterType:
        rosterType = "active"

    params = {"rosterType": rosterType, "season": season, "teamId": teamId}
    if date:
        params.update({"date": date})

    r = get("team_roster", params)

    players = []
    for x in r["roster"]:
        players.append(
            [x["person"]["fullName"], x["person"]['id'], x["position"]["abbreviation"]]
        )

    return players