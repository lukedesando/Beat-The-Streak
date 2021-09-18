## imports
from BackgroundFunctions import CheckPosition, Get_BBRef_and_MLB_ID, Get_MLB_ID, Get_BBRefID_From_MLBID, Check_bat_or_pitch
from baseball_scraper import statcast_batter, statcast_pitcher
from datetime import date, timedelta
from BackgroundFunctions import FiveDaysAgoString,TodayString

def statcast_player(PlayerName=None,start_string=FiveDaysAgoString, end_string=TodayString, MLBID=None, position=None):
    "Works by specifying either player name or MLBID"
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
    if position == None:
        position = CheckPosition(MLBID)
    if position == 'P':
        return statcast_pitcher(start_string,end_string,MLBID)
    else:
        return statcast_batter(start_string,end_string,MLBID)

def print_statcast_player(PlayerName=None, start_string=FiveDaysAgoString, end_string=TodayString, MLBID=None, position=None):
    "Works by specifying either player name or MLBID"
    print(statcast_player(PlayerName=PlayerName,start_string=start_string, end_string=end_string, MLBID=MLBID, position=position))

def statcast_player_csv(PlayerName=None,start_string=FiveDaysAgoString, end_string=TodayString, MLBID=None, position=None):
    "Works by specifying either player name or MLBID, exports CSV"
    if MLBID == None:
        MLBID = Get_MLB_ID(PlayerName)
    CSVtoPrint = statcast_player(PlayerName=PlayerName,start_string=start_string, end_string=end_string, MLBID=MLBID, position=position)
    CSVtoPrint.to_csv("Statcast " + str(MLBID) + " " + PlayerName +".csv")
# Testing Functions
if __name__ == '__main__':
    statcast_player_csv("Buster Posey",BeginningofYearString)
    statcast_player_csv("Clayton Kershaw",BeginningofYearString)