Create TABLE CombinedEvents(
    pitcher_name tinytext,
    pitcher int,
    batter int,
    batter_name tinytext,
    PA smallINT,
    AB smallINT,
    Hits smallINT,
    actual_ba DOUBLE,
    estimated_ba DOUBLE,
    estimated_minus_actual_ba DOUBLE
)
select
    pitcher,
    batter,
    player_name as batter_name,
    avg(estimated_ba_using_speedangle) as estimated_ba,
    count(batter) as PA,
    SUM(babip_value)+count(CASE events when 'home_run' then 1 else null end) as Hits,
from
    DatabaseBatterEvents
group by
    batter,
    pitcher;

Update CombinedEvents c
	Inner JOIN(
select batter, pitcher, count(batter) as AB from DatabaseBatterEvents 
where description = 'hit_into_play' OR description = 'swinging_strike' OR description = 'swinging_strike_blocked' OR description = 'called_strike' or description = 'foul_tip'
group by batter, pitcher) b
	on c.batter = b.batter and c.pitcher = b.pitcher
Set c.AB = b.AB;

update CombinedEvents set actual_ba = Hits/AB;

update CombinedEvents
set estimated_minus_actual_ba = estimated_ba-actual_ba;

ALTER TABLE `GameLogs`.`CombinedEvents`
CHANGE `pitcher` `pitcher` int(11) NULL DEFAULT NULL COMMENT '' AFTER `pitcher_name`,
CHANGE `batter` `batter` int(11) NULL DEFAULT NULL COMMENT '' AFTER `pitcher`,
CHANGE `batter_name` `batter_name` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '' AFTER `batter`,
CHANGE `PA` `PA` tinyint NULL DEFAULT NULL COMMENT '' AFTER `batter_name`,
CHANGE `AB` `AB` tinyint NULL DEFAULT NULL COMMENT '' AFTER `PA`,
CHANGE `Hits` `Hits` tinyint NULL DEFAULT NULL COMMENT '' AFTER `AB`,
CHANGE `actual_ba` `actual_ba` double NULL DEFAULT NULL COMMENT '' AFTER `Hits`,
CHANGE `estimated_ba` `estimated_ba` double NULL DEFAULT NULL COMMENT '' AFTER `actual_ba`,
CHANGE `estimated_minus_actual_ba` `estimated_minus_actual_ba` double NULL DEFAULT NULL COMMENT '' AFTER `estimated_ba`;

update
    CombinedEvents C
    left join MLBIDs M on
    C.pitcher = M.PlayerID
set
    C.pitcher_name = M.PlayerName
where C.pitcher_name is NULL;