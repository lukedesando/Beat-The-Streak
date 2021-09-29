import numpy
from BackgroundFunctions import Get_MLB_ID, GetTeamKeyMap, rosterPlayers
from StatcastScrape import statcast_player
from GenerateGamelogs import GenerateGamelog, GenerateGamelogs
import pandas as pd
from BackgroundFunctions import Since2017String, Since2018String, Since2019String

# def GenerateDatabase(DatabaseFrame: DataFrame, AppendFrame: DataFrame):
#     DatabaseFrame = DatabaseFrame.append(AppendFrame)
#     return DatabaseFrame

dbyear = 2018

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
                PitcherStatcast = statcast_player(Player[0],MLBID=Player[1],position=Player[2],start_string=Since2018String)
                PitcherGamelogs = GenerateGamelogs(Player[0],MLBID=Player[1],position=Player[2],year=dbyear)
                PitcherEvents = PitcherStatcast.dropna(subset=['events'])

                PStatcastDatabase = PStatcastDatabase.append(PitcherStatcast)
                PEventsDatabase = PEventsDatabase.append(PitcherEvents)
                PGamelogsDatabase = PGamelogsDatabase.append(PitcherGamelogs)

            else:
                BatterStatcast = statcast_player(Player[0],MLBID=Player[1],position=Player[2],start_string=Since2018String)
                BatterGamelogs = GenerateGamelogs(Player[0],MLBID=Player[1],position=Player[2],year=dbyear)
                BatterEvents = BatterStatcast.dropna(subset=['events'])

                BStatcastDatabase = BStatcastDatabase.append(BatterStatcast)
                BEventsDatabase = BEventsDatabase.append(BatterEvents)
                BGamelogsDatabase = BGamelogsDatabase.append(BatterGamelogs)

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