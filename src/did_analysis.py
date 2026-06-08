print("SCRIPT STARTED")

import pandas as pd

print("PANDAS IMPORTED")

# Load dataset
df = pd.read_csv("Data/marketing_geo_experiment.csv")

# Before campaign
before = df[df["campaign_active"] == False]

# After campaign
after = df[df["campaign_active"] == True]

# Treatment
t_before = before[before["group"] == "Treatment"]["revenue"].mean()
t_after = after[after["group"] == "Treatment"]["revenue"].mean()

# Control
c_before = before[before["group"] == "Control"]["revenue"].mean()
c_after = after[after["group"] == "Control"]["revenue"].mean()

# Difference in Differences
did = (t_after - t_before) - (c_after - c_before)

# Lift %
lift_pct = (did / t_before) * 100

# Total Incremental Revenue
weeks_after = len(after["DATE"].unique())

total_incremental = did * weeks_after

print("\n===== DIFFERENCE-IN-DIFFERENCES =====")

print(f"Treatment Before : ${t_before:,.0f}")
print(f"Treatment After  : ${t_after:,.0f}")

print(f"Control Before   : ${c_before:,.0f}")
print(f"Control After    : ${c_after:,.0f}")

print("\n------------------------------------")

print(f"Incremental Revenue Per Week : ${did:,.0f}")

print(f"Revenue Lift %              : {lift_pct:.2f}%")

print(f"Total Incremental Revenue   : ${total_incremental:,.0f}")

print("\n===== EXECUTIVE SUMMARY =====")

print(
    f"The campaign generated approximately "
    f"${total_incremental:,.0f} in incremental revenue "
    f"representing a {lift_pct:.2f}% lift versus baseline performance."
)