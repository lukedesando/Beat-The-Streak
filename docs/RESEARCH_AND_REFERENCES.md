# Research, Data Sources, and Upstream References

Beat the Streak combined several public baseball-data sources and also grew alongside exploratory forks of other open-source baseball projects. This document separates **direct dependencies/data sources** from **historical research references** so the provenance of the project is clear.

## Direct dependencies and data sources

### MLB Stats API / `MLB-StatsAPI`

The project imports the Python `statsapi` package directly for player lookup, player statistics, schedules, team rosters, and lower-level Stats API requests.

The package comes from Todd Roberts' **MLB-StatsAPI** project:

- upstream: https://github.com/toddrob99/MLB-StatsAPI
- package: https://pypi.org/project/MLB-StatsAPI/

A personal fork (`lukedesando/MLB-StatsAPI`) was kept during the original research period. The fork is reference material, not an authorship claim; the upstream project is the dependency that should be cited and used going forward.

### pybaseball / Statcast

`StatcastScrape.py` wraps `pybaseball.statcast_batter` and `pybaseball.statcast_pitcher` to retrieve pitch- and event-level Statcast data for the matchup pipeline.

- upstream: https://github.com/jldbc/pybaseball

### Chadwick Bureau Register

`BackgroundFunctions.py` uses the Chadwick Bureau player register to reconcile identifiers across providers such as MLBAM, Baseball Reference, Retrosheet, and FanGraphs.

The current repository contains an old ~59 MB CSV snapshot. Rehabilitation should replace that committed snapshot with a documented fetch/cache step from the maintained register.

- upstream: https://github.com/chadwickbureau/register

### ESPN probable starters

The daily workflow uses probable starting-pitcher information from ESPN. `myespn.py` contains the historical scraper used to turn the schedule page into a structured DataFrame.

The scraper should be provenance-reviewed and retested before being described as a supported current interface; HTML structure and acceptable-use constraints may have changed since the original project was built.

### Baseball Reference / Sports Reference

Several historical gamelog/split workflows use Baseball Reference or Sports Reference pages as analytical inputs. Those adapters should be revalidated before the project is made runnable again.

## Historical research forks

The following repositories were forked during the original baseball-analysis period. They are useful as evidence of what approaches were being evaluated, but they are **not incorporated wholesale into Beat the Streak and are not presented as original work**.

### `MLBDailyLineups`

Forked from `mattgorb/MLBDailyLineups` while exploring lineup/probable-player data sources. Beat the Streak's surviving daily workflow instead uses ESPN probable starters and MLB roster lookup, so this fork should be treated as historical source research rather than a current dependency.

- upstream: https://github.com/mattgorb/MLBDailyLineups

### `draftfast`

Forked from Ben Brostoff's DraftFast project, an optimization framework for constructing constrained DFS lineups. It is relevant background for thinking about player selection, ranking, constraints, and optimization, but the current Beat the Streak code does not directly depend on DraftFast.

- upstream: https://github.com/BenBrostoff/draftfast

### `Machine-Learning-Predict-MLB-Games`

Forked from EugenioGrant's project while researching predictive approaches to MLB game outcomes. The upstream project documents a random-forest approach built from historical game data. Beat the Streak's surviving code is focused on player/matchup data acquisition and transformation rather than reproducing that model.

- upstream: https://github.com/EugenioGrant/Machine-Learning-Predict-MLB-Games

### `monte-carlo-mlb`

Forked from Snoozle Software's Monte Carlo MLB Simulator while researching simulation-based prediction. The simulator is useful conceptual background, but the surviving Beat the Streak Python pipeline does not directly integrate its Java simulation code.

- upstream: https://github.com/snoozle-software/monte-carlo-mlb

## Earlier companion repositories

Two small original repositories also came from the same experimentation period:

- `MLBStatsHarvest` — exploratory player/stat retrieval and machine-learning scratch work.
- `BaseballSQLBackup` — SQL schema/setup experiments and backup-style database scripts.

Those repositories are being treated as historical material rather than separate portfolio projects. Any useful schema or acquisition lessons should be documented here or incorporated into the modernized Beat the Streak design instead of requiring visitors to navigate several unfinished repositories.

## Provenance rule for rehabilitation

When modernizing this project:

1. preserve upstream attribution for code or techniques derived from external projects;
2. prefer maintained upstream packages over old personal forks;
3. do not copy fork contents into this repository merely to consolidate them;
4. fold **lessons, architecture choices, and links** into documentation, and copy code only when its license and provenance are explicitly reviewed;
5. keep original Beat the Streak implementation work distinguishable from third-party data clients and scrapers.
