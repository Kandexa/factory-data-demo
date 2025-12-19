## Why this exists
This mini-project demonstrates how factory telemetry can be stored and reported:
- time-stamped machine states (run/stop/fault)
- production counts (good/scrap)
- energy sampling (kW)
Then it generates basic operational reports using SQL.

## Quick demo (2 commands)
```bash
python data_generator.py
psql -U mceli -d factory365_demo -f daily_summary.sql > report_output.txt

\# Factory Data Demo (PostgreSQL + Python + SQL)



A small demo that simulates factory telemetry and generates basic reports using SQL.



\## What this demo does

\- Creates a simple schema:

&nbsp; - `machine\_events(ts, machine\_id, state)`

&nbsp; - `production(ts, machine\_id, good\_count, scrap\_count)`

&nbsp; - `energy(ts, machine\_id, kw)`

\- Generates demo data for the last 30 minutes (3 machines: A, B, C)

\- Produces a "Daily Summary" report:

&nbsp; - Stop events today

&nbsp; - Fault events in the last hour

&nbsp; - Production totals (good/scrap/total)



\## Prerequisites

\- Anaconda (recommended)

\- PostgreSQL installed in a conda env (this repo assumes a local postgres on `localhost:5432`)

\- A database named `factory365\_demo`

\- A user with access (in my setup: `mceli`)



\## Setup (Windows / Anaconda)

```bash

conda create -n factorydb python=3.10 -y

conda activate factorydb

conda install -c conda-forge postgresql -y

pip install -r requirements.txt

## Talking points (for interview)
- I designed a minimal PostgreSQL schema for factory telemetry.
- Machine states are stored as time-stamped events (run / stop / fault).
- Production data separates good parts and scrap parts.
- Energy is sampled independently as kW values.
- I used Python to generate realistic demo data.
- I wrote SQL queries to produce daily operational summaries:
  - stop counts
  - fault counts
  - production totals
  - estimated downtime
  - average energy usage

## Future work
- Calculate basic OEE metrics (Availability / Quality).
- Add real-time ingestion instead of generated data.
- Visualize reports using a simple dashboard.
- Parameterize machines and sampling intervals.

