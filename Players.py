from datetime import datetime, timedelta
from baseball_scraper import espn, playerid_lookup


import requests
import io
import bs4
import pandas as pd
import numpy as np

class Players:
    def __init__(self):
        self.player_keys = pd.read_excel('PlayerKeys.xlsx')
        self.starting_pitchers = self.get_starting_pitchers()
    
    def get_starting_pitchers(self):
        starters = espn.ProbableStartersScraper(datetime.today(), datetime.today() + timedelta(days=1)).scrape()
        
        missing_pitcher_keys = []
        for index, row in starters.iterrows():
            if row['espn_id'] not in self.player_keys.espn_id.values:
                id_list = self.search_keys(row['Name'])
                
                if id_list is not None:
                    id_list['espn_id'] = row['espn_id']
                    # id_list = pd.DataFrame([id_list])
                    missing_pitcher_keys.append(id_list)
        print(missing_pitcher_keys)
        self.player_keys = self.player_keys.append(missing_pitcher_keys, ignore_index=True)
        self.player_keys.to_excel("PlayerKeys.xlsx")
        
                
    def search_keys(self, player_name):
              
        try:
            PlayerFirstName,PlayerLastName=player_name.split(" ")
        
        
            Player_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)
        
            # player = Player_Dataframe.iloc[Player_Dataframe.mlb_played_last.argmax()]
            return Player_Dataframe.iloc[Player_Dataframe.mlb_played_last.argmax()].to_dict()
        except ValueError as e:
            print(f'problem searching {player_name}\nerror: {e}')
            return None
  
test = Players()
#print(test.keys)
