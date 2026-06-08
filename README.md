# Media Incrementality & Geo Lift Analytics Platform

## Overview

This project is a marketing measurement platform designed to estimate the true incremental impact of media campaigns across geographic markets.

The platform applies causal inference and marketing measurement methodologies to answer a critical business question:

**Did the campaign actually generate incremental conversions, or would those conversions have happened anyway?**

---

## Business Problem

Marketing teams invest millions of dollars in advertising campaigns but often struggle to determine whether observed conversion increases were actually caused by marketing efforts.

This project simulates a geo-based media experiment where selected treatment markets receive additional advertising spend while control markets do not.

The objective is to estimate:

- Incremental Conversions
- Conversion Lift
- Incremental CPA
- Incremental Revenue
- Geographic Performance
- Budget Reallocation Opportunities

---

## Methodologies

### Geo Experiments

Compare treatment and control markets before and after campaign launch.

### Difference-in-Differences (DiD)

Estimate causal impact by comparing conversion changes between treatment and control groups.

### Synthetic Control

Construct a counterfactual estimate of campaign performance in the absence of marketing intervention.

### Marketing Measurement

Evaluate conversion lift, media efficiency, and budget optimization opportunities.

---

## Planned Features

- KPI Engine
- Geo Lift Analysis
- Difference-in-Differences Modeling
- Synthetic Control Analysis
- Conversion Lift Measurement
- Budget Recommendation Engine
- Streamlit Dashboard
- Executive Summary Generation

---

## Tech Stack

- Python
- Pandas
- NumPy
- Statsmodels
- Scikit-Learn
- Streamlit
- Plotly

---

## Project Status

In Progress