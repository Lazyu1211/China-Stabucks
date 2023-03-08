import pandas as pd

PATH = "/Users/junyuwu/China Starbucks /components/starbucks.csv"
df = pd.read_csv(PATH)
df["closeTime"].fillna("23:00:00", inplace=True)
df["openTime"].fillna("07:30:00", inplace=True)

def get_data():
    df['hasArtwork'] = df['hasArtwork'].apply(lambda x:10000 if x=="True" else 1)
    return df

def get_city():
    bycity = df["city"].value_counts()[:10].to_frame()
    bycity = bycity.rename(columns={"city": "门店数量"})
    bycity.index.name = "城市"
    return bycity

def get_opentime():
    byopen = df.groupby("openTime")["city"].value_counts().to_frame()
    listopen =sorted(list(set(byopen.index.get_level_values('openTime').tolist())))
    return listopen


def get_opentime_num():
    byopen = df["openTime"].value_counts().to_frame()
    return byopen

def get_closetime():
    byclose = df.groupby("closeTime")["city"].value_counts().to_frame()
    listclose =sorted(list(set(byclose.index.get_level_values('closeTime').tolist())))
    return listclose

def get_closetime_num():
    byclose = df["closeTime"].value_counts().to_frame()
    return byclose
