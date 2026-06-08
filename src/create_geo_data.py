import pandas as pd

print("Loading dataset...")

df = pd.read_csv("Data/dt_simulated_weekly.csv")

states = [
    "California",
    "Texas",
    "Florida",
    "Arizona",
    "Nevada",
    "Colorado"
]

state_multiplier = {
    "California": 1.20,
    "Texas": 1.10,
    "Florida": 1.00,
    "Arizona": 0.95,
    "Nevada": 0.90,
    "Colorado": 1.05
}

geo_data = []

for state in states:
    temp = df.copy()

    temp["state"] = state
    temp["revenue"] = temp["revenue"] * state_multiplier[state]

    if state in ["California", "Texas", "Florida"]:
        temp["group"] = "Treatment"
    else:
        temp["group"] = "Control"

    geo_data.append(temp)

geo_df = pd.concat(geo_data, ignore_index=True)

print("Rows after expansion:", geo_df.shape)

campaign_start = df["DATE"].iloc[104]

geo_df["campaign_active"] = geo_df["DATE"] >= campaign_start

mask = (
    (geo_df["group"] == "Treatment")
    &
    (geo_df["campaign_active"] == True)
)

geo_df.loc[mask, "revenue"] = geo_df.loc[mask, "revenue"] * 1.15

geo_df.to_csv("Data/marketing_geo_experiment.csv", index=False)

print("Dataset Created!")
print(geo_df.shape)