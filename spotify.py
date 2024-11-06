import os
import spotipy
from rich import box
from rich.table import Table
from dotenv import load_dotenv
from rich.console import Console
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def connect_to_spotify() -> spotipy.Spotify:
    client_id: str = os.getenv('CLIENT_ID')
    client_secret: str = os.getenv('CLIENT_SECRET')
    redirect_url: str = os.getenv('REDIRECT_URL')
    cache_path: str = os.getenv('CACHE_PATH')

    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                        client_secret=client_secret,
                                                        redirect_url=redirect_url,
                                                        scope='user-top-read',
                                                        cache_path=cache_path))
    
    return spotify