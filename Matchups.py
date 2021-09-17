from GenerateGamelogs import GenerateGamelog
from BackgroundFunctions import Get_BBRef_and_MLB_ID, Get_MLB_ID, GetBBRefTeamID, GetMLBTeamID, rosterPlayers
from StatsCollation import BeginningofYearString
from StatcastScrape import statcast_player


from pandas.core.frame import DataFrame

#TODO: Get Buster Posey's numbers off Giants in 2021

def GetMatchup(BatterName = None,PitcherName = None,BatterID = None,PitcherID = None):
    '''Returns a dataframe with all pitches thrown between two players in 2021
    \n Batter first'''
    if BatterID == None:
        BatterID = Get_MLB_ID(BatterName)
    if PitcherID == None:
        PitcherID = Get_MLB_ID(PitcherName)
    PlayerDataFrame = statcast_player(BatterID,BeginningofYearString)
    MatchupFrame = PlayerDataFrame.loc[PlayerDataFrame['pitcher']==PitcherID]
    return MatchupFrame

def GetMatchupCSV(BatterName = None,PitcherName = None,BatterID = None,PitcherID = None):
    "Batter first"
    if BatterID == None:
        BatterID = Get_MLB_ID(BatterName)
    if PitcherID == None:
        PitcherID = Get_MLB_ID(PitcherName)
    PlayerDataFrame = GetMatchup(BatterName=BatterName,PitcherName=PitcherName,BatterID = BatterID,PitcherID = PitcherID)
    CSVFileName = "Matchup B{} P{} {} vs. {}.csv".format(BatterID,PitcherID,BatterName,PitcherName) 
    PlayerDataFrame.to_csv(CSVFileName,index=False)

def GetBatterTeamGamelogs(BatterName,OpponentTeamID,BatterID=None):
    if OpponentTeamID == None:
        print("Needs Team ID to function")
        return
    BBRefTeamID = GetBBRefTeamID(OpponentTeamID)
    Gamelogs = GenerateGamelog(BatterName,MLBID=BatterID)
    RelevantGamelogs = Gamelogs.loc[Gamelogs['Opp']==BBRefTeamID]
    return RelevantGamelogs

def GetBatterTeamGamelogsCSV(BatterName,OpponentTeamID,BatterID=None):
    Gamelogs = GetBatterTeamGamelogs(BatterName=BatterName,OpponentTeamID=OpponentTeamID,BatterID=BatterID)
    if BatterID == None:
        BatterMLBID = Get_MLB_ID(BatterName)
    MLBTeamID = GetMLBTeamID(OpponentTeamID)
    CSVFileName = "Matchup B{} T{} {} vs. {}.csv".format(BatterMLBID,MLBTeamID,BatterName,OpponentTeamID)
    Gamelogs.to_csv(CSVFileName,index=False)

if __name__ == '__main__':
    # print(GetMatchup("Buster Posey","Blake Snell"))
    # GetMatchupCSV("Buster Posey","Blake Snell")
    BatterList = ["Buster Posey", "Evan Longoria", "Kris Bryant"]
    Opponent = 'SDP'
    for BatterName in BatterList:
        GetBatterTeamGamelogsCSV(BatterName,Opponent)
