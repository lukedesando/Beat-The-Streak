## imports
from BackgroundFunctions import Get_BBRef_ID
import pandas as pd
from functools import partial
from datetime import date

CurrentYear = date.today().year
PlayerName = "Fernando Tatis"
#batting_or_pitching = "pitching"
year = 2021

# def Check_Batting_or_Pitching(batting_or_pitching):
#     if batting_or_pitching == "pitching":
#         return "p","pitch"
#     else:
#         return "b", "bat"

#NOTE: Shohei Ohtani won't work; need an exception for him
def Check_batting_or_pitching(PlayerID):
    try:
        SplitsSeasonTotalsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_total_extra'''.format(PlayerID,year)
        pd.read_html(SplitsSeasonTotalsPitchersURL)
        return "pitching","pitch","p"
    except ImportError:
        return "batting","bat","b"

#XXX: I want a way to add more urls to both sides more easily. They will be out of order. Is there a way?
def PrintAllSplits(PlayerID,batting_or_pitching="batting"):
    print(PlayerID,"\n")
    if batting_or_pitching == "pitching":
        dfList = Splits,SplitsPitcher,SplitsPlatoon, SplitsPlatoonPitcher, SplitsGameConditions, SplitsGameConditionsPitchers, SplitsMonths
        for df in dfList:
            print (df,"\n")
    else:
        dfList = Splits,SplitsPlatoon, SplitsGameConditions, SplitsMonths, SplitsPowerPitcher, SplitsGBFBPitcher, SplitsHitTrajectory
        for df in dfList:
            print (df,"\n")


PlayerID = Get_BBRef_ID(PlayerName)
batting_or_pitching, bat_or_pitch,b_or_p = Check_batting_or_pitching(PlayerID)
#Reduces testing time by a few seconds to not go through the get ID function
#PlayerID = "corbipa01"

#b_or_p, bat_or_pitch = Check_Batting_or_Pitching(batting_or_pitching)
#PlayerID = 'tatisfe02'
# if batting_or_pitching == "pitching":
#     b_or_p = "p"
#     bat_or_pitch = "pitch"
# else:
#     b_or_p = "b"
#     bat_or_pitch = "bat"

GameLogsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3F\
id%3D{}%26t%3D{}%26year%3D{}&div=div_{}_gamelogs'''.format(PlayerID,b_or_p,year,batting_or_pitching)

SplitsSeasonTotalsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3D{}&div=div_total'''.format(PlayerID,year,b_or_p)

SplitsSeasonTotalsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_total_extra'''.format(PlayerID,year)
#NOTE: widget is designed for pitchers; does not exist for hitters

SplitsPlatoonURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3D{}&div=div_plato'''.format(PlayerID,year,b_or_p)

SplitsPlatoonPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_hmvis_extra'''.format(PlayerID,year)
#NOTE: widget is designed for pitchers; does not exist for hitters

SplitsMonthsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3D{}&div=div_month'''.format(PlayerID,year,b_or_p)

SplitsPowerorFinessePitcherURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Db&div=div_power'''.format(PlayerID,year)
#NOTE: widget is designed for hitters; does not exist for pitchers

SplitsHitTrajectoryURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Db&div=div_traj'''.format(PlayerID,year)
#NOTE: widget is designed for hitters; does not exist for pitchers

SplitsGroundBallFlyBallURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Db&div=div_gbfb'''.format(PlayerID,year)
#NOTE: widget is designed for hitters; does not exist for pitchers

SplitsGameConditionsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3D{}&div=div_stad'''.format(PlayerID,year,b_or_p)

SplitsGameConditionsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_stad_extra'''.format(PlayerID,year)
#NOTE: widget is designed for pitchers; does not exist for hitters


## set our url, notice the differences
#url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3Dturnetr01%26t%3Db%26year%3D2021&div=div_batting_gamelogs"
#url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3Dscherma01%26t%3Dp%26year%3D2021&div=div_pitching_gamelogs"
#url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3Dscherma01%26t%3Dp%26year%3D2020&div=div_pitching_gamelogs"


## remove the junk out of a given dataframe
#XXX Should this be turned into a class? Or is there a better way to do this?
PlayerGameLogs=pd.read_html(GameLogsURL)[0].query('R != "R"')\
    .drop('Unnamed: 5', axis=1)\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

Splits = pd.read_html(SplitsSeasonTotalsURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

SplitsPlatoon = pd.read_html(SplitsPlatoonURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

SplitsMonths = pd.read_html(SplitsMonthsURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

SplitsGameConditions = pd.read_html(SplitsGameConditionsURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

if batting_or_pitching == "pitching":
    SplitsPitcher = pd.read_html(SplitsSeasonTotalsPitchersURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

    SplitsPlatoonPitcher = pd.read_html(SplitsPlatoonPitchersURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

    SplitsGameConditionsPitchers = pd.read_html(SplitsGameConditionsPitchersURL)[0].query('G != "G"')\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

if batting_or_pitching == 'batting':
    SplitsPowerPitcher = pd.read_html(SplitsPowerorFinessePitcherURL)[0].query('G != "G"')\
    .dropna(axis=1)\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)
    # NOTE: Power pitchers are in the top third of the league in strikeouts plus walks.
    # Finesse are in the bottom third of the league in strikeouts plus walks.
    # Stats are based on the three years before and after (when available), and the season for when the split is computed.
    # A split in 1994 would consider years 1991-1997 when classifying a pitcher.

    SplitsHitTrajectory= pd.read_html(SplitsHitTrajectoryURL)[0].query('G != "G"')\
    .dropna(axis=1)\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

    SplitsGBFBPitcher = pd.read_html(SplitsGroundBallFlyBallURL)[0].query('G != "G"')\
    .dropna(axis=1)\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)
    # NOTE: Fly Ball pitchers are in the top third of the league in ratio of fly ball outs to ground ball outs.
    # Ground Ball are in the bottom third of the league in the ratio of fly ball outs to ground ball outs.
    # Stats are based on the three years before and after (when available), and the season for when the split is computed.
    # A split in 1994 would consider years 1991-1997 when classifying a pitcher.


# GameLogs.to_csv(PlayerName + " Game Logs.csv",index=False)
PrintAllSplits(PlayerID,batting_or_pitching)
