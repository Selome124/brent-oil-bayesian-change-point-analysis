## Assumptions and Limitations

This analysis assumes that major geopolitical and economic events have a measurable temporal association with Brent oil price movements. The change point models detect statistical structural breaks in the price series but do not establish causal relationships.

Key assumptions include:
- Market prices reflect information efficiently within a short time window.
- Event dates are accurately labeled and represent the onset of market impact.
- External confounding variables (interest rates, FX, demand shocks) are not explicitly modeled.

Limitations:
- Change point detection identifies correlation in time, not causation.
- Some events overlap, making isolated impact attribution difficult.
- Non-trading days require nearest-price approximations.
- Volatility clustering may arise from multiple latent factors.

Future work would integrate macroeconomic indicators and multivariate Bayesian models to strengthen causal inference.

## Exploratory Data Analysis

Initial visualization of Brent oil prices reveals long-term upward trends punctuated by abrupt shocks and periods of extreme volatility. Log-return analysis shows volatility clustering, indicating heteroskedastic behavior typical of financial time series.

Stationarity analysis on log returns suggests suitability for change point detection, as structural breaks manifest more clearly in return distributions than raw prices.

These observations informed the modeling choice to analyze log returns and focus on detecting regime changes rather than short-term noise.
