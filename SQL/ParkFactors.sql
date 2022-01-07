alter table
    GameLogs.ParkFactors
add
    column venue_id int
after
    `Venue`;
    
update GameLogs.ParkFactors P
left join `KEYS - venues` K 
on P.Team = K.home_team_name
set P.venue_id = K.venue_id;

alter table
    GameLogs.ParkFactorsHandedness
add
    column venue_id int
after
    `Venue`;
    
update GameLogs.ParkFactorsHandedness P
left join `KEYS - venues` K 
on P.Team = K.home_team_name
set P.venue_id = K.venue_id;

-- Changes for ParkFactors Table

Update ParkFactors
Set venue_id = 4705
    where team = 'Braves' and game_year>2016;

Update ParkFactors
Set venue_id = 16
    where team = 'Braves' and game_year<2017;

Update ParkFactors
set venue_id = 15
where team = 'Diamondbacks';

Update ParkFactors
set venue_id = 5325
where team = 'Rangers' and game_year>2019;

Update ParkFactors
set venue_id = 13
where team = 'Rangers' and game_year<2020;

Update ParkFactors
set venue_id = 2756
where team = 'Blue Jays' and game_year=2020;

-- Changes for ParkFactors Handedness Table

Update ParkFactorsHandedness
Set venue_id = 4705
    where team = 'Braves' and game_year>2016;

Update ParkFactorsHandedness
Set venue_id = 16
    where team = 'Braves' and game_year<2017;

Update ParkFactorsHandedness
set venue_id = 15
where team = 'Diamondbacks';

Update ParkFactorsHandedness
set venue_id = 5325
where team = 'Rangers' and game_year>2019;

Update ParkFactorsHandedness
set venue_id = 13
where team = 'Rangers' and game_year<2020;

Update ParkFactorsHandedness
set venue_id = 2756
where team = 'Blue Jays' and game_year=2020;