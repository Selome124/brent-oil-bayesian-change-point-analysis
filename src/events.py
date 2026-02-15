import pandas as pd

def match_events(change_point_date, events_df: pd.DataFrame, window_days: int = 30):
    window_start = change_point_date - pd.Timedelta(days=window_days)
    window_end = change_point_date + pd.Timedelta(days=window_days)

    return events_df[
        (events_df["Date"] >= window_start) &
        (events_df["Date"] <= window_end)
    ]
