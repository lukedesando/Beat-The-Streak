from mariadb import connect, Error
import sys
from getpass import getpass
import mariadb
#FIXME: Need to import from Beat-The-Streak repo
from BackgroundFunctions import Get_Player_Name

localhost = '192.168.1.152'

select_pitcherID_query = "SELECT pitcher, pitcher_name FROM CombinedEvents WHERE pitcher_name IS Null"
update_pitcherName_query = "UPDATE CombinedEvents"
CurrentDB = "GameLogs"


try:
    conn = mariadb.connect(
        host='192.168.1.152',
        user='Luke',
        # user=input("Enter username: "),
        database = CurrentDB
        # password=getpass("Enter password: "),
    )
    cur = conn.cursor()
    cur.execute(select_pitcherID_query)
    for PitcherID, PitcherName in cur:

        print(f"PitcherID: {PitcherID}, PitcherName: {PitcherName}")
except Error as e:
    print(e)
    sys.exit(1)