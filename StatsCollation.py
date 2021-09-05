# if night
# if gb pitcher
# if power pitcher
# totals, last 7 and 14 days

## imports
from BackgroundFunctions import rosterPlayers
from BBRefScrape import GetAllSplits, PrintAllSplits
from PlayerPrintouts import CSV_RosterStats, PrintPlayerStats, StartingPitchersPrintoutwRoster, CSV_PlayerStats
from StatcastScrape import statcast_player, print_statcast_player
from datetime import date, timedelta
from statsapi import roster
from baseball_scraper import espn
import pandas as pd
from GenerateGamelogs import GenerateGamelogCSV

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

def PrintAllInfo(PlayerName):
    PrintPlayerStats(PlayerName)
    PrintAllSplits(PlayerName)
    #print_statcast_player(PlayerName)

def GenerateAllCSVs(PlayerName):
    CSV_PlayerStats(PlayerName)
    GenerateGamelogCSV(PlayerName)

#StartingPitchersPrintoutwRoster()
PlayerList = ["Nick Castellanos", "Clayton Kershaw", "Max Scherzer", "Trea Turner","Alcides Escobar"]

for player in PlayerList:
    GenerateAllCSVs(player)
    # PrintAllInfo(player)

# CSV_RosterStats(121)

writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')
df_from_each_file = (pd.read_csv(f) fo)

for idx, df in enumerate(df_from_each_file):
    df.to_excel(writer, sheet_name='data{0}.csv'.format(idx))

writer.save()

#PrintAllSplits(BBRefID="smithwi05")
#StartingPitchersPrintout()


#print(Check_bat_or_pitch('scherma01'))

#PrintAllSplitsBBRefID(543037)
#PrintAllSplits('Max Scherzer')

#GetBatterPrintoutMLBID()

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