import pandas as pd

def rolling_volatility(df: pd.DataFrame, window: int = 30) -> pd.Series:
    return df["log_return"].rolling(window).std()
