import pandas as pd

def transform_data(data):
    try:
        df = pd.json_normalize(data)
        df = df.fillna("")
        return df.to_dict(orient='records')
    except Exception:
        return data
    