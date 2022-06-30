import os
import unittest
from week1_proj import (get_playlist,
                        transform_data,
                        enter_data
                       )

class test_week1_proj(unittest.TestCase):
  def setUp(self):
    os.environ['API_KEY'] = 'AIzaSyB0S1oSehFW5v6ICXJ2iaiUDpMhjCIPeeQ'
    os.environ['PLAYLIST_ID'] = 'PL9rbyFT14-WFy71Ed0Ihu4CbLczTftcC3'

  def test_get_playlist(self):
    pass
  
  def test_transform_data(self):
    pass

  def test_enter_data(self):
    pass
