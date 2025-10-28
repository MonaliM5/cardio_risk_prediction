def create_features(df):
    """Creating additional features if required"""
    df = df.copy()
    # Example: converting age from days to years
    if 'age' in df.columns:
        df['age_years'] = (df['age'] / 365).round(0)
    return df
