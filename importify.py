import csv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Autentica
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                               client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='playlist-modify-private'))

# Le o arquivo CSV
with open('my_lib.csv', 'r') as f:
    reader = csv.reader(f)
    tracks = list(reader)

# Busca os IDs das faixas no Spotify
track_ids = []
for track in tracks:
    results = sp.search(q=track, limit=1)
    if results['tracks']['items']:
        track_ids.append(results['tracks']['items'][0]['id'])

# Exibe no console as track_ids para confirmar que foram encontradas
print(track_ids)

# Cria a playlist
playlist = sp.user_playlist_create(sp.me()['id'], 'Favoritas', public=False)

# Adiciona as faixas a playlist em lotes de 100 (limite do Spotify)
for i in range(0, len(track_ids), 100):
    sp.playlist_add_items(playlist['id'], track_ids[i:i+100])