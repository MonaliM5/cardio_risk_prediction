import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(_file_).resolve().parents[1] / "models" / "best_model.joblib"

def predict_from_csv(csv_path):
    model = joblib.load(MODEL_PATH)
    df = pd.read_csv(csv_path)
    preds = model.predict(df)
    df['prediction'] = preds
    df.to_csv("predictions.csv", index=False)
    print("✅ Predictions saved to predictions.csv")

if _name_ == "_main_":
    import sys
    predict_from_csv(sys.argv[1])
