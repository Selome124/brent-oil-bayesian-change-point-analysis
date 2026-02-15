from src.data.load_data import load_price_data

def test_price_data_load():
    df = load_price_data("data/raw/BrentOilPrices.csv")
    assert "Price" in df.columns
    assert len(df) > 1000
