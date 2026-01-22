import pandas as pd
import random
from faker import Faker

fake = Faker()

NUM_ROWS = 5000

content_titles = [
    "Bol Radha Bol",
    "Desi Londe",
    "Ghatak",
    "Nirahua Hindustani",
    "Kesariya Balam",
    "Padharo Mhare Des"
]

dialects = ["Haryanvi", "Rajasthani", "Bhojpuri"]
device_types = ["Mobile", "SmartTV", "Web"]
regions = ["Haryana", "Rajasthan", "Bihar", "UP", "Delhi"]

rows = []

for view_id in range(1, NUM_ROWS + 1):
    row = {
        "view_id": view_id,
        "user_id": random.randint(1, 500),
        "content_title": random.choice(content_titles),
        "dialect": random.choice(dialects),
        "watch_duration_sec": random.randint(0, 3600),
        "device_type": random.choice(device_types),
        "timestamp": fake.date_time_between(start_date="-14d", end_date="now"),
        "region": random.choice(regions)
    }
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("stage_viewership.csv", index=False)

print("✅ stage_viewership.csv generated with 5000 rows (schema compliant)")
