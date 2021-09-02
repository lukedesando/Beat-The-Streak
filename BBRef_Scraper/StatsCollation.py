# if night
# if gb pitcher
# if power pitcher
# totals, last 7 and 14 days

## imports
from BackgroundFunctions import Get_BBRef_ID, Get_MLB_ID, Get_BBRefID_From_MLBID
from BBRefScrape import PrintAllSplits, PrintAllSplitsBBRefID
from PlayerPrintouts import PrintPlayerStats, PrintPlayerStatsMLBID

PlayerList = ['Gerrit Cole', "Juan Soto"]

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

for player in PlayerList:
    PrintPlayerStats(player)
    PrintAllSplits(player)
