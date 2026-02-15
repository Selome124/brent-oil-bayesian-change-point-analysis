import pandas as pd

def load_price_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    
    # 1. Clean column names (removes hidden spaces/newlines)
    df.columns = df.columns.str.strip()
    
    # 2. Find the date column regardless of capitalization (Date, date, DATE)
    date_col = next((c for c in df.columns if c.lower() == 'date'), None)
    
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])
        # Rename to a standard 'Date' for the rest of your app logic
        df = df.rename(columns={date_col: 'Date'})
        df = df.sort_values("Date")
    else:
        raise KeyError(f"Could not find a 'Date' column in {path}. Found: {list(df.columns)}")
        
    return df

def load_event_data(path: str) -> pd.DataFrame:
    events = pd.read_csv(path)
    
    # Clean column names
    events.columns = events.columns.str.strip()
    
    # Find the date column
    date_col = next((c for c in events.columns if c.lower() == 'date'), None)
    
    if date_col:
        events[date_col] = pd.to_datetime(events[date_col])
        events = events.rename(columns={date_col: 'Date'})
    else:
        # Fallback print to help you debug in the terminal if it still fails
        print(f"DEBUG: Columns found in events: {events.columns.tolist()}")
        raise KeyError(f"Could not find a 'Date' column in {path}")
        
    return events