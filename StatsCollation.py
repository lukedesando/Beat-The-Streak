# if night
# if gb pitcher
# if power pitcher
# totals, last 7 and 14 days

## imports
from BackgroundFunctions import CheckPosition, Get_BBRef_ID, Get_MLB_ID, Get_BBRefID_From_MLBID
from BBRefScrape import PrintAllSplits
from PlayerPrintouts import PrintPlayerStats
from StatcastScrape import statcast_player, print_statcast_player
from datetime import date, timedelta

Today = date.today()
Tomorrow = date.today() + timedelta(days=1)
Yesterday = date.today() + timedelta(days=-1)
CurrentYear = date.today().year
ThirtyDaysAgo = date.today() + timedelta(days=-30)

TodayString = str(Today)
TomorrowString = str(Tomorrow)
YesterdayString = str(Yesterday)
BeginningofYearString = '2021-01-01'
ThirtyDaysAgoString = str(ThirtyDaysAgo)


PlayerList = ['Casey Mize', "Juan Soto",'Robbie Ray']

#print(Check_bat_or_pitch('scherma01'))

#PrintAllSplitsBBRefID(543037)
#PrintAllSplits('Max Scherzer')

#GetBatterPrintoutMLBID()

#print(Get_BBRefID_From_MLBID([543037]))
#FIXME: Touches database twice; should probably combine into one touch
# for player in PlayerList:
#     MLBID = Get_MLB_ID(player)
#     BBRefID = Get_BBRef_ID(player)
#     PrintPlayerStatsMLBID(MLBID)
#     PrintAllSplitsBBRefID(BBRefID)
for players in PlayerList:
    PrintPlayerStats(players)
    print_statcast_player(players)
    PrintAllSplits(players)
# #NOTE: Just for printing!
# for player in PlayerList:
#     #PrintPlayerStats(player)
#     PrintAllSplits(player)
#     #print_statcast_player(start_dt= ThirtyDaysAgoString,PlayerName=player)


# for player in PlayerList:
#     StatcastDF = statcast_player(start_dt=ThirtyDaysAgoString,PlayerName = player)
#     StatcastDF.to_csv('Statcast Data '+player+'.csv',index=False)

#PrintAllSplits(BBRefID='sotoju01')
#MyStatsdf = MyPitcherStats('Gerrit Cole')