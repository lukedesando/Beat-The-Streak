import pandas as pd
import Players
from BackgroundFunctions import Find_Fangraph_ID
from Players import playerid_reverse_lookup_Fangraphs_Sheet


player_keys = pd.read_excel('PlayerKeys.xlsx')
Fangraphs_ID_Sheet = pd.read_csv('FanGraphs_Players_IDs_2021.csv',)
Name_Column = Fangraphs_ID_Sheet['Name']

for player_name in Name_Column:
	FanGraphID = Find_Fangraph_ID(player_name)
	row_check = player_keys.loc[player_keys.isin([FanGraphID]).any(axis=1)] #needs to only search key_fangraphs column
	if row_check.empty:
		new_row = Players.playerid_reverse_lookup_Fangraphs_Sheet(player_name)
		player_keys=player_keys.append(new_row,ignore_index=True)
		player_keys.to_excel("PlayerKeys.xlsx",index=False)