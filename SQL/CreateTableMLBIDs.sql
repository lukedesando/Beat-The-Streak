Create TABLE MLBIDs(
    PlayerID INT,
    PlayerName text)
select batter as PlayerID,
player_name as PlayerName
from DatabaseBatterEvents
group by batter;

Insert into MLBIDs
select pitcher as PlayerID,
player_name as PlayerName
from DatabasePitcherEvents
group by pitcher;