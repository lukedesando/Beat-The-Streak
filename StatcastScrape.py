## imports
from pandas.core.frame import DataFrame
from BackgroundFunctions import CheckPosition, Get_BBRef_and_MLB_ID, Get_MLB_ID, Get_BBRefID_From_MLBID, Check_bat_or_pitch
from baseball_scraper import statcast_batter, statcast_pitcher
from datetime import date, timedelta
from BackgroundFunctions import FiveDaysAgoString,TodayString, BeginningofYearString

def statcast_player(
    PlayerName=None,start_string=BeginningofYearString, end_string=TodayString, MLBID=None, position=None,Events=False
    ):
    "Works by specifying either player name or MLBID"
    StatcastDataframe = DataFrame()
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
    if position == None:
        position = CheckPosition(MLBID)
    if position == 'P':
        StatcastDataframe = statcast_pitcher(start_string,end_string,MLBID)
    else:
        StatcastDataframe = statcast_batter(start_string,end_string,MLBID)
    if Events == True:
        StatcastDataframe = StatcastDataframe.dropna(subset=['events'])
    return StatcastDataframe

def print_statcast_player(
    PlayerName=None, start_string=FiveDaysAgoString, end_string=TodayString, MLBID=None, position=None, Events=False
    ):
    "Works by specifying either player name or MLBID"
    print(statcast_player(PlayerName,start_string, end_string, MLBID, position,Events))

def statcast_player_csv(
    PlayerName=None,start_string=FiveDaysAgoString, end_string=TodayString, MLBID=None, position=None, Events=False
    ):
    "Works by specifying either player name or MLBID, exports CSV"
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
    CSVtoPrint = statcast_player(PlayerName,start_string, end_string, MLBID, position,Events)
    CSVtoPrint.to_csv("Statcast " + str(MLBID) + " " + PlayerName +".csv")
# Testing Functions
if __name__ == '__main__':
    print(statcast_player("Buster Posey", Events=True))