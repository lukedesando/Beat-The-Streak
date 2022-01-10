from contextlib import nullcontext
from mariadb import connect, Error, Warning
import sys
from getpass import getpass
import mariadb
from numpy import empty
from BackgroundFunctions import Get_MLB_ID

localhost = '192.168.1.152'

select_Player_query = "SELECT MLBID, Player FROM HardHitLeaders"
update_MLBID_query = '''UPDATE HardHitLeaders SET MLBID = ? WHERE Player = ?'''
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
    cur2 = conn.cursor()
    cur.execute(select_Player_query)
    emptynames = cur.fetchall()
    for MLBID, PlayerName in emptynames:
        try:
            lastName, firstName = PlayerName.split(', ')
            FullName = firstName + ' ' + lastName
            MLBID = Get_MLB_ID(FullName)
            cur2.execute (update_MLBID_query,(MLBID, PlayerName))
            conn.commit()
            print(f"MLBID: {MLBID}, PlayerName: {PlayerName}")
        except (Error, Warning) as e:
            print(f"MLBID: {MLBID}, PlayerName: {PlayerName}")
            print("Didn't Work")
except Error as e:
    print(e)
    sys.exit(1)