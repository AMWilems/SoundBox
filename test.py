import spotipy
from spotipy.oauth2 import SpotifyOAuth
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

DEVICE_ID = "YOUR_DEVICE_ID"
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8080/",
                                               scope="user-read-playback-state,user-modify-playback-state"))

# sp.pause_playback(device_id=DEVICE_ID) pause
# sp.previous_track(device_id=DEVICE_ID) last track
sp.start_playback(device_id=DEVICE_ID, uris="spotify:track:6mrRJpEOqNEKygu4fesH1e")

# sp.next_track(device_id=DEVICE_ID) next track
# sp.search() if start playback works, continue with finding information
# information

