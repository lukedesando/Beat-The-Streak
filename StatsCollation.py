# if night
# if gb pitcher
# if power pitcher
# totals, last 7 and 14 days

## imports
from BackgroundFunctions import rosterPlayers
from BBRefScrape import PrintAllSplits
from PlayerPrintouts import PrintPlayerStats, StartingPitchersPrintout,PrintPitcherStats, StartingPitchersPrintoutwRoster
from StatcastScrape import statcast_player, print_statcast_player
from datetime import date, timedelta
from statsapi import roster
from baseball_scraper import espn

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

#StartingPitchersPrintout()

StartingPitchersPrintoutwRoster()
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
# for players in PlayerList:
#     PrintPlayerStats(players)
#     print_statcast_player(players)
#     PrintAllSplits(players)

#print(roster(136))
#print(rosterPlayers(136))
#roster(136)

# # RosterList = rosterPlayers(120)+rosterPlayers(121)
# # XXX: Right here!!!
# # for Player in RosterList:
# #     PrintInfo = Player[1]
# #     PrintPlayerStats(PrintInfo)
# #     #print_statcast_player(PrintInfo)

#i=0
# for Person in RosterList:
#     print(str(Person[0])+" is "+str(Person[1]))


    
#['roster'][1])
#PlayerList = rosterPlayers(136)

#for players in PlayerList:
#    PrintPlayerStats(players)

#PrintPlayerStats("Shohei Ohtani")
#PrintAllSplits("Shohei Ohtani",batting_or_pitching='batting')
#print_statcast_player("Shohei Ohtani",position='DH')

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