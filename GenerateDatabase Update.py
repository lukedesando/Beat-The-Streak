import numpy as np
from pandas.io.parsers import read_csv
from BackgroundFunctions import Get_MLB_ID, GetTeamKeyMap, rosterPlayers
from StatcastScrape import statcast_player
from GenerateGamelogs import GenerateGamelog
import pandas as pd

playername = "Bryce Harper"
# def GenerateDatabase(DatabaseFrame: DataFrame, AppendFrame: DataFrame):
#     DatabaseFrame = DatabaseFrame.append(AppendFrame)
#     return DatabaseFrame
BatGamelogs = read_csv("DatabaseBatterGamelogsCopy.csv",delimiter=",")
BatGamelogs = BatGamelogs.to_numpy()
NewLogs = GenerateGamelog("Bryce Harper")
NewLogs = NewLogs.to_numpy()
test = BatGamelogs.append(NewLogs)
print(test)



# BatEvents = np.genfromtxt("DatabaseBatterEvents.csv")
# 
# 
# BatGamelogs = np.genfromtxt("DatabaseBatterGamelogs.csv",delimiter=",")
# )
# print(NewLogs)
# NewLogs = NewLogs.to_numpy()
# print(NewLogs)
# PGamelogsDatabase = np.array()

# BGamelogsDatabase = np.array()

# TroublesomeNameDatabase = np.array()
# test = np.concatenate((BatGamelogs,NewLogs), axis=1)

test = BatGamelogs.append(NewLogs)
print(test)

merged = pd.merge(BatGamelogs,NewLogs,how='inner',indicator=True)

test.to_csv('utest.csv')
merged.to_csv("xtest.csv")

# np.concatenate(BatEvents, NewEvents)

# NOTE: Apparently the fastest way to interate through a large dataset it with numpy
# https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06

# AllTeams = GetTeamKeyMap()
# # k = AllTeams.at[0,'MLBTeamID']
# # print(k)

# for ind,Team in AllTeams.iterrows():
#     PlayerList = rosterPlayers(Team['MLBTeamID'])
#     for Player in PlayerList:
#         print(Player)
#         try:
#             if Player[2] == 'P':
#                 PitcherStatcast, PitcherEvents = statcast_player(Player[0],MLBID=Player[1])
#                 PitcherGamelogs = GenerateGamelog(Player[0],MLBID=Player[1])
#                 # PitcherEvents = statcast_player(Player[0],Events=True,MLBID=Player[1])
#                 PStatcastDatabase = PStatcastDatabase.append(PitcherStatcast)
#                 PGamelogsDatabase = PGamelogsDatabase.append(PitcherGamelogs)
#                 PEventsDatabase = PEventsDatabase.append(PitcherEvents)
#                 pass
#             else:
#                 BatterStatcast,BatterEvents = statcast_player(Player[0],MLBID=Player[1])
#                 BatterGamelogs = GenerateGamelog(Player[0],MLBID=Player[1])
#                 # BatterEvents = statcast_player(Player[0],Events=True,MLBID=Player[1])
#                 BStatcastDatabase = BStatcastDatabase.append(BatterStatcast)
#                 BGamelogsDatabase = BGamelogsDatabase.append(BatterGamelogs)
#                 BEventsDatabase = BEventsDatabase.append(BatterEvents)
#         except Exception as e:
#             print(e)
#             TroublesomeNameDatabase = TroublesomeNameDatabase.append([str(e)])
#             continue
#     # print(EventsDatabase['player_name'])
# PGamelogsDatabase.to_csv("DatabasePitcherGamelogs.csv",index=False)
# PStatcastDatabase.to_csv("DatabasePitcherStatcast.csv",index=False)
# PEventsDatabase.to_csv("DatabasePitcherEvents.csv",index=False)
# BGamelogsDatabase.to_csv("DatabaseBatterGamelogs.csv",index=False)
# BStatcastDatabase.to_csv("DatabaseBatterStatcast.csv",index=False)
# BEventsDatabase.to_csv("DatabaseBatterEvents.csv",index=False)
# TroublesomeNameDatabase.to_csv("DatabaseTroublesomeNames.csv",index=False)
# print('Finished')