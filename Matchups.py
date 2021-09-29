from GenerateGamelogs import GenerateGamelog
from BackgroundFunctions import Get_MLB_ID, GetBBRefTeamID, GetMLBTeamID, rosterPlayers
from BackgroundFunctions import Today, BeginningofYearString, CurrentYear, Since2017String
from StatcastScrape import statcast_player
from PlayerPrintouts import GetStartingPitchers, RosterBatterStatsPrintout,PrintPlayerStats
# from baseball_scraper import espn

#TODO: Get Buster Posey's numbers off Giants in 2021

def GetMatchup(BatterName, PitcherName, BatterID = None, PitcherID = None, Events = True, StartDateString=BeginningofYearString):
    '''Returns a dataframe with all pitches thrown between two players in the current year
    \n Batter first. If you want to only see the events, set Events = True'''
    if BatterID == None:
        BatterID = Get_MLB_ID(BatterName)
    if PitcherID == None:
        PitcherID = Get_MLB_ID(PitcherName)
    PlayerDataFrame = statcast_player(BatterID,StartDateString,position="B",Events=Events)
    MatchupFrame = PlayerDataFrame.loc[PlayerDataFrame['pitcher']==PitcherID]
    # if Events == True:
    #     MatchupFrame = MatchupFrame.dropna(subset=['events'])
    return MatchupFrame

def GetMatchupCSV(BatterName = None,PitcherName = None,BatterID = None,PitcherID = None,Events=True,StartDateString=BeginningofYearString):
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
    try:
        Gamelogs = GenerateGamelog(BatterName,MLBID=BatterID)
    except Exception as e:
        raise e
    RelevantGamelogs = Gamelogs.loc[Gamelogs['Opp']==BBRefTeamID]
    return RelevantGamelogs

def GetBatterTeamGamelogsCSV(BatterName,OpponentTeamID,BatterID=None,year=CurrentYear):
    Gamelogs = GetBatterTeamGamelogs(BatterName=BatterName,OpponentTeamID=OpponentTeamID,BatterID=BatterID)
    if BatterID == None:
        BatterID = Get_MLB_ID(BatterName)
    MLBTeamID = GetMLBTeamID(OpponentTeamID)
    CSVFileName = "Matchup B{} T{} {} {} vs. {}.csv".format(BatterID,MLBTeamID,year,BatterName,OpponentTeamID)
    Gamelogs.to_csv(CSVFileName,index=False)


if __name__ == '__main__':
    # batterlist = ['Corey Seager','David Fletcher','Justin Turner']
    # pitcherlist = ['Ryan Weathers', 'Taylor Hearn', 'Ryan Weathers']
    # for batter, pitcher in zip(batterlist, pitcherlist):
    #     GetMatchupCSV(batter,pitcher)
    # print(Get_MLB_ID("Ryan Weathers"))
    # print(Get_MLB_ID("Justin Turner"))
    GetMatchupCSV("Corey Seager","Ryan Weathers",608369,677960)
    GetMatchupCSV("Justin Turner","Ryan Weathers",608369,457759)
    pass
    # # print(GetMatchup("Buster Posey","Blake Snell"))
    # # GetMatchupCSV("Buster Posey","Blake Snell")
    # SanitizedMatchup = GetMatchup("Buster Posey","Blake Snell",Events=True)
    # # FinalBoss = SanitizedMatchup.loc[SanitizedMatchup['events']=='walk']
    # print (SanitizedMatchup)
    # GetMatchupCSV("Buster Posey","Blake Snell",Events=True)

    # BatterList = ["Kris Bryant", "Juan Soto", "Bryce Harper"]
    # Opponent = 'Clayton Kershaw'
    # for BatterName in BatterList:
    #     GetMatchupCSV(BatterName,Opponent,StartDateString='2016-01-01')
    #     #GetMatchupCSV(BatterName,Opponent,Events=True)