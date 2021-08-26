from baseball_scraper import espn, playerid_lookup
from BackgroundFunctions import Find_Fangraph_ID, num_names

#FIXME It's all here, just needs to be cleaned up into a function

player_name = "Trea Turner"
#TODO Need Player_Type to be automatically configured as p for pitcher or b for batter, otherwise it'll take forever
batter_or_pitcher = "batter"
b_or_p = "b"
bat_or_pitch = "bat"
Year = 2020


PlayerFirstName,PlayerLastName=player_name.split(" ")
Player_ID_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)

#TODO for names with 3 names
# try:
#     if num_names(player_name) == 3:
#         pname0,pname1,pname2 = player_name.split(" ")
#         PlayerFirstName = pname0 + " " + pname1
#         PlayerLastName = pname2
#     else:
#         PlayerFirstName,PlayerLastName=player_name.split(" ")
#     Player_ID_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)
#     print(Player_ID_Dataframe)

# except ValueError as e:
#     print(f'Problem searching for {player_name}\nerror: {e}')

SanitizedIDFrame = Player_ID_Dataframe.loc[Player_ID_Dataframe['mlb_played_last']==2021]
BBRefKey = SanitizedIDFrame['key_bbref']

SanitizedBBRefKey = BBRefKey.to_string(index=False)
BBRefLetter = SanitizedBBRefKey[0]

hyperlink_Main_Page = "\fhttps://www.baseball-reference.com/players/%s/%s.shtml" % (BBRefLetter,SanitizedBBRefKey)
print(hyperlink_Main_Page)

hyperlink_GameLogs = "\fhttps://www.baseball-reference.com/players/gl.fcgi?id=%s&t=%s&year=%d" % (SanitizedBBRefKey,Player_Type,Year)
print(hyperlink_GameLogs)

hyperlink_Splits = "\fhttps://www.baseball-reference.com/players/split.fcgi?id=%s&year=%d&t=%s" % (SanitizedBBRefKey,Year,Player_Type)
print(hyperlink_Splits)

hyperlink_AdvancedStats = "\fhttps://www.baseball-reference.com/players/%s/%s-%s.shtml" % (BBRefLetter,SanitizedBBRefKey,Bat_Or_Pitch)
print (hyperlink_AdvancedStats)