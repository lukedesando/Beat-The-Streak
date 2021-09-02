from statsapi import player_stats,player_stat_data,lookup_player
import pandas as pd
from BackgroundFunctions import CheckPosition, Get_MLB_ID
from baseball_scraper import espn, playerid_lookup
from datetime import datetime, time, timedelta

import statsapi
Today = datetime.today()
Tomorrow = datetime.today() + timedelta(days=1)

def PrintPitcherStats(PlayerName=None,MLBID=None,PitcherBasics=['current_team','pitch_hand'],
PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn']):
    '''Pitcher Basics include First Name, Last Name, Current Team, and Pitching Hand by default
    \nPitcher Stats are GS, SO, ERA, AVG, WHIP, Hits, and H/9 by default'''
    
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
        
    try:
        PitcherStatsDict = player_stat_data(MLBID,group='pitching')
        if PlayerName!=None:
            print(PlayerName)
        
        #PitcherBasics = ['first_name','last_name','pitch_hand']
        for stat in PitcherBasics:
            print (PitcherStatsDict.get(stat))

        print(MLBID)

        #PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn',]
        for stat in PitcherStats:
            print (f"{stat}: {PitcherStatsDict['stats'][0]['stats'][stat]}")
    except:
        print("Can't print due to error")
    #NOTE: needed to separate the pitchers
    print()

def PrintBatterStats(PlayerName=None,MLBID=None,BatterBasics=['current_team','bat_side'],
BatterStats=['hits','avg','babip','strikeOuts','baseOnBalls','obp','ops']):
    '''Batter Basics include First Name, Last Name, Current Team, and Batting Side by default
    \nBatter Stats are H, AVG, BABIP, SO, BB, OBP, and OPS by default'''
    
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)

    BatterStatsDict = player_stat_data(MLBID,group='batting')
    if PlayerName!=None:
        print(PlayerName)
    
    for stat in BatterBasics:
        print (BatterStatsDict.get(stat))

    print(MLBID)

    for stat in BatterStats:
        print (f"{stat}: {BatterStatsDict['stats'][0]['stats'][stat]}")
    print()

def PrintPitcherStatsMLBID(MLBPitcherID,PitcherBasics=['first_name','last_name','current_team','pitch_hand'],
PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn']):
    '''Pitcher Basics include First Name, Last Name, Current Team, and Pitching Hand by default
    \nPitcher Stats are GS, SO, ERA, AVG, WHIP, Hits, and H/9 by default'''
    
    try:
        PitcherStatsDict = player_stat_data(MLBPitcherID,group='pitching')
        
        #PitcherBasics = ['first_name','last_name','pitch_hand']
        for stat in PitcherBasics:
            print (PitcherStatsDict.get(stat))

        print(MLBPitcherID)

        #PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn',]
        for stat in PitcherStats:
            print (f"{stat}: {PitcherStatsDict['stats'][0]['stats'][stat]}")
    except:
        print("Can't print due to error")
    #NOTE: needed to separate the pitchers
    print()

def PrintBatterStatsMLBID(MLBBatterID,BatterBasics=['first_name','last_name','current_team','bat_side'],
BatterStats=['hits','avg','babip','strikeOuts','baseOnBalls','obp','ops']):
    '''Batter Basics include First Name, Last Name, Current Team, and Batting Side by default
    \nBatter Stats are H, AVG, BABIP, SO, BB, OBP, and OPS by default'''
    
    #BatterID = Get_MLB_ID(BatterName)
    BatterStatsDict = player_stat_data(MLBBatterID,group='batting')
    #print(BatterName)
    
    for stat in BatterBasics:
        print (BatterStatsDict.get(stat))

    print(MLBBatterID)

    for stat in BatterStats:
        print (f"{stat}: {BatterStatsDict['stats'][0]['stats'][stat]}")
    print()

def StartingPitchersPrintout(StartDate=Today,EndDate=Today):
    '''Today is selected by default as the start and end dates
    \n Encounters errors if used with past dates'''
    starters = espn.ProbableStartersScraper(StartDate, EndDate).scrape()
    StartingPitchersdf = starters['Name']
    for pitcher in StartingPitchersdf:
        PrintPitcherStats(pitcher)

#NOTE: Only needed to test if Starting pitchrs
def StartingPitchersTest(StartDate=Today,EndDate=Today):
    starters = espn.ProbableStartersScraper(StartDate, EndDate).scrape()
    StartingPitchersdf = starters['Name']
    print (StartingPitchersdf)
    print ()

def PrintPlayerStats(PlayerName=None,MLBID=None):
    if MLBID == None:
        if PlayerName != None:
            MLBID = Get_MLB_ID(PlayerName)

    position = CheckPosition(MLBID)
    if position == 'P':
        PrintPitcherStatsMLBID(MLBID)
    else:
        PrintBatterStatsMLBID(MLBID)

#StartingPitchersPrintout()

# starters = espn.ProbableStartersScraper(Today, Today).scrape()
# StartingPitchersdf = starters['Name']
# #print(StartingPitchersdf)
# for pitcher in StartingPitchersdf:
#     PrintPitcherStats(pitcher)
#starters = espn.ProbableStartersScraper(Today, Tomorrow +timedelta(5)).scrape()
#starters.to_csv("StartersTest.csv")
#StartingPitchersPrintout(Tomorrow, Tomorrow)
#PrintBatterStats("Vladimir Guerrero")
#tartingPitchersPrintout(Tomorrow,Tomorrow)
#PrintBatterStats("Juan Soto")



#print(playerid_lookup("Soto","Juan"))
    #NOTE This will be how we get the BBref keys
    # just cross reference them with MLB_played_last (or MLB key)



# pitcherID = Get_Player_ID("Patrick Corbin")
# PitcherStatsDict = player_stat_data(pitcherID,group='pitching')
# #print(player_stat_data(pitcherID,group='pitching'))
# #print(player_stats(pitcherID,group='pitching'))

# batterID = Get_Player_ID("Juan Soto")
# BatterStatsDict = player_stat_data(batterID,group='batting')
# print(player_stat_data(batterID,group='batting'))

# PitcherBasics = ['first_name','last_name','pitch_hand']
# for stat in PitcherBasics:
#     print (PitcherStatsDict.get(stat))

# #Necessary structure for nested dict
# #print(PitcherStatsDict['stats'][0]['stats']['avg'])

# PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn',]
# for stat in PitcherStats:
#     print (f"{stat}: {PitcherStatsDict['stats'][0]['stats'][stat]}")