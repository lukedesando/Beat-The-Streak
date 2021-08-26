## imports
from BackgroundFunctions import Get_BBRef_ID
import pandas as pd
from functools import partial

#hyperlink = "https://www.baseball-reference.com/players/gl.fcgi?id=turnetr01&t=b&year=2021"
PlayerName = "Fernando Tatis"
batting_or_pitching = "batting"
year = 2021

PlayerID = Get_BBRef_ID(PlayerName)
#PlayerID = 'tatisfe02'
if batting_or_pitching == "pitching":
    b_or_p = "p"
    bat_or_pitch = "pitch"
else:
    b_or_p = "b"
    bat_or_pitch = "bat"

## set our url, notice the differences
#url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3Dturnetr01%26t%3Db%26year%3D2021&div=div_batting_gamelogs"
#url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3Dscherma01%26t%3Dp%26year%3D2021&div=div_pitching_gamelogs"
#url = "https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3Dscherma01%26t%3Dp%26year%3D2020&div=div_pitching_gamelogs"

#NOTE This will give the table for gamelogs of a specified year off BBRef

#url = '''\fhttps://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3Fid%3D{PlayerID}%26t%3Dp%26year%3D{year}&div=div_{batting_or_pitching}_gamelogs'''
url = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3F\
id%3D{}%26t%3D{}%26year%3D{}&div=div_{}_gamelogs'''.format(PlayerID,b_or_p,year,batting_or_pitching)
#four different fields to change

## remove the junk out of the dataframe
GameLogs=pd.read_html(url)[0].query('aLI != "aLI"')\
    .drop('Unnamed: 5', axis=1)\
    .apply(partial(pd.to_numeric, errors='ignore'))\
    .reset_index(drop=True)

GameLogs.to_csv(PlayerName + " Game Logs.csv",index=False)