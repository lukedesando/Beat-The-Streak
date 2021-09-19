import csv
from pandas.core.frame import DataFrame
from statsapi import player_stats,player_stat_data,lookup_player, roster,schedule
import pandas as pd
from datetime import date, datetime,timedelta
from statsapi import get

#Important Variables

Today = date.today()
Tomorrow = date.today() + timedelta(days=1)
Yesterday = date.today() + timedelta(days=-1)
FiveDaysAgo = date.today() + timedelta(days=-5)
CurrentYear = date.today().year

TodayString = str(Today)
TomorrowString = str(Tomorrow)
YesterdayString = str(Yesterday)
FiveDaysAgoString = str(FiveDaysAgo)
BeginningofYearString = '2021-01-01'
Since2017String = '2017-01-01'


def num_names(PlayerName):
    count=PlayerName.count(" ")+1
    return count

#HACK There has to be a better way to do this
def Name_Check(PlayerName):
    namesNum = num_names(PlayerName)
    if namesNum == 2:
        if "." in PlayerName:
            PlayerFirstName,PlayerLastName = PlayerName.split(" ")
            idx = PlayerFirstName.index(".")+1
            PlayerFirstName = PlayerFirstName[:idx]+" "+PlayerFirstName[idx:]
            PlayerName = PlayerFirstName +" " + PlayerLastName
            namesNum = 3
    if namesNum == 3:
        if "Jr" in PlayerName:
            pname0,pname1,pname2 = PlayerName.split(" ")
            PlayerFirstName = pname0
            PlayerLastName = pname1
            PlayerName = PlayerFirstName +" " + PlayerLastName
            namesNum = 2
    return namesNum, PlayerName

#FIXME: calls numnames twice, once through period check and next through calling it
def Player_Dataframe_Fetch(PlayerName):
    namesNum, PlayerName = Name_Check(PlayerName)
    troublesome_names = {
        "Phil Gosselin": ('Philip', "Gosselin")
    }
    try:
        if (PlayerName in troublesome_names):
            PlayerFirstName,PlayerLastName = troublesome_names[PlayerName]
        # else:
        elif namesNum == 3:
            pname0,pname1,pname2 = PlayerName.split(" ")
            PlayerFirstName = pname0 + " " + pname1
            PlayerLastName = pname2
        else:
            PlayerFirstName,PlayerLastName=PlayerName.split(" ")
        Player_ID_Dataframe = playerid_lookup(PlayerLastName,PlayerFirstName)
        return Player_ID_Dataframe
    except ValueError as e:
        print(f'Problem searching for {PlayerName}\nerror: {e}')

def Get_MLB_ID(PlayerName):
    "May cause errors for players with identical names to other players"
    try:
        PlayerJson = lookup_player(PlayerName)
        PlayerID = PlayerJson[0]['id']
        return PlayerID
    except IndexError as e:
        print (f'Problem searching for {PlayerName}\nerror: {e}')
    
def CheckPosition(PlayerNameorMLBID):
    try:
        PlayerJson = lookup_player(PlayerNameorMLBID)
        PlayerPosition = PlayerJson[0]['primaryPosition']
        PlayerAbb = PlayerPosition['abbreviation']
        return PlayerAbb
    except IndexError as e:
        print (f'Problem searching for {PlayerNameorMLBID}\nerror: {e}')

def Get_BBRef_and_MLB_ID(PlayerName):
    "First Name, Last Name, Returns BBRef and MLB"
    errorID = 'Series([], )'

    Player_ID_Dataframe = Player_Dataframe_Fetch(PlayerName)
    
    #TODO: Luis Garcia Exception
    #FIXME: Luis Garcia gets treated like he doesn't exist until I figure out how to do this right


    SanitizedIDFrame = Player_ID_Dataframe.loc[Player_ID_Dataframe['mlb_played_last']==2021]
    SanLength = len(SanitizedIDFrame.index)
    if SanLength > 1:
        print (SanitizedIDFrame)
        print(str(SanLength) + ' players found with name {}'.format(PlayerName))
        return errorID, errorID

    BBRefKey = SanitizedIDFrame['key_bbref']
    MLBKey = SanitizedIDFrame['key_mlbam']
    SanitizedMLBKey = MLBKey.to_string(index=False)
    SanitizedBBRefKey = BBRefKey.to_string(index=False)
    return SanitizedBBRefKey, SanitizedMLBKey

def Get_BBRefID_From_MLBID(MLBID):
    "Needs to import MLBID as a list"
    if not isinstance(MLBID,list):
        MLBID = [MLBID]
    Player_ID_Dataframe = playerid_reverse_lookup(MLBID)
    SanitizedIDFrame = Player_ID_Dataframe.loc[Player_ID_Dataframe['mlb_played_last']==2021]
    BBRefKey = SanitizedIDFrame['key_bbref']
    SanitizedBBRefKey = BBRefKey.to_string(index=False)
    return SanitizedBBRefKey

#print(Get_BBRef_ID("Chi Chi Gonzalez"))

#NOTE Relies on external database; will need to be updated occasionally
#FIXME depreciated
def Find_Fangraph_ID(player_name):
    #loop through the csv list
    FanGraphsCSV = csv.reader(open('FanGraphs_Players_IDs_2021.csv', "r"), delimiter=",")
    for row in FanGraphsCSV: #Not reading in init file for some reason?
        #if current rows 2nd value is equal to input, print that row
        if player_name == row[0]:
            FGid = row[2]
            #print(FGid)
            return int(FGid)

