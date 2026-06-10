# 📈 AI Marketing Measurement Platform

### Estimating Incremental Revenue Using Geo Experiments, Difference-in-Differences, and Synthetic Control

[Live Demo](https://marketing-incrementality-platform.streamlit.app/) | [GitHub Repository](https://github.com/Pallak02/media-incrementality-geo-lift-platform)

---

## Overview

Marketing teams invest millions of dollars in advertising campaigns but often struggle to answer a critical question:

> Did the campaign actually generate incremental revenue, or would those sales have happened anyway?

This project is an AI-powered marketing measurement platform designed to estimate the true causal impact of advertising campaigns using geo experiments and modern causal inference techniques.

The platform combines:

- Geo Experiment Design
- Difference-in-Differences (DiD)
- Synthetic Control Modeling
- Executive Insight Generation
- Budget Optimization Recommendations

The goal is to help marketing decision-makers move beyond attribution and measure true business impact.

---

## Business Problem

Traditional marketing dashboards report performance metrics such as:

- Revenue
- Clicks
- Conversions
- ROAS

However, these metrics do not necessarily measure causality.

A campaign may coincide with increased revenue without actually causing it.

To solve this problem, this project simulates a geo-based marketing experiment where selected markets receive additional advertising spend while control markets do not.

The platform estimates:

✅ Incremental Revenue

✅ Revenue Lift

✅ Counterfactual Performance

✅ Budget Allocation Recommendations

---

## Methodology

### 1. Geo Experiment Design

Markets are divided into:

| Treatment Markets | Control Markets |
|------------------|----------------|
| California | Arizona |
| Texas | Nevada |
| Florida | Colorado |

Treatment markets receive the campaign intervention while control markets serve as the baseline.

---

### 2. Difference-in-Differences (DiD)

Difference-in-Differences estimates causal impact by comparing:

```text
(Treatment After - Treatment Before)
-
(Control After - Control Before)
```

This removes underlying market trends and isolates campaign impact.

#### Results

- Revenue Lift: **15.21%**
- Incremental Revenue: **$31.6M**
- Weekly Incremental Revenue: **$303K**

---

### 3. Synthetic Control

Synthetic Control constructs a counterfactual version of a treatment market using weighted combinations of untreated markets.

This answers:

> What would California's revenue have looked like if the campaign had never run?

The gap between actual and synthetic performance represents incremental impact.

#### Results

- Synthetic Control Lift: **15.0%**
- Incremental Revenue: **$329K per week**

---

## Dashboard Features

### Executive Summary

Automatically translates statistical results into business recommendations.

### AI Executive Insights

Generates:

- Campaign verdict
- Key findings
- Revenue lift interpretation
- Strategic recommendations

### Difference-in-Differences Analysis

Visualizes treatment and control market performance before and after campaign launch.

### Synthetic Control Analysis

Compares actual market performance against a generated counterfactual baseline.

### Budget Optimizer

Recommends future budget allocation across markets based on measured incremental lift.

---

## Dashboard Screenshots

### Executive View

![Executive View](assets/executive_view.png)

---

### Difference-in-Differences Analysis

![DiD Analysis](assets/did_analysis.png)

---

### Synthetic Control Analysis

![Synthetic Control](assets/synthetic_control.png)

---

## Tech Stack

### Analytics

- Python
- Pandas
- NumPy
- Scikit-Learn

### Causal Inference

- Difference-in-Differences
- Synthetic Control

### Visualization

- Streamlit
- Matplotlib

### Product Layer

- Executive Insight Generation
- Budget Recommendation Engine

---

## Results

| Metric | Value |
|----------|----------|
| Revenue Lift | 15.21% |
| Incremental Revenue | $31.6M |
| Weekly Incremental Revenue | $303K |
| Synthetic Control Lift | 15.0% |

---

## Key Learnings

Through this project I learned how to:

- Design geo-based marketing experiments
- Estimate causal impact using Difference-in-Differences
- Build Synthetic Control counterfactual models
- Translate statistical findings into business recommendations
- Build and deploy analytics applications using Streamlit
- Connect marketing measurement with executive decision-making

---

## Future Improvements

- Integration with Google Ads API
- Integration with Meta Ads API
- Marketing Mix Modeling (MMM)
- Uplift Modeling
- LLM-powered insight generation using OpenAI
- Automated budget reallocation recommendations
- Multi-touch attribution comparison

---

## Author

**Palak Wadhwa**

M.S. Data Science, University of Maryland

Interested in:
- Marketing Analytics
- Marketing Science
- Growth Analytics
- Product Analytics
- Causal Inference
- AI Applications in Marketing
