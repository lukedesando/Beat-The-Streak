from StatcastScrape import BeginningofYearString, print_statcast_player, statcast_player
from BackgroundFunctions import Tomorrow
from BBRefScrape import GetAllSplits
from PlayerPrintouts import GetStartingPitchers, PrintPlayerStats, StartingPitchersPrintout
from Matchups import GetMatchupCSV


#FIXME: Pitcher with same name as hitter is mistaken for hitter
#StartingPitchersPrintout(Tomorrow,Tomorrow)

#TODO Update Chadwick Now and again

PlayerList = ["Miguel Cabrera"]#, "Jeimer Candelario","Harold Castro","Jonathan Schoop"]
# StartingPitchersPrintout()
# print(GetStartingPitchers())
StartingPitchersdf = GetStartingPitchers()
# for Player in PlayerList:
#     print(Player)
#     GetAllSplits(Player)
#     statcast_player(Player,BeginningofYearString).to_csv("Statcast " + Player + ".csv")
#     print_statcast_player(Player,BeginningofYearString)
#     #TODO: Batter vs. Pitcher stats
#     #TODO: Batter vs. Team stats