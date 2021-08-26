import pandas as pd
import Players
from BackgroundFunctions import Find_Fangraph_ID
from Players import playerid_reverse_lookup_Fangraphs_Sheet


player_keys = pd.read_excel('PlayerKeys.xlsx')
Fangraphs_ID_Sheet = pd.read_csv('FanGraphs_Players_IDs_2021.csv',)
Name_Column = Fangraphs_ID_Sheet['Name']
Player_Names_Keys = player_keys['name_first']
Fangraph_ID_To_Update_Column = player_keys['key_fangraphs']
result = []
index=-1

#turning into fuction so it can not itit every time

def Update_Key_Excel():
	for player_name in Name_Column:
		FanGraphID = Find_Fangraph_ID(player_name)
		row_check = player_keys.loc[player_keys.isin([FanGraphID]).any(axis=1)] #needs to only search key_fangraphs column
		if row_check.empty:
			new_row = Players.playerid_reverse_lookup_Fangraphs_Sheet(player_name)
			player_keys=player_keys.append(new_row,ignore_index=True)
			player_keys.to_excel("PlayerKeys.xlsx",index=False)


#There's a number of players on the Fangraphs csv that do not have a Fangraphs_ID
# Mostly players who joined league in 2020 to 2021
# Theorized way: grab fangraph ids from csv, then match them against player keys
#

for Fangraphs_key in Fangraph_ID_To_Update_Column:
	index += 1
	if Fangraphs_key == -1:
		player_name = Name_Column
		print (Name_Column)
		#Fangraphs_key = Find_Fangraph_ID(player_name)
		#player_keys.to_excel