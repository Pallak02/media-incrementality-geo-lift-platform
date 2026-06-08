import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Data/marketing_geo_experiment.csv")

# Aggregate revenue by date and group
trend = (
    df.groupby(["DATE", "group"])["revenue"]
    .mean()
    .reset_index()
)

# Split groups
treatment = trend[trend["group"] == "Treatment"]
control = trend[trend["group"] == "Control"]

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    treatment["DATE"],
    treatment["revenue"],
    label="Treatment"
)

plt.plot(
    control["DATE"],
    control["revenue"],
    label="Control"
)

plt.xticks(rotation=45)

plt.title("Treatment vs Control Revenue Over Time")

plt.xlabel("Date")

plt.ylabel("Revenue")

plt.legend()

plt.tight_layout()

plt.savefig("reports/revenue_trend.png")

plt.show()