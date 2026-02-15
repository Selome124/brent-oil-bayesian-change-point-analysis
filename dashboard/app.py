import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import ruptures as rpt  # pip install ruptures

# ---------------------------------------------------
# 1. Path Setup (project root)
# ---------------------------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ---------------------------------------------------
# 2. Local Imports
# ---------------------------------------------------
from src.data.load_data import load_price_data, load_event_data
from src.data.preprocess import compute_log_returns
from src.volatility import rolling_volatility

# ---------------------------------------------------
# 3. Helper Function: Change Point Detection
# ---------------------------------------------------
def detect_change_points(df: pd.DataFrame, n_bkps: int = 5):
    """
    Detect structural shifts in price using binary segmentation.
    Returns list of dates where change points occur.
    """
    signal = df["Price"].values
    algo = rpt.Binseg(model="l2").fit(signal)
    result = algo.predict(n_bkps=n_bkps)
    return df.iloc[result[:-1]]["Date"].tolist()

# ---------------------------------------------------
# 4. Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Brent Oil Analysis Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# 5. Data Loading
# ---------------------------------------------------
prices = load_price_data("data/raw/BrentOilPrices.csv")
events = load_event_data("data/events/oil_market_events.csv")

# ---- Normalize event schema (IMPORTANT FIX)
events.columns = events.columns.str.lower()
events["date"] = pd.to_datetime(events["date"])

# ---------------------------------------------------
# 6. Preprocessing
# ---------------------------------------------------
returns_df = compute_log_returns(prices)
returns_df["volatility"] = rolling_volatility(returns_df)

# ---------------------------------------------------
# 7. Sidebar Controls
# ---------------------------------------------------
st.sidebar.header("📊 Dashboard Controls")

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(prices["Date"].min().date(), prices["Date"].max().date()),
    min_value=prices["Date"].min().date(),
    max_value=prices["Date"].max().date()
)

num_bkps = st.sidebar.slider(
    "AI Change Points to Detect",
    min_value=1,
    max_value=15,
    value=5
)

# ---------------------------------------------------
# 8. Data Filtering
# ---------------------------------------------------
mask = (
    (prices["Date"].dt.date >= date_range[0]) &
    (prices["Date"].dt.date <= date_range[1])
)

filtered_prices = prices.loc[mask].copy()

filtered_events = events[
    events["date"].dt.date.between(date_range[0], date_range[1])
].copy()

# ---------------------------------------------------
# 9. Dashboard Header
# ---------------------------------------------------
st.title("🛢️ Brent Oil Price & Volatility Analysis")
st.markdown(
    """
    This dashboard compares **human-labeled geopolitical events**
    with **AI-detected structural change points** in Brent oil prices.
    """
)

# ---------------------------------------------------
# 10. KPI Metrics
# ---------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "Latest Price",
    f"${filtered_prices['Price'].iloc[-1]:.2f}"
)

col2.metric(
    "Average Volatility",
    f"{returns_df['volatility'].mean():.4f}"
)

col3.metric(
    "Events in Range",
    len(filtered_events)
)

# ---------------------------------------------------
# 11. Price Chart with Overlays
# ---------------------------------------------------
st.subheader("📈 Price Trends & Structural Shifts")

cp_dates = detect_change_points(filtered_prices, n_bkps=num_bkps)

fig = px.line(
    filtered_prices,
    x="Date",
    y="Price",
    title="Brent Crude Oil Price ($/barrel)"
)

# ---- Human-Labeled Events (RED)
for _, row in filtered_events.iterrows():

    # Safe price lookup (handles non-trading days)
    nearest_price = filtered_prices.iloc[
        (filtered_prices["Date"] - row["date"]).abs().argsort()[:1]
    ]["Price"].values[0]

    fig.add_vline(
        x=row["date"],
        line_dash="dash",
        line_color="red",
        opacity=0.5
    )

    fig.add_trace(
        go.Scatter(
            x=[row["date"]],
            y=[nearest_price],
            mode="markers",
            marker=dict(color="red", size=10, symbol="triangle-up"),
            name="Geopolitical Event",
            hovertemplate=(
                f"<b>Event:</b> {row['event']}<br>"
                f"<b>Category:</b> {row['category']}<br>"
                f"<b>Date:</b> {row['date'].date()}<extra></extra>"
            )
        )
    )

# ---- AI Change Points (GREEN)
for cp in cp_dates:
    fig.add_vline(
        x=cp,
        line_width=2,
        line_dash="dot",
        line_color="green",
        opacity=0.8
    )

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# 12. Volatility Section
# ---------------------------------------------------
st.subheader("📉 Market Volatility (30-Day Rolling)")

vol_df = returns_df[
    returns_df["Date"].dt.date.isin(filtered_prices["Date"].dt.date)
]

fig_vol = px.area(
    vol_df,
    x="Date",
    y="volatility",
    title="Rolling Volatility",
    labels={"volatility": "Volatility"}
)

st.plotly_chart(fig_vol, use_container_width=True)

# ---------------------------------------------------
# 13. Data Tables
# ---------------------------------------------------
col_a, col_b = st.columns(2)

with col_a:
    st.write("### 📝 Event Log")
    st.dataframe(filtered_events, use_container_width=True)

with col_b:
    st.write("### 🤖 AI-Detected Change Points")
    st.dataframe(
        pd.DataFrame({"Change Point Date": cp_dates}),
        use_container_width=True
    )
