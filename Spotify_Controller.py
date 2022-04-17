import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

SPOTIPY_DEVICE_ID = 'b87867c30c93d315bd7a3a67efd57d7a8888506b' # change to rasperry pi device ID
SPOTIPY_CLIENT_ID = '2b690c77b1624824bb3209a3dc1f94f4'
SPOTIPY_CLIENT_SECRET = 'fc9b969b85cf4f2280bde177ca5c243'
scope = "user-read-playback-state, user-read-currently-playing"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                              redirect_uri='http://localhost:8080/', scope=scope))


def Play():
    sp.start_playback(device_id=SPOTIPY_DEVICE_ID, uris=['spotify:track:7lT1dCz96jANsLAAADlfIg', 'spotify:track'
                                                                                                                    ':1R28m5eWk1EV9FQ3puWrUp'])


sleep(1)


def Pause():
    sp.pause_playback(device_id=SPOTIPY_DEVICE_ID)
    sleep(1)


def Next():
    sp.next_track(device_id=SPOTIPY_DEVICE_ID)
    sleep(1)


def Previous():
    sp.previous_track(device_id=SPOTIPY_DEVICE_ID)
    sleep(1)

def Spotify_control(choice):
    while True:
        print("enter 1(Play), 2(Pause), 3(Next), 4(Previous)")
        choice = int(input("enter choice\n"))
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
