import os
import spotipy
from rich import box
from rich.table import Table
from dotenv import load_dotenv
from rich.console import Console
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def convert_time_range(time_range):
    if time_range == "long_term":
        return "since the beginning"
    elif time_range == "medium_term":
        return "for the last 6 months"
    else:
        return "for the last month"
    
def ms_to_min_sec_format(milliseconds):
    total_seconds = milliseconds // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:02d}"

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

def create_table(time_range: str, limit: int) -> None:
    try:
        spotify: spotipy.Spotify = connect_to_spotify()
        top_tracks = spotify.current_user_top_tracks(time_range=time_range, limit=limit)
        counter: int = 0

        table = Table(title='Your top {limit} {period}', box=box.SIMPLE)

        table.add_column("RANK", justify="right", header_style="bold bright_green", style="bright_green")
        table.add_column("TITLE", header_style="bold bright_blue", style="bright_blue")
        table.add_column("ARTIST", header_style="bold bright_green", style="bright_green")
        table.add_column("DURATION", header_style="bold bright_blue", style="bright_blue")
        table.add_column("PUBLISHED", justify="center", header_style="bold bright_green", style="bright_green")
        table.add_column("CURRENT POPULARITY", justify="center", header_style="bold bright_blue", style="bright_blue")

        for track in top_tracks['items']:
            counter += 1
            table.add_row(
                f"{counter}",
                f"{track['name']}",
                f"{track['artists'][0]['name']}",
                f"{ms_to_min_sec_format(track['duration_ms'])} min",
                f"{track['album']['release_date']}",
                f"{track['popularity']}"
                )

        console = Console()
        print()
        console.print(table)  

    except Exception as e:
        print('Unknown Error: ', e)
        return None
