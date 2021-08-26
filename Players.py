from datetime import datetime, timedelta
from baseball_scraper import espn, playerid_lookup
from BackgroundFunctions import Find_Fangraph_ID, num_names
#Not sure why I had to import it, instead of putting it in this file
from pybaseball import playerid_reverse_lookup, pitching_stats

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
#I have no idea why this wouldn't work in the init file when I put it there

class Players:
	def __init__(self):
		self.player_keys = pd.read_excel('PlayerKeys.xlsx')
		self.starting_pitchers = self.get_starting_pitchers()
		self.matchups = self.get_todays_matchups()
		# todays_starters = self.todays_starting_pichers()

	def get_todays_matchups(self):
		matchups = {}
		for index, row in self.starting_pitchers.iterrows():
			matchups[row['Name']] = {
				'opponent': row['opponent'],
				'date': row['Date'], #FIXME chomp off time from date
				'pitcher_stats': self.get_pitcher_stats(row['espn_id']),
				'hitters': {}
			}
		return matchups
	def todays_starting_pichers(self):
		self.starters = espn.ProbableStartersScraper(Today, Today).scrape()
		# print(self.starters)

	def get_pitcher_stats(self, espn_id):
		try:
			pitcher_key = self.player_keys[self.player_keys['espn_id']==espn_id].reset_index().at[0, 'key_bbref']
		except KeyError as e:
			#FIXME Need to fix the case where a player is missing in player_keys
			print(f'Unable to get bbref key for the corresponding espn_id {espn_id}')
			return {}
		
		bbref_url = f'https://www.baseball-reference.com/players/{pitcher_key[0]}/{pitcher_key}.shtml'
		soup = requests.get(bbref_url)
		page = bs4.BeautifulSoup(soup.text, 'html.parser')
		try:
			#FIXME does not get pitching table when id doesn't include year; see https://www.baseball-reference.com/players/o/ohtansh01.shtml
			
			row = page.find('tr', id=f'pitching_standard.{datetime.today().year}')
			values = row.find_all('td') 
		except AttributeError as e:
			print(f'Could not find {datetime.today().year} Standard Pitching stats at {bbref_url}')
			with open("output1.html", "w") as file:
				file.write(str(page))
			return {}
		
		return {value['data-stat']: value.text for value in values}
	
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
		# print(missing_pitcher_keys)
		self.player_keys = self.player_keys.append(missing_pitcher_keys, ignore_index=True)
		#need to drop index from adding
		self.player_keys.to_excel("PlayerKeys.xlsx",index=False)
		#self.player_keys.to_csv("PlayerKeys.csv",index=False)
		return starters
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
	
	def matchups_to_csv(self, stats, filename='pitcher_stats'):
		out = []
		for key, value in self.matchups.items():
			item = {}
			item['name'] = key
			item['opponent'] = value['opponent']
			item['date'] = value['date']
			for p_key, p_stat in value['pitcher_stats'].items():
				if (p_key in stats):
					item[p_key] = p_stat
			out.append(item)

		pd.DataFrame(out).to_excel(f'{filename}.xlsx')

def playerid_reverse_lookup_Fangraphs_Sheet(player_name):
	FGid = Find_Fangraph_ID(player_name) #Why won't this read in the same file? I had to move it to background functinons
	Fangraph_Keys_List = [FGid]
	#print(FGid)
	return playerid_reverse_lookup(Fangraph_Keys_List,key_type='fangraphs')

	#def find_player_in_key(player_name):
