from StatcastScrape import print_statcast_player, statcast_player
from BackgroundFunctions import GetMLBTeamID, Tomorrow,Today,Since2017String, rosterPlayers
from BBRefScrape import GetAllSplits
from PlayerPrintouts import GetStartingPitchers, PrintPlayerStats, StartingPitchersPrintout
from Matchups import GetBatterTeamGamelogsCSV, GetMatchupCSV
import myespn


#FIXME: Pitcher with same name as hitter is mistaken for hitter
#StartingPitchersPrintout(Tomorrow,Tomorrow)

#TODO Update Chadwick Now and again
#TODO: Batter vs. Team stats

if __name__ == '__main__':
    StartDate = Today
    EndDate = Today
    # StartingPitchers = GetStartingPitchers()
    starters = myespn.ProbableStartersScraper(StartDate, EndDate).scrape()
    print (starters)
    for i, row in starters.iterrows():
        pitcher = row['Name']
        opponent = row['opponent']
        pitcherteam = row['team']
        Roster = rosterPlayers(GetMLBTeamID(opponent))
        for player in Roster:
            PlayerName = player[0]
            PlayerID = player[1]
            PlayerPosition = player[2]
            if PlayerPosition != 'P':
                batter = PlayerName
                GetMatchupCSV(batter,pitcher,BatterID = PlayerID,Events=True,StartDateString=Since2017String)
                #TODO Get Team of pitcher
                GetBatterTeamGamelogsCSV(batter,pitcherteam,BatterID=PlayerID)