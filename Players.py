from datetime import datetime, timedelta
from baseball_scraper import espn, playerid_lookup
from BackgroundFunctions import Find_Fangraph_ID, num_names
#Not sure why I had to import it, instead of putting it in this file
from pybaseball import playerid_reverse_lookup

import requests
import io
import bs4
import pandas as pd
import numpy as np
import csv
import sys

#Important Global Variables
Today = datetime.today()
Tomorrow = datetime.today() + timedelta(days=1)
FanGraphsCSV = csv.reader(open('FanGraphs_Players_IDs_2021.csv', "r"), delimiter=",")
Name_Column = FanGraphsCSV['Name']
#I have no idea why this wouldn't work in the init file when I put it there

class Players:
	def __init__(self):
		self.player_keys = pd.read_excel('PlayerKeys.xlsx')
		self.starting_pitchers = self.get_starting_pitchers()
		todays_starters = self.todays_starting_pichers()

	def todays_starting_pichers(self):
		self.starters = espn.ProbableStartersScraper(Today, Today).scrape()
		print(self.starters)
	
	def get_starting_pitchers(self):
		starters = espn.ProbableStartersScraper(Today, Tomorrow).scrape()
		missing_pitcher_keys = []
		for ind, row in starters.iterrows():
			if row['espn_id'] not in self.player_keys.espn_id.values:
				id_list = self.search_keys(row['Name'])
                
				if id_list is not None:
					id_list['espn_id'] = row['espn_id']
					# id_list = pd.DataFrame([id_list])
					missing_pitcher_keys.append(id_list)
		print(missing_pitcher_keys)
		self.player_keys = self.player_keys.append(missing_pitcher_keys, ignore_index=True)
		#need to drop index from adding
		self.player_keys.to_excel("PlayerKeys.xlsx",index=False)
		#self.player_keys.to_csv("PlayerKeys.csv",index=False)

		#We need to separate this fuction into a GETSTARTINGPITCHER and a APPEND-EXCEL
		#The append needs to be reusable
		#Also need to update the FanGraphs_Players_IDs_2021 file on occasion (lower priority)
                
	def search_keys(self, player_name):
           
		try:
			if num_names(player_name) == 3:
				pname0,pname1,pname2 = player_name.split(" ")
				PlayerFirstName = pname0 + " " + pname1
				PlayerLastName = pname2
			else:
				PlayerFirstName,PlayerLastName=player_name.split(" ")
			Player_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)
        
			# player = Player_Dataframe.iloc[Player_Dataframe.mlb_played_last.argmax()]
			return Player_Dataframe.iloc[Player_Dataframe.mlb_played_last.argmax()].to_dict()
		except ValueError as e:
			print(f'Problem searching for {player_name}\nerror: {e}')
			return None

def playerid_reverse_lookup_Fangraphs_Sheet(player_name):
	FGid = Find_Fangraph_ID(player_name) #Why won't this read in the same file? I had to move it to background functinons
	Fangraph_Keys_List = [FGid]
	#print(FGid)
	return playerid_reverse_lookup(Fangraph_Keys_List,key_type='fangraphs')

	#def find_player_in_key(player_name):

def Update_Key_Excel():
	for player_name in Name_Column:
		FanGraphID = Find_Fangraph_ID(player_name)
		row_check = player_keys.loc[player_keys.isin([FanGraphID]).any(axis=1)] #needs to only search key_fangraphs column
		if row_check.empty:
			new_row = Players.playerid_reverse_lookup_Fangraphs_Sheet(player_name)
			player_keys=player_keys.append(new_row,ignore_index=True)
			player_keys.to_excel("PlayerKeys.xlsx",index=False)

	
# def compare_and_append(player_name):
# 	FanGraphs_ID = Players.playerid_reverse_lookup_Fangraphs(player_name)
# 	#print(FanGraphs_ID)
# 	player_keys = pd.read_excel('PlayerKeys.xlsx')
# 	player_keys=player_keys.append(FanGraphs_ID,ignore_index=True)
# 		#if
# 			#player_keys.to_excel("PlayerKeys.xlsx",index=False)



#print(player_keys)
#It works, but it will duplicate. Need an apend-excel function to make it dynamic

#Feel free to clean it up and make it work better