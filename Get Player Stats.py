from logging import ERROR, error
from typing import Optional
from numpy import errstate
from statsapi import player_stats,player_stat_data,lookup_player
import pandas as pd
from BackgroundFunctions import Get_MLB_ID, Get_BBRef_ID
from baseball_scraper import espn, playerid_lookup
from datetime import datetime, timedelta

import statsapi
Today = datetime.today()
Tomorrow = datetime.today() + timedelta(days=1)

def GetPitcherPrintout(PitcherName,PitcherBasics=['current_team','pitch_hand'],
PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn']):
    '''Pitcher Basics include First Name, Last Name, Current Team, and Pitching Hand by default
    \nPitcher Stats are GS, SO, ERA, AVG, WHIP, Hits, and H/9 by default'''
    
    PitcherID = Get_MLB_ID(PitcherName)
    try:
        PitcherStatsDict = player_stat_data(PitcherID,group='pitching')
        print(PitcherName)
        
        #PitcherBasics = ['first_name','last_name','pitch_hand']
        for stat in PitcherBasics:
            print (PitcherStatsDict.get(stat))

        print(PitcherID)

        #PitcherStats = ['gamesStarted', 'strikeOuts', 'era','avg','whip','hits','hitsPer9Inn',]
        for stat in PitcherStats:
            print (f"{stat}: {PitcherStatsDict['stats'][0]['stats'][stat]}")
    except:
        print("Can't print due to error")
    #NOTE: needed to separate the pitchers
    print()

def GetBatterPrintout(BatterName,BatterBasics=['current_team','bat_side'],
BatterStats=['hits','avg','babip','strikeOuts','baseOnBalls','obp','ops']):
    '''Batter Basics include First Name, Last Name, Current Team, and Batting Side by default
    \nBatter Stats are H, AVG, BABIP, SO, BB, OBP, and OPS by default'''
    
    BatterID = Get_MLB_ID(BatterName)
    BatterStatsDict = player_stat_data(BatterID,group='batting')
    print(BatterName)
    
    for stat in BatterBasics:
        print (BatterStatsDict.get(stat))

    print(BatterID)

    for stat in BatterStats:
        print (f"{stat}: {BatterStatsDict['stats'][0]['stats'][stat]}")
    print()

def StartingPitchersPrintout(StartDate=Today,EndDate=Today):
    '''Today is selected by default as the start and end dates
    \n Encounters errors if used with past dates'''
    starters = espn.ProbableStartersScraper(StartDate, EndDate).scrape()
    StartingPitchersdf = starters['Name']
    for pitcher in StartingPitchersdf:
        GetPitcherPrintout(pitcher)

def StartingPitchersTest(StartDate=Today,EndDate=Today):
    starters = espn.ProbableStartersScraper(StartDate, EndDate).scrape()
    StartingPitchersdf = starters['Name']
    print (StartingPitchersdf)

# starters = espn.ProbableStartersScraper(Today, Today).scrape()
# StartingPitchersdf = starters['Name']
# #print(StartingPitchersdf)
# for pitcher in StartingPitchersdf:
#     GetPitcherPrintout(pitcher)
StartingPitchersTest()
StartingPitchersPrintout()
#GetBatterPrintout("Juan Soto")



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