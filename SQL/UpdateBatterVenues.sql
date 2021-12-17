alter table
    ParkFactors
add
    column venue_id int
after
    `Team`;
    
update ParkFactors P
left join `KEYS - venues` K 
on P.Team = K.home_team_name
set P.venue_id = K.venue_id;

-- Other Teams Found in UpdateEventsVenue.py

Update DatabaseBatterEvents
Set venue_id = 4705
    where home_team = 'ATL' and game_year>2016;

Update DatabaseBatterEvents
Set venue_id = 16
    where home_team = 'ATL' and game_year<2017;

Update DatabaseBatterEvents
set venue_id = 15
where home_team = 'ARI';

Update DatabaseBatterEvents
set venue_id = 5325
where home_team = 'TEX' and game_year>2019;

Update DatabaseBatterEvents
set venue_id = 2756
where home_team = 'TOR' and game_year=2020;