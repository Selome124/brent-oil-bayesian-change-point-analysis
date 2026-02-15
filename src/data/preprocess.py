import numpy as np
import pandas as pd

def compute_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["log_return"] = np.log(df["Price"]).diff()
    return df.dropna()
