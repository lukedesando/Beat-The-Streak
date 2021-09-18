from numpy import empty
from GenerateGamelogs import GenerateGamelog
from BackgroundFunctions import Get_BBRef_and_MLB_ID, Get_MLB_ID, GetBBRefTeamID, GetMLBTeamID, rosterPlayers
from StatsCollation import BeginningofYearString
from StatcastScrape import statcast_player


from pandas.core.frame import DataFrame

#TODO: Get Buster Posey's numbers off Giants in 2021

def GetMatchup(BatterName, PitcherName, BatterID = None, PitcherID = None, Events = False, StartDateString=BeginningofYearString):
    '''Returns a dataframe with all pitches thrown between two players in 2021
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
    PlayerDataFrame = GetMatchup(BatterName=BatterName,PitcherName=PitcherName,BatterID = BatterID,PitcherID = PitcherID,Events=Events,StartDateString=StartDateString)
    if PlayerDataFrame.empty:
        print("No Matchup Data for {} versus {}".format(BatterName,PitcherName))
        return
    if Events == False:
        CSVFileName = "Matchup B{} P{} {} vs. {}.csv".format(BatterID,PitcherID,BatterName,PitcherName)
    else:
        CSVFileName = "Matchup B{} P{} Events {} vs. {}.csv".format(BatterID,PitcherID,BatterName,PitcherName)
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
    # # print(GetMatchup("Buster Posey","Blake Snell"))
    # # GetMatchupCSV("Buster Posey","Blake Snell")
    # SanitizedMatchup = GetMatchup("Buster Posey","Blake Snell",Events=True)
    # # FinalBoss = SanitizedMatchup.loc[SanitizedMatchup['events']=='walk']
    # print (SanitizedMatchup)
    # GetMatchupCSV("Buster Posey","Blake Snell",Events=True)

    BatterList = ["Kris Bryant", "Juan Soto"]
    Opponent = 'Blake Snell'
    for BatterName in BatterList:
        GetMatchupCSV(BatterName,Opponent,StartDateString='2016-01-01')
        #GetMatchupCSV(BatterName,Opponent,Events=True)
