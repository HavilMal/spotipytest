import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pp = pprint.PrettyPrinter(indent=2, compact=True)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


PLAYLISTS_IDS = [
    "37i9dQZF1DWZeKCadgRdKQ"
]

playlists_striped = []

for ID in PLAYLISTS_IDS:
    
    results =spotify.playlist_items(playlist_id="37i9dQZF1DWZeKCadgRdKQ", limit=10)

    tracks = results['items']

    playlist = []

    for track in tracks:
        for artist in track['track']["artists"]:
            output = artist["name"] + " "

        output += "- " + track['track']["name"]

        playlist.append(output)

    playlists_striped.append(playlist)

# pp.pprint(playlists_striped)


pp.pprint(set(playlists_striped[0]).intersection(*playlists_striped))