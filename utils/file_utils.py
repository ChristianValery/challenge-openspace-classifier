import pandas as pd

def collugues_excel(filename):
    df = pd.read_excel(filename)
    print(df)
    print(df.columns)
    return df["Name "].tolist()

