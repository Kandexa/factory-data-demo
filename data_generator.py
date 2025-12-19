import random
from datetime import datetime, timedelta
import psycopg2

DB = dict(
    host="localhost",
    dbname="factory365_demo",
    user="mceli",
    password="celil123",
)

MACHINES = ["A", "B", "C"]

def main():
    conn = psycopg2.connect(**DB)
    conn.autocommit = True
    now = datetime.now()
    start = now - timedelta(minutes=30)

    with conn.cursor() as cur:
        t = start
        while t <= now:
            for m in MACHINES:
                state = random.choices(["run", "stop", "fault"], weights=[0.80, 0.15, 0.05], k=1)[0]

                cur.execute(
                    "INSERT INTO machine_events (ts, machine_id, state) VALUES (%s, %s, %s)",
                    (t, m, state)
                )

                good = random.randint(3, 10) if state == "run" else 0
                scrap = random.randint(0, 2) if state == "run" and random.random() < 0.1 else 0
                cur.execute(
                    "INSERT INTO production (ts, machine_id, good_count, scrap_count) VALUES (%s, %s, %s, %s)",
                    (t, m, good, scrap)
                )

                kw = round(random.uniform(2.0, 5.0), 2) if state == "run" else round(random.uniform(0.2, 1.0), 2)
                cur.execute(
                    "INSERT INTO energy (ts, machine_id, kw) VALUES (%s, %s, %s)",
                    (t, m, kw)
                )

            t += timedelta(seconds=10)

    conn.close()
    print("✅ Demo data inserted (last 30 minutes).")

if __name__ == "__main__":
    main()
