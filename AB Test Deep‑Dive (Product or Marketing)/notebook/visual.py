import matplotlib.pyplot as plt
import pandas as pd
# Conversion rates and confidence intervals
groups = ["A (Control)", "B (Variant)"]
rates = [519/5076, 622/4924]
ci_lower = [0.093911, 0.117041]   # from your results
ci_upper = [0.110581, 0.135599]

# Error bars = distance from rate to CI bound
error_lower = [max(r - l, 0) for r, l in zip(rates, ci_lower)]
error_upper = [max(u - r, 0) for r, u in zip(ci_upper, rates)]

plt.bar(groups, rates, yerr=[error_lower, error_upper], capsize=5, color=["skyblue", "lightgreen"])
plt.ylabel("Conversion Rate")
plt.title("A/B Test Conversion Rates with 95% CI")
plt.ylim(0, 0.15)
plt.show()



# daily_trend
data = {
    "test_group": [
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B",
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B",
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B",
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B",
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B",
        "A", "B", "A", "B", "A", "B", "A", "B", "A", "B",
        "A", "B", "A", "B"
    ],
    "test_date": [
        "2025-07-19", "2025-07-19", "2025-07-20", "2025-07-20", "2025-07-21", "2025-07-21",
        "2025-07-22", "2025-07-22", "2025-07-23", "2025-07-23", "2025-07-24", "2025-07-24",
        "2025-07-25", "2025-07-25", "2025-07-26", "2025-07-26", "2025-07-27", "2025-07-27",
        "2025-07-28", "2025-07-28", "2025-07-29", "2025-07-29", "2025-07-30", "2025-07-30",
        "2025-07-31", "2025-07-31", "2025-08-01", "2025-08-01", "2025-08-02", "2025-08-02",
        "2025-08-03", "2025-08-03", "2025-08-04", "2025-08-04", "2025-08-05", "2025-08-05",
        "2025-08-06", "2025-08-06", "2025-08-07", "2025-08-07", "2025-08-08", "2025-08-08",
        "2025-08-09", "2025-08-09", "2025-08-10", "2025-08-10", "2025-08-11", "2025-08-11",
        "2025-08-12", "2025-08-12", "2025-08-13", "2025-08-13", "2025-08-14", "2025-08-14",
        "2025-08-15", "2025-08-15", "2025-08-16", "2025-08-16", "2025-08-17", "2025-08-17",
        "2025-08-18", "2025-08-18", "2025-08-19", "2025-08-19"
    ],
    "conversion_rate": [
        0.0737, 0.1494, 0.1469, 0.0909, 0.1192, 0.1299, 0.125, 0.1626, 0.0928, 0.1369,
        0.0833, 0.1779, 0.0736, 0.1316, 0.0848, 0.1203, 0.0926, 0.1074, 0.1059, 0.0798,
        0.0904, 0.1325, 0.0753, 0.1047, 0.1, 0.1209, 0.0867, 0.1235, 0.1447, 0.1029,
        0.0843, 0.1132, 0.0791, 0.1553, 0.1067, 0.2013, 0.0979, 0.1456, 0.1375, 0.1206,
        0.1098, 0.1386, 0.1138, 0.0833, 0.1014, 0.1617, 0.1111, 0.0903, 0.0927, 0.1203,
        0.1069, 0.1143, 0.0893, 0.1575, 0.1636, 0.1524, 0.1059, 0.1032, 0.0647, 0.1086,
        0.1098, 0.0783, 0.0862, 0.1667
    ]
}
df = pd.DataFrame(data)

# Convert date column
df["test_date"] = pd.to_datetime(df["test_date"])

# Plot
plt.figure(figsize=(10,5))
for g in df["test_group"].unique():
    subset = df[df["test_group"] == g]
    plt.plot(subset["test_date"], subset["conversion_rate"], marker="o", label=f"Group {g}")

plt.xlabel("Date")
plt.ylabel("Conversion Rate")
plt.title("Daily Conversion Trends - A vs B")
plt.legend()
plt.show()
plt.savefig("daily_conversion_trends.png", dpi=300, bbox_inches='tight')