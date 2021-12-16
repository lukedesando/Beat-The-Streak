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