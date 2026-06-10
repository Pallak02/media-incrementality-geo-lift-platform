import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Geo Lift Platform",
    layout="wide"
)

# ---------- CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: #0b0f19;
        color: #f9fafb;
    }

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    .hero-card {
        padding: 2.4rem;
        border-radius: 28px;
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 45%, #4c1d95 100%);
        box-shadow: 0 18px 50px rgba(0,0,0,0.35);
        margin-bottom: 1.8rem;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .hero-title {
        font-size: 2.7rem;
        font-weight: 900;
        color: white;
        margin-bottom: 0.7rem;
        line-height: 1.1;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #d1d5db;
        max-width: 950px;
        line-height: 1.7;
    }

    .badge-row {
        margin-top: 1.4rem;
    }

    .badge {
        display: inline-block;
        padding: 0.45rem 0.85rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.10);
        color: #e5e7eb;
        font-size: 0.82rem;
        font-weight: 700;
        margin-right: 0.5rem;
        border: 1px solid rgba(255,255,255,0.12);
    }

    .kpi-card {
        background: #ffffff;
        padding: 1.6rem;
        border-radius: 22px;
        box-shadow: 0 18px 35px rgba(0,0,0,0.28);
        border: 1px solid #e5e7eb;
        min-height: 130px;
    }

    .kpi-label {
        color: #6b7280;
        font-size: 0.76rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 800;
        margin-bottom: 0.7rem;
    }

    .kpi-value {
        color: #0f172a;
        font-size: 2rem;
        font-weight: 900;
        margin-bottom: 0.35rem;
    }

    .kpi-note {
        color: #64748b;
        font-size: 0.85rem;
    }

    .section-heading {
        font-size: 1.5rem;
        font-weight: 900;
        color: #f9fafb;
        margin-top: 1rem;
        margin-bottom: 0.3rem;
    }

    .section-copy {
        color: #9ca3af;
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }

    .insight-panel {
        background: linear-gradient(135deg, #eef2ff 0%, #f8fafc 100%);
        color: #111827;
        padding: 1.4rem 1.6rem;
        border-radius: 20px;
        border-left: 7px solid #6366f1;
        box-shadow: 0 18px 35px rgba(0,0,0,0.22);
        line-height: 1.65;
        margin-top: 1rem;
    }

    .chart-panel {
        background: #ffffff;
        padding: 1.4rem;
        border-radius: 24px;
        box-shadow: 0 18px 35px rgba(0,0,0,0.28);
        border: 1px solid #e5e7eb;
        margin-top: 1rem;
    }

    .mini-panel {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 18px;
        padding: 1rem;
        color: #d1d5db;
        margin-bottom: 1rem;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #111827;
        border-radius: 999px;
        color: #d1d5db;
        padding: 0.55rem 1rem;
        border: 1px solid #1f2937;
    }

    .stTabs [aria-selected="true"] {
        background: #6366f1 !important;
        color: white !important;
    }

    h1, h2, h3, h4 {
        color: #f9fafb;
    }

    .stDataFrame {
        background: white;
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Data ----------
df = pd.read_csv("Data/marketing_geo_experiment.csv")
df["DATE"] = pd.to_datetime(df["DATE"])

treatment_states = ["California", "Texas", "Florida"]
control_states = ["Arizona", "Nevada", "Colorado"]

campaign_start = df[df["campaign_active"] == True]["DATE"].min()

# ---------- Sidebar ----------
st.sidebar.markdown("## Geo Lift Studio")
st.sidebar.caption("Marketing measurement controls")

selected_state = st.sidebar.selectbox(
    "Select treatment market",
    treatment_states
)

show_data = st.sidebar.checkbox("Show dataset preview", value=False)

st.sidebar.markdown("---")
st.sidebar.markdown("### Experiment Design")
st.sidebar.write("**Treatment:** California, Texas, Florida")
st.sidebar.write("**Control:** Arizona, Nevada, Colorado")
st.sidebar.write(f"**Launch:** {campaign_start.strftime('%Y-%m-%d')}")

st.sidebar.markdown("---")
st.sidebar.markdown("### Methods")
st.sidebar.write("Difference-in-Differences")
st.sidebar.write("Synthetic Control")
st.sidebar.write("Geo Lift Measurement")

# ---------- Calculations ----------
before = df[df["campaign_active"] == False]
after = df[df["campaign_active"] == True]

t_before = before[before["group"] == "Treatment"]["revenue"].mean()
t_after = after[after["group"] == "Treatment"]["revenue"].mean()

c_before = before[before["group"] == "Control"]["revenue"].mean()
c_after = after[after["group"] == "Control"]["revenue"].mean()

did = (t_after - t_before) - (c_after - c_before)
lift_pct = (did / t_before) * 100
weeks_after = len(after["DATE"].unique())
total_incremental = did * weeks_after

# ---------- Hero ----------
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Media Incrementality & Geo Lift Analytics Platform</div>
        <div class="hero-subtitle">
            Executive-ready marketing measurement dashboard for estimating whether campaign spend
            actually caused incremental revenue. Built with geo experiments, Difference-in-Differences,
            and Synthetic Control counterfactual modeling.
        </div>
        <div class="badge-row">
            <span class="badge">Geo Experiments</span>
            <span class="badge">Causal Inference</span>
            <span class="badge">Marketing Measurement</span>
            <span class="badge">Synthetic Control</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- KPI Cards ----------
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Revenue Lift</div>
            <div class="kpi-value">{lift_pct:.2f}%</div>
            <div class="kpi-note">Estimated incremental lift</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Incremental Revenue</div>
            <div class="kpi-value">${total_incremental/1_000_000:.1f}M</div>
            <div class="kpi-note">Total post-campaign impact</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Revenue / Week</div>
            <div class="kpi-value">${did:,.0f}</div>
            <div class="kpi-note">Average weekly lift</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with k4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">Campaign Launch</div>
            <div class="kpi-value">{campaign_start.strftime('%Y-%m')}</div>
            <div class="kpi-note">Intervention start period</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Executive View",
        "DiD Analysis",
        "Synthetic Control",
        "Methodology"
    ]
)

