from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

def load_raw_data(filename="data_cardiovascular_risk.csv"):
    path = DATA_DIR / filename
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Dataset not found at {path}. Please upload it to data/raw folder.") from e
