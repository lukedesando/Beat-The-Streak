## imports
from BackgroundFunctions import Get_BBRef_ID, Check_batting_or_pitching
import pandas as pd
from functools import partial
from datetime import date

CurrentYear = date.today().year
PlayerName = "Carlos Correa"
#batting_or_pitching = "pitching"
year = 2021

#XXX: See other XXX note
def PrintAllSplits(PlayerID,batting_or_pitching="batting",dfList=""):
    "Defaults to batting"
    print(PlayerID,"\n")

    if batting_or_pitching == "pitching":
        dfList = Splits, SplitsPitcher,SplitsPlatoon, SplitsPlatoonPitcher,\
            SplitsGameConditions, SplitsGameConditionsPitchers, SplitsMonths
        for df in dfList:
            print (df,"\n")
    else:
        dfList = Splits,SplitsPlatoon, SplitsGameConditions, SplitsMonths,\
            SplitsPowerPitcher, SplitsGBFBPitcher, SplitsHitTrajectory
        for df in dfList:
            print (df,"\n")


#XXX Reduce testing time by a few seconds by not going through the get ID function
PlayerID = Get_BBRef_ID(PlayerName)
#PlayerID = "corbipa01"
batting_or_pitching, bat_or_pitch,b_or_p = Check_batting_or_pitching(PlayerID)

SplitsWidgetsURL ='''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3D{}&div='''.format(PlayerID,year,b_or_p)

#FIXME Cleanup needed? Any way to group these?
SplitsSeasonTotalsURL = SplitsWidgetsURL+"div_total"

SplitsSeasonTotalsPitchersURL = SplitsWidgetsURL+"div_total_extra"

SplitsPlatoonURL = SplitsWidgetsURL+"div_plato"

SplitsPlatoonPitchersURL = SplitsWidgetsURL+"div_hmvis_extra"

SplitsMonthsURL = SplitsWidgetsURL+"div_month"

SplitsPowerorFinessePitcherURL = SplitsWidgetsURL+"div_power"

SplitsHitTrajectoryURL = SplitsWidgetsURL+"div_traj"

SplitsGroundBallFlyBallURL = SplitsWidgetsURL+"div_gbfb"

SplitsGameConditionsURL = SplitsWidgetsURL+"div_stad"

SplitsGameConditionsPitchersURL = SplitsWidgetsURL+"div_stad_extra"


## removes the junk out of a given dataframe
#XXX Should this be turned into a class? Or is there a better way to do this?
#class SplitsDataframes(Self):

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

#PrintAllSplits(PlayerID,batting_or_pitching)
PrintAllSplits(Get_BBRef_ID("Vladimir Guerrero"))