# ---------- Executive ----------
with tab1:
    st.markdown('<div class="section-heading">Executive Summary</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Business-facing interpretation of campaign incrementality.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="insight-panel">
            <b>Campaign impact:</b> The campaign generated approximately
            <b>${total_incremental:,.0f}</b> in incremental revenue, representing a
            <b>{lift_pct:.2f}% revenue lift</b> across treatment markets.
            <br><br>
            <b>Business read:</b> Treatment markets outperformed control markets after launch,
            suggesting the media investment created measurable incremental revenue beyond
            baseline market movement.
            <br><br>
            <b>Decision implication:</b> The campaign shows positive lift and should be considered
            for scaled testing, deeper market-level analysis, and budget optimization.
        </div>
        """,
        unsafe_allow_html=True
    )

    if show_data:
        st.markdown('<div class="section-heading">Dataset Preview</div>', unsafe_allow_html=True)
        st.dataframe(df.head(20), use_container_width=True)

# ---------- DiD ----------
with tab2:
    st.markdown('<div class="section-heading">Difference-in-Differences Analysis</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Compares revenue movement in treatment and control markets before and after campaign launch.</div>',
        unsafe_allow_html=True
    )

    trend = (
        df.groupby(["DATE", "group"])["revenue"]
        .mean()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for group in trend["group"].unique():
        group_df = trend[trend["group"] == group]
        ax.plot(
            group_df["DATE"],
            group_df["revenue"],
            label=group,
            linewidth=3
        )

    ax.axvline(
        x=campaign_start,
        linestyle="--",
        linewidth=2,
        label="Campaign Start"
    )

    ax.set_title("Treatment vs Control Revenue Over Time", fontsize=15, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    ax.legend(frameon=True)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.markdown('<div class="chart-panel">', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="insight-panel">
            Difference-in-Differences estimated average weekly incremental revenue of
            <b>${did:,.0f}</b>, equivalent to a <b>{lift_pct:.2f}% lift</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- Synthetic Control ----------
with tab3:
    st.markdown(
        f'<div class="section-heading">Synthetic Control: {selected_state}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-copy">Builds a counterfactual version of the selected treatment market using untreated controls.</div>',
        unsafe_allow_html=True
    )

    pivot = df.pivot_table(
        index="DATE",
        columns="state",
        values="revenue",
        aggfunc="mean"
    ).reset_index()

    pre = pivot[pivot["DATE"] < campaign_start]
    post = pivot[pivot["DATE"] >= campaign_start]

    X_pre = pre[control_states]
    y_pre = pre[selected_state]

    model = LinearRegression(positive=True)
    model.fit(X_pre, y_pre)

    synthetic_col = f"synthetic_{selected_state.lower()}"
    pivot[synthetic_col] = model.predict(pivot[control_states])

    post_period = pivot[pivot["DATE"] >= campaign_start]

    actual_post = post_period[selected_state].mean()
    synthetic_post = post_period[synthetic_col].mean()

    synthetic_lift = actual_post - synthetic_post
    synthetic_lift_pct = (synthetic_lift / synthetic_post) * 100

    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Synthetic Lift</div>
                <div class="kpi-value">{synthetic_lift_pct:.2f}%</div>
                <div class="kpi-note">Selected market lift</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with s2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Lift / Week</div>
                <div class="kpi-value">${synthetic_lift:,.0f}</div>
                <div class="kpi-note">{selected_state} weekly impact</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with s3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Counterfactual</div>
                <div class="kpi-value">${synthetic_post:,.0f}</div>
                <div class="kpi-note">Expected revenue without campaign</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    weights_df = pd.DataFrame({
        "Control Market": control_states,
        "Weight": model.coef_
    })

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-copy">Control market weights used to construct the synthetic counterfactual.</div>', unsafe_allow_html=True)
    st.dataframe(weights_df, use_container_width=True)

    fig2, ax2 = plt.subplots(figsize=(12, 5))
    fig2.patch.set_facecolor("white")
    ax2.set_facecolor("white")

    ax2.plot(
        pivot["DATE"],
        pivot[selected_state],
        label=f"Actual {selected_state}",
        linewidth=3
    )

    ax2.plot(
        pivot["DATE"],
        pivot[synthetic_col],
        label=f"Synthetic {selected_state}",
        linewidth=3
    )

    ax2.axvline(
        x=campaign_start,
        linestyle="--",
        linewidth=2,
        label="Campaign Start"
    )

    ax2.set_title(f"Actual {selected_state} vs Synthetic {selected_state}", fontsize=15, fontweight="bold")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Revenue")
    ax2.legend(frameon=True)

    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.markdown('<div class="chart-panel">', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Methodology ----------
with tab4:
    st.markdown('<div class="section-heading">Methodology</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="mini-panel">
        <b>Difference-in-Differences</b><br>
        Compares treatment market revenue changes against control market revenue changes before
        and after the campaign. This helps remove background market movement.
        </div>

        <div class="mini-panel">
        <b>Synthetic Control</b><br>
        Creates a counterfactual version of a selected treatment market using untreated controls.
        The post-campaign gap between actual and synthetic revenue estimates incremental impact.
        </div>

        <div class="mini-panel">
        <b>Business Use Case</b><br>
        Helps marketing teams answer whether campaign spend actually caused incremental business outcomes,
        rather than simply moving alongside revenue growth.
        </div>
        """,
        unsafe_allow_html=True
    )