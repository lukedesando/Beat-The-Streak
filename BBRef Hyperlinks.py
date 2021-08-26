from baseball_scraper import espn, playerid_lookup
from BackgroundFunctions import Find_Fangraph_ID, num_names,Get_BBRef_ID

#FIXME It's all here, just needs to be cleaned up into a function

PlayerName = "Fernando Tatis"
batting_or_pitching = "batting"
#TODO Need Player_Type to be automatically configured as p for pitcher or b for batter, otherwise it'll take forever
if batting_or_pitching == "pitching":
    b_or_p = "p"
    bat_or_pitch = "pitch"
else:
    b_or_p = "b"
    bat_or_pitch = "bat"

Year = 2021

#Referenced from Background Functions
BBRefID = Get_BBRef_ID(PlayerName)
BBRefLetter = BBRefID[0]

hyperlink_Main_Page = "\fhttps://www.baseball-reference.com/players/%s/%s.shtml" % (BBRefLetter,BBRefID)
print(hyperlink_Main_Page)

hyperlink_GameLogs = "\fhttps://www.baseball-reference.com/players/gl.fcgi?id=%s&t=%s&year=%d" % (BBRefID,b_or_p,Year)
print(hyperlink_GameLogs)

hyperlink_Splits = "\fhttps://www.baseball-reference.com/players/split.fcgi?id=%s&year=%d&t=%s" % (BBRefID,Year,b_or_p)
print(hyperlink_Splits)

hyperlink_AdvancedStats = "\fhttps://www.baseball-reference.com/players/%s/%s-%s.shtml" % (BBRefLetter,BBRefID,bat_or_pitch)
print (hyperlink_AdvancedStats)