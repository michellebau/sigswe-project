"""This file stores the data obtained from a specific artist"""
# import random
import requests
from auth import get_auth

def get_data(artist_id):
    """function that retrieces and stores the data"""
    access_token = get_auth()

    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }
    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_id)
    data = requests.get(URL + "?market=US", headers = headers)
    data = data.json()
    rand = 2
    song_name = data['tracks'][rand]['name']

    artist_names = ''
    for artist in data['tracks'][rand]['artists']:
        artist_names += artist['name'] + ', '

    artist_names = artist_names[:-2]

    album_cover = data['tracks'][rand]['album']['images'][0]['url']

    preview_url = data['tracks'][rand]['preview_url']

    spotify_url = data['tracks'][rand]['external_urls']['spotify']

    info = [song_name, artist_names, album_cover, preview_url, spotify_url]
    return info

if __name__ == '__main__':
    get_data()
