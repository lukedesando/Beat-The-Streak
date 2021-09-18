from GenerateGamelogs import GenerateGamelog
from BackgroundFunctions import Get_MLB_ID, GetBBRefTeamID, GetMLBTeamID, rosterPlayers
from BackgroundFunctions import Today, BeginningofYearString, CurrentYear, Since2017String
from StatcastScrape import statcast_player
from PlayerPrintouts import GetStartingPitchers, RosterBatterStatsPrintout,PrintPlayerStats
from baseball_scraper import espn

#TODO: Get Buster Posey's numbers off Giants in 2021

def GetMatchup(BatterName, PitcherName, BatterID = None, PitcherID = None, Events = False, StartDateString=BeginningofYearString):
    '''Returns a dataframe with all pitches thrown between two players in the current year
    \n Batter first. If you want to only see the events, set Events = True'''
    if BatterID == None:
        BatterID = Get_MLB_ID(BatterName)
    if PitcherID == None:
        PitcherID = Get_MLB_ID(PitcherName)
    PlayerDataFrame = statcast_player(BatterID,StartDateString)
    MatchupFrame = PlayerDataFrame.loc[PlayerDataFrame['pitcher']==PitcherID]
    if Events == True:
        MatchupFrame = MatchupFrame.dropna(subset=['events'])
    return MatchupFrame

def GetMatchupCSV(BatterName = None,PitcherName = None,BatterID = None,PitcherID = None,Events=False,StartDateString=BeginningofYearString):
    "Batter first"
    StartDateString : str
    if BatterID == None:
        BatterID = Get_MLB_ID(BatterName)
    if PitcherID == None:
        PitcherID = Get_MLB_ID(PitcherName)
    PlayerDataFrame = GetMatchup(BatterName=BatterName,PitcherName=PitcherName,BatterID=BatterID,PitcherID=PitcherID,Events=Events,StartDateString=StartDateString)
    if PlayerDataFrame.empty:
        print("No Matchup Data for {} versus {}".format(BatterName,PitcherName))
        return
    if Events == False:
        CSVFileName = "Matchup B{} P{} {} vs. {}.csv".format(BatterID,PitcherID,BatterName,PitcherName)
    else:
        CSVFileName = "Matchup B{} P{} Events {} vs. {}.csv".format(BatterID,PitcherID,BatterName,PitcherName)
    PlayerDataFrame.to_csv(CSVFileName,index=False)

def GetBatterTeamGamelogs(BatterName,OpponentTeamID,BatterID=None,year=CurrentYear):
    if OpponentTeamID == None:
        print("Needs Team ID to function")
        return
    BBRefTeamID = GetBBRefTeamID(OpponentTeamID)
    Gamelogs = GenerateGamelog(BatterName,MLBID=BatterID)
    RelevantGamelogs = Gamelogs.loc[Gamelogs['Opp']==BBRefTeamID]
    return RelevantGamelogs

def GetBatterTeamGamelogsCSV(BatterName,OpponentTeamID,BatterID=None,year=CurrentYear):
    Gamelogs = GetBatterTeamGamelogs(BatterName=BatterName,OpponentTeamID=OpponentTeamID,BatterID=BatterID)
    if BatterID == None:
        BatterMLBID = Get_MLB_ID(BatterName)
    MLBTeamID = GetMLBTeamID(OpponentTeamID)
    CSVFileName = "Matchup B{} T{} {} {} vs. {}.csv".format(BatterMLBID,MLBTeamID,year,BatterName,OpponentTeamID)
    Gamelogs.to_csv(CSVFileName,index=False)


if __name__ == '__main__':
    # # print(GetMatchup("Buster Posey","Blake Snell"))
    # # GetMatchupCSV("Buster Posey","Blake Snell")
    # SanitizedMatchup = GetMatchup("Buster Posey","Blake Snell",Events=True)
    # # FinalBoss = SanitizedMatchup.loc[SanitizedMatchup['events']=='walk']
    # print (SanitizedMatchup)
    # GetMatchupCSV("Buster Posey","Blake Snell",Events=True)
    StartDate = Today
    EndDate = Today
    # StartingPitchers = GetStartingPitchers()
    starters = espn.ProbableStartersScraper(StartDate, EndDate).scrape()
    for i, row in starters.iterrows():
        pitcher = row['Name']
        opponent = row['opponent']
        Roster = rosterPlayers(GetMLBTeamID(opponent))
        for player in Roster:
            PlayerName = player[0]
            PlayerID = player[1]
            PlayerPosition = player[2]
            if PlayerPosition != 'P':
                batter = PlayerName
                GetMatchupCSV(batter,pitcher,BatterID = PlayerID,Events=True,StartDateString=Since2017String)
    # BatterList = ["Kris Bryant", "Juan Soto", "Bryce Harper"]
    # Opponent = 'Clayton Kershaw'
    # for BatterName in BatterList:
    #     GetMatchupCSV(BatterName,Opponent,StartDateString='2016-01-01')
    #     #GetMatchupCSV(BatterName,Opponent,Events=True)
