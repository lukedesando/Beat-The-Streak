## imports
from BackgroundFunctions import CurrentYear, Get_BBRef_ID, Get_MLB_ID, Get_BBRefID_From_MLBID, Check_bat_or_pitch
from baseball_scraper import statcast_batter, statcast_pitcher
from datetime import date, timedelta

Today = date.today()
Tomorrow = date.today() + timedelta(days=1)
Yesterday = date.today() + timedelta(days=-1)
CurrentYear = date.today().year

TodayString = str(Today)
TomorrowString = str(Tomorrow)
YesterdayString = str(Yesterday)
BeginningofYearString = '2021-01-01'

def statcast_player_MLBID(start_dt=None, end_dt=TodayString, MLBID=None):
    BBRefID=Get_BBRefID_From_MLBID(MLBID)
    bat_or_pitch = Check_bat_or_pitch(BBRefID)
    if bat_or_pitch == 'bat':
        return statcast_batter(start_dt,end_dt,MLBID)
    else:
        return statcast_pitcher(start_dt,end_dt,MLBID)

def statcast_player(start_dt=None, end_dt=TodayString, PlayerName=None):
    MLBID = Get_MLB_ID(PlayerName)
    BBRefID=Get_BBRefID_From_MLBID(MLBID)
    bat_or_pitch = Check_bat_or_pitch(BBRefID)
    if bat_or_pitch == 'bat':
        return statcast_batter(start_dt,end_dt,MLBID)
    else:
        return statcast_pitcher(start_dt,end_dt,MLBID)

def print_statcast_player_MLBID(start_dt=None, end_dt=TodayString, MLBID=None):
    'Needs MLBID'
    BBRefID=Get_BBRefID_From_MLBID(MLBID)
    bat_or_pitch = Check_bat_or_pitch(BBRefID)
    if bat_or_pitch == 'bat':
        print(statcast_batter(start_dt,end_dt,MLBID))
    else:
        print(statcast_pitcher(start_dt,end_dt,MLBID))

def print_statcast_player(start_dt=None, end_dt=TodayString, PlayerName=None):
    'Needs MLBID'
    MLBID = Get_MLB_ID(PlayerName)
    BBRefID=Get_BBRefID_From_MLBID(MLBID)
    bat_or_pitch = Check_bat_or_pitch(BBRefID)
    if bat_or_pitch == 'bat':
        print(statcast_batter(start_dt,end_dt,MLBID))
    else:
        print(statcast_pitcher(start_dt,end_dt,MLBID))

#print(statcast_player(start_dt = BeginningofYearString,end_dt=TodayString,PlayerName='Juan Soto'))