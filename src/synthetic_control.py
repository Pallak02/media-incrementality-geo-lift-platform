import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
print("SCRIPT STARTED")
# Load geo experiment data
df = pd.read_csv("Data/marketing_geo_experiment.csv")

# Choose one treatment market
treatment_state = "California"

# Control markets
control_states = ["Arizona", "Nevada", "Colorado"]

# Create pivot table: rows = date, columns = state, values = revenue
pivot = df.pivot_table(
    index="DATE",
    columns="state",
    values="revenue",
    aggfunc="mean"
).reset_index()

# Get campaign start date
campaign_start = df[df["campaign_active"] == True]["DATE"].min()

# Split pre and post campaign periods
pre = pivot[pivot["DATE"] < campaign_start]
post = pivot[pivot["DATE"] >= campaign_start]

# X = control states, y = treatment state
X_pre = pre[control_states]
y_pre = pre[treatment_state]

# Train model to learn Synthetic California from controls
model = LinearRegression(positive=True)
model.fit(X_pre, y_pre)

# Predict synthetic California for all dates
pivot["synthetic_california"] = model.predict(pivot[control_states])

# Calculate post-campaign lift
post_period = pivot[pivot["DATE"] >= campaign_start]

actual_post = post_period[treatment_state].mean()
synthetic_post = post_period["synthetic_california"].mean()

incremental_lift = actual_post - synthetic_post
lift_pct = (incremental_lift / synthetic_post) * 100

print("\n===== SYNTHETIC CONTROL ANALYSIS =====")
print(f"Treatment Market: {treatment_state}")
print(f"Campaign Start Date: {campaign_start}")
print("--------------------------------------")
print("Control Market Weights:")
for state, weight in zip(control_states, model.coef_):
    print(f"{state}: {weight:.3f}")

print("--------------------------------------")
print(f"Actual Post-Campaign Revenue    : ${actual_post:,.0f}")
print(f"Synthetic Post-Campaign Revenue : ${synthetic_post:,.0f}")
print(f"Estimated Incremental Lift      : ${incremental_lift:,.0f}")
print(f"Lift %                          : {lift_pct:.2f}%")

# Plot
plt.figure(figsize=(12, 6))
plt.plot(pivot["DATE"], pivot[treatment_state], label="Actual California")
plt.plot(pivot["DATE"], pivot["synthetic_california"], label="Synthetic California")

plt.axvline(
    x=campaign_start,
    linestyle="--",
    label="Campaign Start"
)

plt.title("Actual vs Synthetic California Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("reports/synthetic_control_california.png", dpi=300, bbox_inches="tight")
plt.close()

print("Chart saved to reports/synthetic_control_california.png")