import numpy
from BackgroundFunctions import Get_MLB_ID, GetTeamKeyMap, rosterPlayers
from StatcastScrape import statcast_player
from GenerateGamelogs import GenerateGamelog
import pandas as pd

# def GenerateDatabase(DatabaseFrame: DataFrame, AppendFrame: DataFrame):
#     DatabaseFrame = DatabaseFrame.append(AppendFrame)
#     return DatabaseFrame


PGamelogsDatabase = pd.DataFrame()
PStatcastDatabase = pd.DataFrame()
PEventsDatabase = pd.DataFrame()
BGamelogsDatabase = pd.DataFrame()
BStatcastDatabase = pd.DataFrame()
BEventsDatabase = pd.DataFrame()
TroublesomeNameDatabase = pd.DataFrame()

# NOTE: Apparently the fastest way to interate through a large dataset it with numpy
# https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06

AllTeams = GetTeamKeyMap()
# k = AllTeams.at[0,'MLBTeamID']
# print(k)

for ind,Team in AllTeams.iterrows():
    PlayerList = rosterPlayers(Team['MLBTeamID'])
    for Player in PlayerList:
        print(Player)
        try:
            if Player[2] == 'P':
                PitcherStatcast = statcast_player(Player[0],MLBID=Player[1])
                PitcherGamelogs = GenerateGamelog(Player[0],MLBID=Player[1])
                PitcherEvents = statcast_player(Player[0],Events=True,MLBID=Player[1])
                PStatcastDatabase = PStatcastDatabase.append(PitcherStatcast)
                PGamelogsDatabase = PGamelogsDatabase.append(PitcherGamelogs)
                PEventsDatabase = PEventsDatabase.append(PitcherEvents)
                pass
            else:
                PitcherStatcast = statcast_player(Player[0],MLBID=Player[1])
                PitcherGamelogs = GenerateGamelog(Player[0],MLBID=Player[1])
                PitcherEvents = statcast_player(Player[0],Events=True,MLBID=Player[1])
                BStatcastDatabase = BStatcastDatabase.append(PitcherStatcast)
                BGamelogsDatabase = BGamelogsDatabase.append(PitcherGamelogs)
                BEventsDatabase = BEventsDatabase.append(PitcherEvents)
        except Exception as e:
            print(e)
            TroublesomeNameDatabase = TroublesomeNameDatabase.append([str(e)])
            continue
    # print(EventsDatabase['player_name'])
PGamelogsDatabase.to_csv("DatabasePitcherGamelogs.csv",index=False)
PStatcastDatabase.to_csv("DatabasePitcherStatcast.csv",index=False)
PEventsDatabase.to_csv("DatabasePitcherEvents.csv",index=False)
BGamelogsDatabase.to_csv("DatabaseBatterGamelogs.csv",index=False)
BStatcastDatabase.to_csv("DatabaseBatterStatcast.csv",index=False)
BEventsDatabase.to_csv("DatabaseBatterEvents.csv",index=False)
TroublesomeNameDatabase.to_csv("DatabaseTroublesomeNames.csv",index=False)
print('Finished')