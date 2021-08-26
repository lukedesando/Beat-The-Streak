import statsapi
from statsapi import player_stats,player_stat_data,lookup_player

def Get_Player_ID(PlayerName):
    "Because I'm Lazy"
    PlayerJson = statsapi.lookup_player(PlayerName)
    PlayerID = PlayerJson[0]['id']
    return PlayerID




pitcherID = Get_Player_ID("Patrick Sandoval")
print(player_stat_data(pitcherID,group='pitching'))

batterID = Get_Player_ID("Juan Soto")
print(player_stat_data(batterID,group='batting'))