from mariadb import connect, Error, Warning
import sys
from getpass import getpass
import mariadb
#FIXME: Need to import from Beat-The-Streak repo
from BackgroundFunctions import GetFangraphsTeamID, GetPyBaseballTeamID, GetVenueID

localhost = '192.168.1.152'
CurrentTable = 'EventsBatter'
select_query = "SELECT home_team, game_year FROM " + CurrentTable + " WHERE venue_id IS Null group by home_team"
update_query = "UPDATE " + CurrentTable + " SET venue_id = ? WHERE home_team = ?"
CurrentDB = "GameLogs"
TeamMapCSV = 'MLB Team Map.csv'

try:
    conn = mariadb.connect(
        host=localhost,
        user='Luke',
        # user=input("Enter username: "),
        database = CurrentDB
        # password=getpass("Enter password: "),
    )
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur.execute(select_query)
    emptynames = cur.fetchall()
    for TeamShortID, uselessID in emptynames:
        try:
            print(TeamShortID)
            VenueID = GetVenueID(GetFangraphsTeamID(TeamShortID))
            cur2.execute (update_query, (VenueID, TeamShortID))
            conn.commit()
            # cur2.execute (f'''UPDATE CombinedEvents SET pitcher_name = {PitcherName} WHERE pitcher = {PitcherID}''')
            print(f"VenueID: {VenueID}, TeamID: {TeamShortID}")
        except (Error, Warning) as e:
            print(f"VenueID: {VenueID}, TeamID: {TeamShortID}")
            print("Didn't Work")
except Error as e:
    print(e)
    sys.exit(1)