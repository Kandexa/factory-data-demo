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



