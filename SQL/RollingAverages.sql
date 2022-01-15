-- alter table GamelogsBatter
-- add column H1G int, add column AB1G int,
-- add column H2G int, add column AB2G int,
-- add column H3G int, add column AB3G int,
-- add column H4G int, add column AB4G int,
-- add column H5G int, add column AB5G int,
-- add column H7G int, add column AB7G int,
-- add column H15G int, add column AB15G int,
-- add column H30G int, add column AB30G int;

drop table if exists GamelogsBatterCalc;

create table GamelogsBatterCalc select GamelogPk,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 1 preceding AND 1 preceding) AS H1G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 1 preceding AND 1 preceding) AS AB1G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 2 preceding AND 1 preceding) AS H2G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 2 preceding AND 1 preceding) AS AB2G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 3 preceding AND 1 preceding) AS H3G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 3 preceding AND 1 preceding) AS AB3G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 4 preceding AND 1 preceding) AS H4G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 4 preceding AND 1 preceding) AS AB4G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 5 preceding AND 1 preceding) AS H5G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 5 preceding AND 1 preceding) AS AB5G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 7 preceding AND 1 preceding) AS H7G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 7 preceding AND 1 preceding) AS AB7G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 15 preceding AND 1 preceding) AS H15G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 15 preceding AND 1 preceding) AS AB15G,

SUM(H) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 30 preceding AND 1 preceding) AS H30G,
SUM(AB) over (partition by PlayerName, GameYear
ORDER BY game_date
ROWS BETWEEN 30 preceding AND 1 preceding) AS AB30G

from GamelogsBatter;

UPDATE GamelogsBatter G
INNER JOIN GamelogsBatterCalc T ON G.GamelogPk = T.GamelogPk
SET 
G.AB1G = T.AB1G, G.H1G = T.H1G,
G.AB2G = T.AB2G, G.H2G = T.H2G,
G.AB3G = T.AB3G, G.H3G = T.H3G,
G.AB4G = T.AB4G, G.H4G = T.H4G,
G.AB5G = T.AB5G, G.H5G = T.H5G,
G.AB7G = T.AB7G, G.H7G = T.H7G,
G.AB15G = T.AB15G, G.H15G = T.H15G,
G.AB30G = T.AB30G, G.H30G = T.H30G;

drop table GamelogsBatterCalc;


-- -- alter table GamelogsBatterCalc add column
-- H1G int, AB1G int,
-- H2G int, AB2G int,
-- H3G int, AB3G int,
-- H4G int, AB4G int,
-- H5G int, AB5G int,
-- H7G int, AB7G int,
-- H15G int, AB15G int,
-- H30G int, AB30G int;

-- alter table GamelogsBatter
-- add column RollingBA15G double;

-- update GamelogsBatter 
-- set RollingBA15G =
-- sum(H) over (partition by GameYear, MLBID
-- order by game_date rows between 15 preceding and 1 PRECEDING)
-- /
-- sum(AB) over (partition by GameYear, MLBID
-- order by game_date rows between 15 preceding and 1 PRECEDING);