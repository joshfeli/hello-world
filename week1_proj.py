import json
import pdb
import requests
from pprint import pprint

import pandas as pd
import pyyoutube
import sqlalchemy as db


# 3 steps:
# 1) Get data from API
# 2) Transform data from (nested) dict -> DataFrame
# 3) Create database and enter data into items
API_KEY = 'AIzaSyB0S1oSehFW5v6ICXJ2iaiUDpMhjCIPeeQ'
PLAYLIST_ID = 'PL9rbyFT14-WFy71Ed0Ihu4CbLczTftcC3'

# test ideas: different limits (including 0 and and over 111,
# the length of my Gospel playlist)
def get_playlist(playlist_id=PLAYLIST_ID, limit=None):
    api = pyyoutube.Api(api_key=API_KEY)

    res = api.get_playlist_items(playlist_id=playlist_id, count=limit)

    playlist_items = res.items
    gospel_playlist = [video.to_dict()['snippet']
                       for video in playlist_items]

    # pdb.set_trace()
    # pprint(gospel_playlist)

    return gospel_playlist

# different levels of nesting, empty dict, list of dicts?
def transform_data(data):
    df = pd.json_normalize(data)
    pdb.set_trace()
    # pprint(data)
    # pprint(df)
    return df

# different types of data frames? Empty dataframes?
def enter_data(df):
    engine = db.create_engine('sqlite:///youtube-data.db')
    # col_names = [name for name in df.columns] # column names are not showing up in the database
    df.to_sql('YouTube_videos', con=engine, if_exists='replace', index=False)
    query_result = engine.execute('SELECT * FROM YouTube_videos;').fetchall()
    print(pd.DataFrame(query_result))


gospel_playlist = get_playlist()
data_frame = transform_data(gospel_playlist)
enter_data(data_frame)