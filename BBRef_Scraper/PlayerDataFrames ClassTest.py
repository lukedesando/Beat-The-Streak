import pandas as pd
from functools import partial

class BBRefURLs:
    def __init__(self,PlayerID,year,batting_or_pitching,b_or_p):
    GameLogsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fgl.fcgi%3F\
    id%3D{}%26t%3D{}%26year%3D{}&div=div_{}_gamelogs'''.format(PlayerID,b_or_p,year,batting_or_pitching)

    SplitsSeasonTotalsURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
    id%3D{}%26year%3D{}%26t%3D{}&div=div_total'''.format(PlayerID,year,b_or_p)

    SplitsSeasonTotalsPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
    id%3D{}%26year%3D{}%26t%3Dp&div=div_total_extra'''.format(PlayerID,year)
    #NOTE: widget is designed for only pitchers; does not exist for hitters

    SplitsPlatoonURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
    id%3D{}%26year%3D{}%26t%3D{}&div=div_plato'''.format(PlayerID,year,b_or_p)

    SplitsPlatoonPitchersURL = '''https://widgets.sports-reference.com/wg.fcgi?css=1&site=br&url=%2Fplayers%2Fsplit.fcgi%3F\
    id%3D{}%26{}%3D2021%26t%3Dp&div=div_hmvis_extra'''.format(PlayerID,year)

class PlayerDataframes:

    def __init__(self):
        PlayerGameLogs=pd.read_html(GameLogsURL)[0].query('R != "R"')\
            .drop('Unnamed: 5', axis=1)\
            .apply(partial(pd.to_numeric, errors='ignore'))\
            .reset_index(drop=True)

        Splits = pd.read_html(SplitsSeasonTotalsURL)[0].query('G != "G"')\
            .apply(partial(pd.to_numeric, errors='ignore'))\
            .reset_index(drop=True)

        SplitsPlatoon = pd.read_html(SplitsPlatoonURL)[0].query('G != "G"')\
            .apply(partial(pd.to_numeric, errors='ignore'))\
            .reset_index(drop=True)

        if batting_or_pitching == "pitching":
            SplitsPitcher = pd.read_html(SplitsSeasonTotalsPitchersURL)[0].query('G != "G"')\
            .apply(partial(pd.to_numeric, errors='ignore'))\
            .reset_index(drop=True)

            SplitsPlatoonPitcher = pd.read_html(SplitsPlatoonPitchersURL)[0].query('G != "G"')\
            .apply(partial(pd.to_numeric, errors='ignore'))\
            .reset_index(drop=True)