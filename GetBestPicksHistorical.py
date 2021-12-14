import sys
from getpass import getpass
import mariadb
from mariadb import connect, Error

localhost = '192.168.1.152'
CurrentDB = "GameLogs"

select_pitcherID_query = 'select pitcher, pitcher_name, batter, batter_name, estimated_ba from CombinedEvents where PA >20 order by estimated_ba DESC;'


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
    for PitcherID, PitcherName, BatterID, BatterName, EstBA in cur:
        print(f"PitcherID: {PitcherID}, BatterID: {BatterID}, Estimated BA: {EstBA}")
except Error as e:
    print(e)
    sys.exit(1)