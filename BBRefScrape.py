## imports
from BackgroundFunctions import CheckPosition, Check_batting_or_pitching, Get_BBRef_and_MLB_ID, Get_MLB_ID
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

#FIXME: convert from print to dataframe; look at PlayerPrintouts for idea
def GetAllSplits(PlayerName=None,BBRefID=None,MLBID=None,batting_or_pitching=None,\
    #NOTE: These are parameters
    KeyList=["SplitsSeasonTotals","SplitsPlatoon","SplitsMonths",'SplitsGameConditions'],\
    ValueList=["div_total",'div_plato','div_month','div_stad'],\
    BatterKeyList=["SplitsPowerPitcher","SplitsHitTrajectory","SplitsGBFBPitcher"],\
    BatterValueList=['div_power','div_traj','div_gbfb'],\
    PitcherKeyList=['SplitsPitcher','SplitsPlatoonPitcher','SplitsGameConditionsPitcher'],\
    PitcherValueList=['div_total_extra','div_hmvis_extra','div_stad_extra']):
    "Specify if you will use the player's name or the BBRefID"

    if BBRefID == None:
        BBRefID, MLBID = Get_BBRef_and_MLB_ID(PlayerName)
    
    if MLBID == None:
        Get_MLB_ID(PlayerName)

    position = CheckPosition(MLBID)


    SplitsDict = {}
    if position == 'P':
        batting_or_pitching = 'pitching'
        b_or_p = 'p'
    else:
        batting_or_pitching = 'batting'
        b_or_p = 'b'
    SplitsWidgetURL ='''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3Fid%3D{}%26year%3D{}%26t%3D{}&div='''.format(BBRefID,year,b_or_p)

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
    return #"It Works"

def PrintAllSplits(PlayerName=None,BBRefID=None,batting_or_pitching=None,\
    #NOTE: These are parameters
    KeyList=["SplitsSeasonTotals","SplitsPlatoon","SplitsMonths",'SplitsGameConditions'],\
    ValueList=["div_total",'div_plato','div_month','div_stad'],\
    BatterKeyList=["SplitsPowerPitcher","SplitsHitTrajectory","SplitsGBFBPitcher"],\
    BatterValueList=['div_power','div_traj','div_gbfb'],\
    PitcherKeyList=['SplitsPitcher','SplitsPlatoonPitcher','SplitsGameConditionsPitcher'],\
    PitcherValueList=['div_total_extra','div_hmvis_extra','div_stad_extra']):
    "Specify if you will use the player's name or the BBRefID"
    if BBRefID == None:
        BBRefID, MLBID = Get_BBRef_and_MLB_ID(PlayerName)
    print(BBRefID,"\n")
    print (GetAllSplits(PlayerName,BBRefID,MLBID,batting_or_pitching,KeyList,ValueList,\
        BatterKeyList,BatterValueList,PitcherKeyList,PitcherValueList))

if __name__ == '__main__':
    PrintAllSplits("Trea Turner")
    PlayerList = ["Nick Castellanos", "Clayton Kershaw", "Max Scherzer", "Trea Turner","Alcides Escobar"]

    for player in PlayerList:
        PrintAllSplits(player)