import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID = "YOUR_DEVICE_ID"
CLIENT_ID = "94b3a66356c1485490ca7d0768206d4994b3a66356c1485490ca7d0768206d49"
CLIENT_SECRET = "5ed3d79e1e2c403985f0e148a188db7a"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8080",
                              scope="user-read-playback-state, user-modify-playback-state"))


sp.start_playback(device_id=DEVICE_ID, uris='spotify:track:5uvosCdMlFdTXhoazkTI5R')
sleep(2)
