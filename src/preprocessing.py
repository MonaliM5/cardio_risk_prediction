import pandas as pd

def clean_data(df):
    """Performing basic cleaning of dataset"""
    df = df.copy()
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # filling missing values if any
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df
