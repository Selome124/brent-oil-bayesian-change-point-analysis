from src.data.preprocess import compute_log_returns
import pandas as pd

def test_log_returns():
    df = pd.DataFrame({"Price": [100, 105, 110]})
    result = compute_log_returns(df)
    assert "log_return" in result.columns
