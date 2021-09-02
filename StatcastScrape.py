## imports
from BackgroundFunctions import CheckPosition, Get_BBRef_ID, Get_MLB_ID, Get_BBRefID_From_MLBID, Check_bat_or_pitch
from baseball_scraper import statcast_batter, statcast_pitcher
from datetime import date, timedelta

Today = date.today()
Tomorrow = date.today() + timedelta(days=1)
Yesterday = date.today() + timedelta(days=-1)
FiveDaysAgo = date.today() + timedelta(days=-5)
CurrentYear = date.today().year

TodayString = str(Today)
TomorrowString = str(Tomorrow)
YesterdayString = str(Yesterday)
FiveDaysAgoString = str(FiveDaysAgo)
BeginningofYearString = '2021-01-01'

def statcast_player(PlayerName=None,start_dt=FiveDaysAgoString, end_dt=TodayString, MLBID=None, position=None):
    "Works by specifying either player name or MLBID"
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
    if position == None:
        position = CheckPosition(MLBID)
    if position == 'P':
        return statcast_pitcher(start_dt,end_dt,MLBID)
    else:
        return statcast_batter(start_dt,end_dt,MLBID)

def print_statcast_player(PlayerName=None, start_dt=FiveDaysAgoString, end_dt=TodayString, MLBID=None, position=None):
    "Works by specifying either player name or MLBID"
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
    if position == None:
        position = CheckPosition(MLBID)
    print(MLBID)
    if position == 'P':
        print(statcast_pitcher(start_dt,end_dt,MLBID))
    else:
        print(statcast_batter(start_dt,end_dt,MLBID))