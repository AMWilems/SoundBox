import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

SPOTIPY_DEVICE_ID = '4ad2f55a4236cd5f7fc8a75f6bade1b337ae32a3' # change to rasperry pi device ID
SPOTIPY_CLIENT_ID = '0b53ed2e631f47ddb7ef45582f666b71'
SPOTIPY_CLIENT_SECRET = '47b8d86158f64d8b9cb70360d42bef71'
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
