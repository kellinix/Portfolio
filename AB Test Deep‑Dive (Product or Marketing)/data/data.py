import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Parameters
n_users = 10000
countries = ["US", "UK", "CA", "DE", "FR"]
devices = ["desktop", "mobile", "tablet"]

# Simulate data
np.random.seed(42)

user_id = np.arange(1, n_users+1)
group = np.random.choice(["A", "B"], size=n_users, p=[0.5, 0.5])

# Conversion probabilities
conversion_probs = {"A": 0.10, "B": 0.12}
converted = [np.random.binomial(1, conversion_probs[g]) for g in group]

country = np.random.choice(countries, size=n_users)
device = np.random.choice(devices, size=n_users)

# Random timestamps in last 30 days
start_date = datetime.now() - timedelta(days=30)
timestamp = [start_date + timedelta(days=random.randint(0, 30),
                                    hours=random.randint(0, 23),
                                    minutes=random.randint(0, 59)) for _ in range(n_users)]

# Build dataframe
df = pd.DataFrame({
    "user_id": user_id,
    "group": group,
    "converted": converted,
    "country": country,
    "device": device,
    "timestamp": timestamp
})

# Save to CSV
df.to_csv("data/ab_test.csv", index=False)
print("✅ A/B test dataset saved to data/ab_test.csv")