#FIXME: Need input of MLBID to run faster
#FIXME: Need position, because batters who pitched in a game come up as pitchers
def Check_batting_or_pitching(MLBID,year=CurrentYear):
    '''Returns 3 values'''
    
    if CheckPosition(MLBID) == 'P':
        return "pitching","pitch","p"
    else:
        return "batting","bat","b"

def Check_bat_or_pitch(BBRefPlayerID,year=CurrentYear):
    "Returns 1 value"
    try:
        SplitsSeasonTotalsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
id%3D{}%26year%3D{}%26t%3Dp&div=div_total_extra'''.format(BBRefPlayerID,year)
        pd.read_html(SplitsSeasonTotalsPitchersURL)
        return "pitch"
    except ImportError:
        return "bat"

def ConfirmList(MyString):
    if not isinstance(MyString,list):
        MyString = [MyString]
    return MyString

def rosterPlayers(teamId, rosterType=None, season=datetime.now().year, date=None):
    """Get the roster for a given team."""
    if not rosterType:
        rosterType = "active"

    params = {"rosterType": rosterType, "season": season, "teamId": teamId}
    if date:
        params.update({"date": date})

    r = get("team_roster", params)

    players = []
    for x in r["roster"]:
        players.append(
            [x["person"]["fullName"], x["person"]['id'], x["position"]["abbreviation"]]
        )

    return players

def GetMLBTeamID(TeamID):
    '''Totally universal in application; will search any and all team ID names across multiple files
    \n if it isn't found, editing needs to be done to the Team Map'''
    df = GetTeamKeyMap()
    df = df[df.isin([TeamID]).any(axis=1)]
    MLBTeamID = df['MLBTeamID'].to_string(index=False)
    return MLBTeamID

def GetBBRefTeamID(TeamID):
    '''Totally universal in application; will search any and all team ID names across multiple files
    \n if it isn't found, editing needs to be done to the Team Map'''
    df = GetTeamKeyMap()
    df = df[df.isin([TeamID]).any(axis=1)]
    BBRefID = df['BBREFTEAM'].to_string(index=False)
    return BBRefID

def GetTeamKeyMap():
    '''I don't feel like remembering this file name
    \n Set it equal to a variable and you can use it in any team key lookup functions'''
    MLBTeamDataframe = pd.read_csv('MLB Team Map.csv')
    return MLBTeamDataframe

def get_lookup_table():
    # print('Gathering player lookup table. This may take a moment.')
    # url = "https://raw.githubusercontent.com/chadwickbureau/register/master/data/people.csv"
    s="Chadwick Bureau People.csv"
    # table = pd.read_csv(io.StringIO(s.decode('utf-8')), dtype={'key_sr_nfl': object, 'key_sr_nba': object, 'key_sr_nhl': object})
    table = pd.read_csv(s, dtype={'key_sr_nfl': object, 'key_sr_nba': object, 'key_sr_nhl': object})
    #subset columns
    cols_to_keep = ['name_last','name_first','key_mlbam', 'key_retro', 'key_bbref', 'key_fangraphs', 'mlb_played_first','mlb_played_last']
    table = table[cols_to_keep]
    #make these lowercase to avoid capitalization mistakes when searching
    table['name_last'] = table['name_last'].str.lower()
    table['name_first'] = table['name_first'].str.lower()
    # Pandas cannot handle NaNs in integer columns. We need IDs to be ints for successful queries in statcast, etc. 
    # Workaround: replace ID NaNs with -1, then convert columns to integers. User will have to understand that -1 is not a valid ID. 
    table[['key_mlbam', 'key_fangraphs']] = table[['key_mlbam', 'key_fangraphs']].fillna(-1)
    table[['key_mlbam', 'key_fangraphs']] = table[['key_mlbam', 'key_fangraphs']].astype(int) # originally returned as floats which is wrong
    return table


def playerid_lookup(last, first=None):
    # force input strings to lowercase
    last = last.lower()
    if first:
        first = first.lower()
    table = get_lookup_table()
    if first is None:
        results = table.loc[table['name_last']==last]
    else:
        results = table.loc[(table['name_last']==last) & (table['name_first']==first)]
    #results[['key_mlbam', 'key_fangraphs', 'mlb_played_first', 'mlb_played_last']] = results[['key_mlbam', 'key_fangraphs', 'mlb_played_first', 'mlb_played_last']].astype(int) # originally returned as floats which is wrong
    results = results.reset_index().drop('index', axis=1)
    return results

# data = playerid_lookup('bonilla')
# data = playerid_lookup('bonilla', 'bobby')

def playerid_reverse_lookup(player_ids, key_type=None):
    """Retrieve a table of player information given a list of player ids

    :param player_ids: list of player ids
    :type player_ids: list
    :param key_type: name of the key type being looked up (one of "mlbam", "retro", "bbref", or "fangraphs")
    :type key_type: str

    :rtype: :class:`pandas.core.frame.DataFrame`
    """
    key_types = ('mlbam', 'retro', 'bbref', 'fangraphs', )

    if not key_type:
        key_type = key_types[0]     # default is "mlbam" if key_type not provided
    elif key_type not in key_types:
        raise ValueError(
            '[Key Type: {}] Invalid; Key Type must be one of "{}"'.format(key_type, '", "'.join(key_types))
        )

    table = get_lookup_table()
    key = 'key_{}'.format(key_type)

    results = table[table[key].isin(player_ids)]
    results = results.reset_index().drop('index', axis=1)
    return results

#Testing Fuctions
if __name__ == '__main__':
    # print(Player_Dataframe_Fetch('Phil Gosselin'))
    print(GetMLBTeamID('WAS'))
    print(GetMLBTeamID('WSN'))
    print(GetMLBTeamID('Nationals'))