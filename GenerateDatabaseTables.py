from os import name
import numpy
from BackgroundFunctions import Get_MLB_ID, GetTeamKeyMap, rosterPlayers
from StatcastScrape import statcast_player
from GenerateGamelogs import GenerateGamelog, GenerateGamelogs
import pandas as pd
from BackgroundFunctions import Since2015String, Since2017String, Since2018String, UpdateChadwick

# def GenerateDatabase(DatabaseFrame: DataFrame, AppendFrame: DataFrame):
#     DatabaseFrame = DatabaseFrame.append(AppendFrame)
#     return DatabaseFrame
if __name__ == '__main__':
    UpdateChadwick()

dbyear = 2015
SinceYearString = Since2015String

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
        # print(Player)
        try:
            if Player[2] == 'P':
                PitcherStatcast = statcast_player(Player[0],MLBID=Player[1],position=Player[2],start_string=SinceYearString)
                PitcherGamelogs = GenerateGamelogs(Player[0],MLBID=Player[1],position=Player[2],year=dbyear)
                PitcherEvents = PitcherStatcast.dropna(subset=['events'])

                PStatcastDatabase = PStatcastDatabase.append(PitcherStatcast)
                PEventsDatabase = PEventsDatabase.append(PitcherEvents)
                PGamelogsDatabase = PGamelogsDatabase.append(PitcherGamelogs)

            else:
                BatterStatcast = statcast_player(Player[0],MLBID=Player[1],position=Player[2],start_string=SinceYearString)
                BatterGamelogs = GenerateGamelogs(Player[0],MLBID=Player[1],position=Player[2],year=dbyear)
                BatterEvents = BatterStatcast.dropna(subset=['events'])

                BStatcastDatabase = BStatcastDatabase.append(BatterStatcast)
                BEventsDatabase = BEventsDatabase.append(BatterEvents)
                BGamelogsDatabase = BGamelogsDatabase.append(BatterGamelogs)

        except Exception as e:
            print(e)
            print(Player)
            TroublesomeNameDatabase = TroublesomeNameDatabase.append([str(e)])
            TroublesomeNameDatabase = TroublesomeNameDatabase.append(Player)
            continue
    # print(EventsDatabase['player_name'])
PGamelogsDatabase.to_csv("PitcherGamelogs.csv",index=False)
PStatcastDatabase.to_csv("PitcherStatcast.csv",index=False)
PEventsDatabase.to_csv("PitcherEvents.csv",index=False)
BGamelogsDatabase.to_csv("BatterGamelogs.csv",index=False)
BStatcastDatabase.to_csv("BatterStatcast.csv",index=False)
BEventsDatabase.to_csv("BatterEvents.csv",index=False)
TroublesomeNameDatabase.to_csv("DatabaseTroublesomeNames.csv",index=False)
print('Finished')