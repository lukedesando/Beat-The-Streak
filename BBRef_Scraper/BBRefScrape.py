## imports
from BackgroundFunctions import Get_BBRef_ID, Check_batting_or_pitching
import pandas as pd
from functools import partial
from datetime import date

CurrentYear = date.today().year
#PlayerName = "Carlos Correa"
#batting_or_pitching = "pitching"
year = 2021

#XXX Reduce testing time by a few seconds by not going through the get ID function
#PlayerID = Get_BBRef_ID(PlayerName)
#PlayerID = "corbipa01"
#SplitsURLList = [SplitsSeasonTotalsURL,SplitsSeasonTotalsPitchersURL,SplitsPlatoonURL]

def AddToSplitsDict(KeyList: list,ValueList: list,SplitsWidgetURL,SplitsDict={}):
    n=0
    # for Key in KeyList:
    #     for Value in ValueList:
    #         SplitsDict[Key] =SplitsWidgetURL+Value
    #         #ValueList.remove(Value)
    #         break
    for Key in KeyList:
        
        SplitsDict[Key] =SplitsWidgetURL+ValueList[n]
        #ValueList.remove(Value)
        n = n+1



#XXX: See other XXX note
def PrintAllSplits(PlayerName,\
    #NOTE: These are parameters
    KeyList=["SplitsSeasonTotals","SplitsPlatoon","SplitsMonths",'SplitsGameConditions'],\
    ValueList=["div_total",'div_plato','div_month','div_stad'],\
    BatterKeyList=["SplitsPowerPitcher","SplitsHitTrajectory","SplitsGBFBPitcher"],\
    BatterValueList=['div_power','div_traj','div_gbfb'],\
    PitcherKeyList=['SplitsPitcher','SplitsPlatoonPitcher','SplitsGameConditionsPitcher'],\
    PitcherValueList=['div_total_extra','div_hmvis_extra','div_stad_extra']):
    
    PlayerID = Get_BBRef_ID(PlayerName)
    print(PlayerID,"\n")

    SplitsDict = {}

    batting_or_pitching, bat_or_pitch,b_or_p = Check_batting_or_pitching(PlayerID)
    SplitsWidgetURL ='''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3Fid%3D{}%26year%3D{}%26t%3D{}&div='''.format(PlayerID,year,b_or_p)

    AddToSplitsDict(KeyList, ValueList,SplitsWidgetURL,SplitsDict)
    if batting_or_pitching  == "batting":
        AddToSplitsDict(BatterKeyList,BatterValueList,SplitsWidgetURL,SplitsDict)
    else:
        AddToSplitsDict(PitcherKeyList,PitcherValueList,SplitsWidgetURL,SplitsDict)

   
    
    for key in SplitsDict:
        #print(key)
        #print (SplitsDict[key])
        print(pd.read_html(SplitsDict[key])[0].query('G != "G"')\
        .apply(partial(pd.to_numeric, errors='ignore'))\
        .reset_index(drop=True))
        print()

    #NOTE: Keeping all keys and values here so we don't lose them
    # KeyList = ["SplitsSeasonTotals","SplitsSeasonTotalsPitchers","SplitsPlatoon","SplitsPlatoonPitchers",\
    # "SplitsMonths",'SplitsPowerorFinessePitcher','SplitsHitTrajectory',\
    # 'SplitsGroundBallFlyBall','SplitsGameConditions','SplitsGameConditionsPitchers']
    # ValueList = ["div_total","div_total_extra","div_plato","div_hmvis_extra","div_month",'div_power','div_traj',\
    # 'div_gbfb','div_stad','div_stad_extra']

def PrintAllSplitsBBRefID(PlayerID,\
    #NOTE: These are parameters
    KeyList=["SplitsSeasonTotals","SplitsPlatoon","SplitsMonths",'SplitsGameConditions'],\
    ValueList=["div_total",'div_plato','div_month','div_stad'],\
    BatterKeyList=["SplitsPowerPitcher","SplitsHitTrajectory","SplitsGBFBPitcher"],\
    BatterValueList=['div_power','div_traj','div_gbfb'],\
    PitcherKeyList=['SplitsPitcher','SplitsPlatoonPitcher','SplitsGameConditionsPitcher'],\
    PitcherValueList=['div_total_extra','div_hmvis_extra','div_stad_extra']):
    
    print(PlayerID,"\n")

    SplitsDict = {}

    batting_or_pitching, bat_or_pitch,b_or_p = Check_batting_or_pitching(PlayerID)
    SplitsWidgetURL ='''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3Fid%3D{}%26year%3D{}%26t%3D{}&div='''.format(PlayerID,year,b_or_p)

    AddToSplitsDict(KeyList, ValueList,SplitsWidgetURL,SplitsDict)
    if batting_or_pitching  == "batting":
        AddToSplitsDict(BatterKeyList,BatterValueList,SplitsWidgetURL,SplitsDict)
    else:
        AddToSplitsDict(PitcherKeyList,PitcherValueList,SplitsWidgetURL,SplitsDict)

   
    
    for key in SplitsDict:
        #print(key)
        #print (SplitsDict[key])
        print(pd.read_html(SplitsDict[key])[0].query('G != "G"')\
        .apply(partial(pd.to_numeric, errors='ignore'))\
        .reset_index(drop=True))
        print()

#SplitsURLDict["SplitsSeasonTotalsURL"]=SplitsWidgetsURL+"div_total"
#PlayerList = ['Fernando Tatis','Patrick Corbin','Vladimir Guerrero']

#PrintAllSplits(Get_BBRef_ID('Fernando Tatis'))

#for player in PlayerList:
    #PrintAllSplits(Get_BBRef_ID(player))
#PrintAllSplits(Get_BBRef_ID("Vladimir Guerrero"))
