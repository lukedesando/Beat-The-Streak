# Beat the Streak — MLB Matchup Analytics

A historical baseball analytics project built to support daily **Beat the Streak** decisions by combining probable starters, active rosters, player identifiers, Statcast events, gamelogs, and matchup history into reusable Python workflows.

> **Project status:** originally developed in 2021–2022 and now being rehabilitated as a documented portfolio project. The existing analytics code is preserved as historical work; dependencies and upstream data interfaces have not yet been fully modernized for 2026.

## What the Project Does

The project was designed around a daily research loop:

1. identify the day's probable starting pitchers;
2. resolve each opponent to an MLB roster;
3. normalize player identities across MLB, Baseball Reference, FanGraphs, Chadwick, and Statcast-oriented identifiers;
4. collect batter and pitcher statistics, gamelogs, and pitch-level events;
5. build batter-vs-pitcher and batter-vs-team matchup datasets;
6. export research-ready CSVs for comparison and historical analysis.

`Daily Play.py` is the clearest example of that workflow: it gets probable starters, expands the opposing roster, filters to hitters, and produces matchup/gamelog outputs for each relevant batter.

## Architecture

```text
ESPN probable starters
        |
        v
MLB team + active roster lookup
        |
        v
Player identity normalization
(MLBAM / BBRef / FanGraphs / Chadwick)
        |
        +------------------------+
        |                        |
        v                        v
Statcast pitch/event data     Player gamelogs + splits
        |                        |
        +-----------+------------+
                    |
                    v
         Batter/pitcher matchup frames
                    |
                    v
           CSV research datasets
```

### Key modules

| Module | Role |
| --- | --- |
| `Daily Play.py` | Daily orchestration around probable starters and opponent rosters. |
| `BackgroundFunctions.py` | Cross-provider player/team ID normalization and common MLB lookups. |
| `StatcastScrape.py` | Wrapper around `pybaseball` Statcast batter/pitcher retrieval. |
| `Matchups.py` | Batter-vs-pitcher and batter-vs-team matchup extraction. |
| `GenerateGamelogs.py` | Historical player gamelog collection. |
| `GenerateSplits.py` | Split-stat collection and shaping. |
| `GenerateDatabaseTables.py` | Batch generation of batter/pitcher Statcast, event, and gamelog datasets. |
| `PlayerPrintouts.py` | Player/roster stat summaries and probable-starter research helpers. |
| `myespn.py` | ESPN probable-starter scraping used by the daily workflow. |

## Engineering Problems Explored

This project is useful portfolio evidence less because of a single predictive model and more because of the data-integration problems it tackles:

- **Identity reconciliation:** the same player can have different IDs and naming conventions across MLB, Baseball Reference, FanGraphs, Chadwick, and other sources.
- **Messy-name handling:** suffixes, compound surnames, duplicate names, and provider-specific naming differences require normalization and explicit exceptions.
- **Cross-source joins:** roster, probable-starter, Statcast, gamelog, and split data need to resolve to the same players and teams before matchup analysis is meaningful.
- **Batch data generation:** the project includes workflows that iterate across MLB rosters and produce separate hitter/pitcher Statcast, event, and gamelog datasets.
- **Daily research automation:** the intended end state was to turn a repetitive manual baseball-research process into a repeatable pipeline.

## Data Sources and Prior Research

The code uses or was informed by several public baseball-data projects and data sources. Those dependencies and historical research references are documented separately so that upstream work is credited clearly and not confused with original code in this repository.

See **[Research, Data Sources, and Upstream References](docs/RESEARCH_AND_REFERENCES.md)**.

## Current Limitations

This is a historical codebase, not a claim that the 2021 runtime still works unchanged today.

Known rehabilitation work includes:

- establish a reproducible modern Python environment and dependency lock;
- verify every external data source against its current API/site contract;
- replace the committed ~59 MB Chadwick player-register snapshot with a fetch/cache workflow;
- remove stale imports and consolidate experimental/deprecated modules;
- add automated tests around identity reconciliation and matchup transforms;
- add CI for a clean-checkout smoke test;
- separate reusable library code from one-off scripts and generated CSV outputs;
- add representative sample output or screenshots without publishing third-party datasets unnecessarily;
- review provenance/licensing before adding a repository-wide software license.

## Rehabilitation Plan

The goal is to preserve the interesting engineering while making the project reproducible and understandable:

1. **Documentation baseline** — explain the pipeline, data sources, and historical research accurately.
2. **Repository hygiene** — move generated/large data out of source control and make inputs reproducible.
3. **Environment recovery** — identify compatible package versions and create a clean setup path.
4. **Testable core** — isolate ID normalization and matchup transformations behind fixtures/tests.
5. **Modernized acquisition** — update or replace stale data-source adapters without changing the analytical intent.
6. **Portfolio evidence** — publish small synthetic/sample outputs that demonstrate the pipeline without bundling large external datasets.

## Why Keep It Public?

Beat the Streak represents an earlier stage of my work focused on Python automation, data collection, cross-source normalization, and turning a manual analytical workflow into a repeatable system. The code shows its age, but the underlying integration problems are the same class of problems that appear in production data and automation work today.

More projects and current work: **https://desando.org**
