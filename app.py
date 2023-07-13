import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pp = pprint.PrettyPrinter(indent=2)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


PLAYLISTS_IDS = [
    "37i9dQZF1DX6cg4h2PoN9y",
    "0fZm7ygIaFLpTX7AEd38WT"
]

playlists_striped = []

for ID in PLAYLISTS_IDS:
    
    results = spotify.playlist_items(playlist_id=ID, limit=20)

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