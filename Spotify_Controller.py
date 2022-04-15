import spotipy
from spotipy.oauth2 import SpotifyOAuth

DEVICE_ID = "YOUR_DEVICE_ID"
CLIENT_ID = "94b3a66356c1485490ca7d0768206d4994b3a66356c1485490ca7d0768206d49"
CLIENT_SECRET = "5ed3d79e1e2c403985f0e148a188db7a"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8080/",
                                               scope="user-read-playback-state,user-modify-playback-state"))

def Pause():
  print("in")
  try:
    sp.pause_playback(device_id=DEVICE_ID) #pause
    
  finally:
      print("done")
  
def Previous():
  print("prev")
  sp.previous_track(device_id=DEVICE_ID) #last track
  print("done")

def Play(spot_ID = ""):
  print ("Play")
  full_path = "spotify:track:" + spot_ID
  sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
  sp.start_playback(device_id=DEVICE_ID, uris = full_path)
  print("done")
  
def Next():
  sp.next_track(device_id=DEVICE_ID) #next track
  print("done")
  
# sp.search() if start playback works, continue with finding information
# information

