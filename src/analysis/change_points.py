import pandas as pd
import ruptures as rpt

def detect_change_points(df: pd.DataFrame, n_bkps: int = 5):
    """
    Detects changes in the price mean/variance.
    n_bkps: Number of change points to look for.
    """
    # Convert prices to a numpy array
    signal = df['Price'].values
    
    # Use the Pelt algorithm or Binary Segmentation
    algo = rpt.Binseg(model="l2").fit(signal)
    result = algo.predict(n_bkps=n_bkps)
    
    # Map indices back to dates
    change_dates = df.iloc[result[:-1]]['Date'].tolist()
    return change_dates