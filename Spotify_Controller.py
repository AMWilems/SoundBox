import spotipy    # spotify API library
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

SPOTIPY_DEVICE_ID = 'b87867c30c93d315bd7a3a67efd57d7a8888506b' # credential variables used to connect to account 
SPOTIPY_CLIENT_ID = '5a4b4ea5a97d43449c2e40f5b84f3cef'
SPOTIPY_CLIENT_SECRET = '22dfa21c37844f4ba8b54f243e969a46'
scope = "user-read-playback-state, user-read-currently-playing" 

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                              redirect_uri='http://localhost:8080/', scope=scope)) # authentication variable used to control device
                                                                                    

def Play(): # Play Track function, includes Spotify URI for specific song for the parameter 
    sp.start_playback(device_id=SPOTIPY_DEVICE_ID, uris=['spotify:track:4cOdK2wGLETKBW3PvgPWqT', 'spotify:track:5EbNBRk0GQyoWeJ8AMlact'])


sleep(1)


def Pause(): # Pause Track Function
    sp.pause_playback(device_id=SPOTIPY_DEVICE_ID)
    sleep(1)


def Next(): # Next Track Function
    sp.next_track(device_id=SPOTIPY_DEVICE_ID)
    sleep(1)


def Previous(): # Previous Track Function
    sp.previous_track(device_id=SPOTIPY_DEVICE_ID)
    sleep(1)

def Spotify_control(choice): # function used to manage function controls based on user input 
    while True:
        # used to connect to the device 
        sp.transfer_playback(device_id=SPOTIPY_DEVICE_ID, force_play=False)

        if choice == 1:
            Play()
        elif choice == 2:
            Pause()
        elif choice == 3:
            Next()
        elif choice == 4:
            Previous()
        elif choice == 5:
            break
        else:
            print("Error: Please pick a valid option.")
