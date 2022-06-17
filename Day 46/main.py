from http import client
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
billboard = response.text
soup = BeautifulSoup(billboard, 'html.parser')

songs_name = soup.select(selector="li h3", class_="c-title")
songs_list = []
 
for song in songs_name:
    text = song.getText().strip()
    songs_list.append(text)
 
songs_list = songs_list[:100]

print(songs_list)


username = 'username'
scope = "playlist-modify-private"
client_id = 'client_id'
client_secret = 'secret'
redirect_uri = 'https://example.com/callback/'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

year = date.split('-')[0]
song_uris = []

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)