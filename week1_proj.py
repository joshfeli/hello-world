import json
import requests

import pyyoutube


API_KEY = 'AIzaSyB0S1oSehFW5v6ICXJ2iaiUDpMhjCIPeeQ'
api = pyyoutube.Api(api_key=API_KEY)

playlist_item_by_id = api.get_playlist_item_by_id(playlist_item_id="UExPVTJYTFl4bXNJS3BhVjhoMEFHRTA1c28wZkF3d2ZUdy41NkI0NEY2RDEwNTU3Q0M2")
playlist_item_by_playlist = api.get_playlist_items(playlist_id="PLOU2XLYxmsIKpaV8h0AGE05so0fAwwfTw", count=2)

print(playlist_item_by_id)
print(playlist_item_by_playlist)
