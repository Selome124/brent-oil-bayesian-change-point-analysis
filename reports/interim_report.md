# Task 1: Data Analysis Workflow for Brent Oil Price Change Point Analysis

## 1. Data Loading and Cleaning
- Load raw Brent oil price data (daily prices from 1987-05-20 to 2022-09-30).
- Convert date strings to datetime objects.
- Handle missing values or anomalies (if any).
- Calculate log returns for stationarity and volatility analysis.

## 2. Exploratory Data Analysis (EDA)
- Visualize price trends over time.
- Analyze volatility patterns, including clustering.
- Perform stationarity tests (e.g., ADF test).
- Identify possible periods of structural breaks.

## 3. Event Data Compilation
- Research major geopolitical, OPEC, and economic events impacting oil prices.
- Compile a CSV dataset with event names and approximate start dates.

## 4. Change Point Modeling
- Build Bayesian change point detection model using PyMC.
- Identify structural breaks and estimate change point dates.
- Quantify changes in mean price levels before and after change points.

## 5. Event Association and Impact Quantification
- Compare detected change points with event dates.
- Formulate hypotheses linking events to structural breaks.
- Quantify price impacts attributable to key events.

## 6. Reporting and Communication
- Create a report summarizing findings and assumptions.
- Develop an interactive dashboard for stakeholders.
- Use clear visualizations and concise explanations.

## Assumptions and Limitations
- Assumes detected change points correspond to external events (correlation, not causation).
- Data quality depends on accuracy of historical price and event records.
- Model assumes a single or few change points; complex market dynamics might be missed.
- Bayesian model convergence and parameter identifiability affect result confidence.

## Communication Channels
- Written reports (Markdown, PDFs)
- Interactive dashboards (React + Flask)
- Presentations to stakeholders (slide decks)

### Assumptions
- Brent oil price data is accurate and complete for the analysis period.
- Key geopolitical events chosen are representative and their dates approximate the start of impact.
- The Bayesian change point model captures mean shifts but may miss more complex volatility changes.

### Limitations
- Change point detection identifies statistical breaks but cannot prove causality.
- Market factors outside the selected events may influence prices.
- Data irregularities or missing data points can affect model accuracy.
- Only daily prices are used; intra-day or hourly data could provide finer insight.

# Task 1: Laying the Foundation for Analysis  
## Brent Oil Price Change Point Analysis

---

## 1. Introduction

The global oil market is highly sensitive to geopolitical events, economic shocks, and policy decisions, particularly those involving major oil-producing nations and OPEC. Brent crude oil prices often experience sudden structural changes following such events.  

This project aims to analyze how major political, economic, and geopolitical events have influenced Brent oil prices over time using **Bayesian Change Point Analysis**. The objective is to identify statistically significant structural breaks in the price series and associate them with real-world events.

---

## 2. Data Analysis Workflow

The analysis follows a structured data science workflow consisting of the following steps:

### 2.1 Data Loading and Preparation
- Load historical daily Brent oil price data.
- Convert date columns to datetime format.
- Inspect and handle missing or anomalous values.
- Compute log returns to stabilize variance and support stationarity.

### 2.2 Exploratory Data Analysis (EDA)
- Visualize raw price trends over time.
- Analyze volatility patterns and identify periods of instability.
- Examine price distributions and summary statistics.

### 2.3 Time Series Property Analysis
- Analyze long-term and short-term trends.
- Perform stationarity testing using statistical methods.
- Examine volatility clustering commonly observed in financial time series.

### 2.4 Event Data Compilation
- Research and collect major geopolitical, economic, and OPEC-related events.
- Create a structured dataset containing event names, dates, and categories.
- Use this dataset to contextualize detected change points.

### 2.5 Change Point Modeling
- Apply Bayesian Change Point Detection using PyMC.
- Identify dates where statistical properties of the series change.
- Estimate mean price levels before and after detected change points.

### 2.6 Insight Generation and Communication
- Associate detected change points with real-world events.
- Quantify the impact of major events on oil prices.
- Communicate insights through reports and an interactive dashboard.

---

## 3. Event Dataset Description

A structured dataset containing major oil market events has been compiled.  
Each entry includes:
- Event start date (approximate)
- Event description
- Event category (Geopolitical, Economic, OPEC, Conflict)

The dataset includes events such as:
- OPEC production decisions
- Global financial crises
- Wars and regional conflicts
- Trade disputes and sanctions
- COVID-19 related economic disruptions

This dataset enables comparison between statistical change points and real-world occurrences.

---

## 4. Time Series Properties of Brent Oil Prices

### 4.1 Trend Analysis
Brent oil prices exhibit long-term trends influenced by supply-demand dynamics, technological advancements, and geopolitical stability. Periods of sustained growth and decline are visible across decades.

### 4.2 Stationarity
The raw price series is **non-stationary**, as its mean and variance change over time. This is common in financial price series.  
To address this, **log returns** are considered, which are more likely to be stationary and suitable for statistical modeling.

### 4.3 Volatility Patterns
The series displays **volatility clustering**, where periods of high volatility are followed by more high volatility. This behavior motivates the use of probabilistic and Bayesian modeling approaches rather than deterministic models.

These properties justify the use of change point models that can adapt to structural shifts in the data.

---

## 5. Change Point Models: Conceptual Overview

Change point models are used to detect moments in time where the statistical properties of a time series change significantly.

In the context of Brent oil prices, change point models help:
- Identify sudden shifts in average price levels
- Detect market regime changes
- Link price instability to major external events

A Bayesian change point model estimates:
- The most probable date(s) of structural change
- Parameter values before and after each change
- Uncertainty around these estimates

---

## 6. Expected Outputs of Change Point Analysis

The expected outputs include:
- Posterior distribution of the change point date(s)
- Estimated mean price levels before and after each change
- Probability-based confidence in detected structural breaks

### Limitations of the Output
- The model detects **statistical correlation**, not causation.
- Multiple overlapping events may influence a single change point.
- Some price changes may be driven by unobserved variables.

---

## 7. Assumptions and Limitations

### Assumptions
- Brent oil price data accurately reflects market conditions.
- Event dates approximate the start of their market impact.
- Structural breaks are reflected primarily as changes in mean price.

### Limitations
- Change point detection does not prove causal relationships.
- Market reactions may lag behind event dates.
- The model simplifies complex market dynamics.
- External factors not included in the event dataset may affect prices.

A key distinction is made between **temporal correlation** and **causal impact**. While events and change points may align in time, this does not guarantee that one caused the other.

---

## 8. Communication Channels

Results will be communicated through:
- Written analytical reports (Markdown / PDF)
- Interactive dashboards (Flask + React)
- Data visualizations for policymakers and investors

These formats ensure accessibility for both technical and non-technical stakeholders.

---

## 9. Conclusion

This foundational analysis establishes a clear workflow, data understanding, and modeling rationale for studying Brent oil price dynamics. Task 1 sets the groundwork for Bayesian change point modeling and deeper insight generation in subsequent tasks.
