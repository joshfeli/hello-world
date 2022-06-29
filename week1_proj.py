import json
import pdb
import requests
from pprint import pprint

import pyyoutube
import sqlalchemy as db
import pandas as pd


API_KEY = 'AIzaSyB0S1oSehFW5v6ICXJ2iaiUDpMhjCIPeeQ'
api = pyyoutube.Api(api_key=API_KEY)

# by_id = api.get_playlist_item_by_id(
#     playlist_item_id="UExPVTJYTFl4bXNJS3BhVjhoMEFHRTA1c28" \
#                    + "wZkF3d2ZUdy41NkI0NEY2RDEwNTU3Q0M2",
#     return_json=True
# )
by_playlist = api.get_playlist_items(
    playlist_id="PLOU2XLYxmsIKpa"
                + "V8h0AGE05so0fAwwfTw",
    count=2,
    return_json=True
)
items = by_playlist['items']

# video ids, video_published_at, title, description, channel_title,
videos = [{} for i in range(len(items))]
for i in range(len(items)):
    details = items[i]['contentDetails']
    videos[i]['video_id'] = details['videoId']
    videos[i]['video_published_at'] = details['videoPublishedAt']
    videos[i]['title'] = items[i]['snippet']['title']
    videos[i]['description'] = items[i]['snippet']['description']
    videos[i]['channel_title'] = items[i]['snippet']['channelTitle']


df = pd.json_normalize(videos)

engine = db.create_engine('sqlite:///youtube-data.db')
df.to_sql('YouTube_videos', con=engine, if_exists='replace', index=False)

query_result = engine.execute('SELECT * FROM YouTube_videos;').fetchall()
print(pd.DataFrame(query_result))
