# Media Incrementality & Geo Lift Analytics Platform

## Overview

This project is a marketing measurement platform designed to estimate the incremental impact of media campaigns across geographic markets.

It uses a marketing measurement dataset from Meta Robyn and extends it with a geo-experiment framework to analyze whether campaign activity caused incremental revenue lift.

The platform answers the business question:

**Did the campaign actually generate incremental revenue, or would that revenue have happened anyway?**

---

## Business Problem

Marketing teams often observe revenue increases after campaign launches, but revenue growth alone does not prove that the campaign caused the increase.

This project creates treatment and control geographic markets to estimate the causal impact of a simulated media campaign.

The objective is to measure:

- Incremental Revenue

- Revenue Lift %

- Treatment vs Control Performance

- Geo-Level Campaign Impact

- Synthetic Counterfactual Performance

- Budget Optimization Opportunities

---

## Methodologies

### Geo Experiment Design

Treatment markets receive campaign exposure, while control markets do not.

### Difference-in-Differences

Estimates campaign impact by comparing revenue changes in treatment markets against revenue changes in control markets before and after campaign launch.

### Synthetic Control

Builds a weighted combination of untreated control markets to estimate what the treatment market would have looked like without the campaign.

---

## Current Results

### Difference-in-Differences

- Incremental Revenue Per Week: **$303,691**

- Revenue Lift: **15.21%**

- Total Incremental Revenue: **$31.58M**

### Synthetic Control

- Treatment Market: **California**

- Estimated Incremental Lift: **$329,252**

- Lift: **15.00%**

Both methods recover approximately 15% lift, validating the geo-lift measurement framework.

---

## Tech Stack

- Python

- Pandas

- NumPy

- Scikit-Learn

- Statsmodels

- Matplotlib

- Streamlit

- Plotly

---

## Project Structure

```text

Data/

src/

dashboard/

reports/

notebooks/

[README.md](http://README.md)

requirements.txt