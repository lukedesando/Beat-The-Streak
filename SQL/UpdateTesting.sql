SELECT pitcher, pitcher_name FROM CombinedEvents WHERE pitcher_name IS Null;

select
    pitcher,
    pitcher_name,
    batter,
    batter_name,
    estimated_ba,
    PA
from
    CombinedEvents
where
    PA > 15
order by
    estimated_ba DESC;
