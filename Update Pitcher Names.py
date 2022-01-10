from mariadb import connect, Error, Warning
import sys
from getpass import getpass
import mariadb
#FIXME: Need to import from Beat-The-Streak repo
from BackgroundFunctions import Get_Player_Name, Get_Player_Name_Last_First, Chadwick_Get_Name_Last_First

localhost = '192.168.1.152'
CurrentTable = 'PitcherVsBatterMatchups'

select_pitcherID_query = "SELECT pitcher, pitcher_name FROM " + CurrentTable + " WHERE pitcher_name IS Null group by pitcher"
update_pitcherName_query = "UPDATE " + CurrentTable + " SET pitcher_name = ? WHERE pitcher = ?"
CurrentDB = "GameLogs"


try:
    conn = mariadb.connect(
        host='192.168.1.152',
        user='LukeLukeLukeLuke',
        # user=input("Enter username: "),
        database = CurrentDB
        # password=getpass("Enter password: "),
    )
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute(select_pitcherID_query)
    emptynames = cur.fetchall()
    for PitcherID, PitcherName in emptynames:
        try:
            PitcherName = Get_Player_Name_Last_First(PitcherID) # - faster, but incomplete for former players
            # PitcherName = Chadwick_Get_Name_Last_First(PitcherID)
            cur2.execute (update_pitcherName_query,(PitcherName, PitcherID))
            conn.commit()
            # cur2.execute (f'''UPDATE CombinedEvents SET pitcher_name = {PitcherName} WHERE pitcher = {PitcherID}''')
            print(f"PitcherID: {PitcherID}, PitcherName: {PitcherName}")
        except (Error, Warning) as e:
            print(f"PitcherID: {PitcherID}, PitcherName: {PitcherName}")
            print("Didn't Work")
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    cur3.execute(select_pitcherID_query)
    Oldemptynames = cur3.fetchall()
    for PitcherID, PitcherName in Oldemptynames:
        try:
            # PitcherName = Get_Player_Name_Last_First(PitcherID) # - faster, but incomplete for former players
            PitcherName = Chadwick_Get_Name_Last_First(PitcherID)
            cur4.execute (update_pitcherName_query,(PitcherName, PitcherID))
            conn.commit()
            # cur2.execute (f'''UPDATE CombinedEvents SET pitcher_name = {PitcherName} WHERE pitcher = {PitcherID}''')
            print(f"PitcherID: {PitcherID}, PitcherName: {PitcherName}")
        except (Error, Warning) as e:
            print(f"PitcherID: {PitcherID}, PitcherName: {PitcherName}")
            print("Didn't Work")
except Error as e:
    print(e)
    sys.exit(1)