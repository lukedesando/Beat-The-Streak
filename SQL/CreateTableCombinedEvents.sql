-- drop table PitcherVsBatterMatchups;


Create TABLE PitcherVsBatterMatchups(
    pitcher_name tinytext,
    pitcher int,
    batter int,
    batter_name tinytext,
    PA smallINT,
    AB smallINT,
    Hits smallINT,
    BA DOUBLE,
    balls_in_play smallint,
    estimated_bacon DOUBLE,
    estimated_minus_actual_bacon DOUBLE,
    bacon double,
    HR smallint
)
select
    pitcher,
    batter,
    player_name as batter_name,
    avg(estimated_ba_using_speedangle) as estimated_bacon,
    count(batter) as PA,
    SUM(babip_value)+count(CASE events when 'home_run' then 1 else null end) as Hits,
    Count(CASE `description` when 'hit_into_play' then 1 else null end) as balls_in_play,
    Count(CASE `events` when 'home_run' then 1 else null end) as HR
from
    EventsBatter
group by
    batter,
    pitcher;

Update PitcherVsBatterMatchups c
	Inner JOIN(
select batter, pitcher, count(batter) as AB from EventsBatter 
where `description` = 'hit_into_play' OR `description` = 'swinging_strike' OR `description` = 'swinging_strike_blocked' OR `description` = 'called_strike' or `description` = 'foul_tip'
group by batter, pitcher) b
	on c.batter = b.batter and c.pitcher = b.pitcher
Set c.AB = b.AB;

update PitcherVsBatterMatchups
set bacon = Hits/nullif(balls_in_play,0);

update PitcherVsBatterMatchups set BA = Hits/AB;

update PitcherVsBatterMatchups
set estimated_minus_actual_bacon = estimated_bacon-bacon;

ALTER TABLE `GameLogs`.`PitcherVsBatterMatchups`
CHANGE `pitcher` `pitcher` int(11) NULL DEFAULT NULL COMMENT '' AFTER `pitcher_name`,
CHANGE `batter` `batter` int(11) NULL DEFAULT NULL COMMENT '' AFTER `pitcher`,
CHANGE `batter_name` `batter_name` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '' AFTER `batter`,
CHANGE `PA` `PA` tinyint NULL DEFAULT NULL COMMENT '' AFTER `batter_name`,
CHANGE `AB` `AB` tinyint NULL DEFAULT NULL COMMENT '' AFTER `PA`,
CHANGE `Hits` `Hits` tinyint NULL DEFAULT NULL COMMENT '' AFTER `AB`,
CHANGE `HR` `HR` tinyint NULL DEFAULT NULL COMMENT '' AFTER `Hits`,
CHANGE `BA` `BA` double NULL DEFAULT NULL COMMENT '' AFTER `HR`,
CHANGE `balls_in_play` `balls_in_play` tinyint NULL DEFAULT NULL COMMENT '' AFTER `BA`,
CHANGE `bacon` `bacon` double NULL DEFAULT NULL COMMENT '' AFTER `balls_in_play`,
CHANGE `estimated_bacon` `estimated_bacon` double NULL DEFAULT NULL COMMENT '' AFTER `bacon`,
CHANGE `estimated_minus_actual_bacon` `estimated_minus_actual_bacon` double NULL DEFAULT NULL COMMENT '' AFTER `estimated_bacon`;

UPDATE PitcherVsBatterMatchups SET Hits=0 WHERE Hits is null;
UPDATE PitcherVsBatterMatchups SET AB=0 WHERE AB is null;
UPDATE PitcherVsBatterMatchups SET BA=0 WHERE BA is null;
UPDATE PitcherVsBatterMatchups SET HR=0 WHERE HR is null;


-- update
--     PitcherVsBatterMatchups C
--     left join MLBIDs M on
--     C.pitcher = M.PlayerID
-- set
--     C.pitcher_name = M.PlayerName
-- where C.pitcher_name is NULL;