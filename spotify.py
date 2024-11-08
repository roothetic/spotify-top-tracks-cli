import os
import spotipy
from rich import box
from rich.table import Table
from dotenv import load_dotenv
from rich.console import Console
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def convert_time_range(time_range) -> str:
    if time_range == "long_term":
        return "since the beginning"
    elif time_range == "medium_term":
        return "for the last 6 months"
    else:
        return "for the last month"
    
def ms_to_min_sec_format(milliseconds) -> str:
    total_seconds = milliseconds // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:02d}"

def connect_to_spotify() -> spotipy.Spotify:
    try:
        client_id: str = os.getenv('CLIENT_ID')
        client_secret: str = os.getenv('CLIENT_SECRET')
        redirect_uri: str = os.getenv('REDIRECT_URI')
        cache_path: str = os.getenv('CACHE_PATH')

        if not client_id or not client_secret or not redirect_uri:
                raise ValueError("Missing Spotify API credentials. Please check environment variables.")

        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope='user-top-read',
                                                            cache_path=cache_path))
        
        return spotify
    
    except spotipy.exceptions.SpotifyException as se:
        print('Spotify API error during connection: ', se)

    except ValueError as ve:
        print('Value error: ', ve)

    except Exception as e:
        print('Unknown error during Spotify connection: ', e)

    return None

def create_table(time_range: str, limit: int) -> bool:
    try:
        spotify: spotipy.Spotify = connect_to_spotify()
        top_tracks = spotify.current_user_top_tracks(time_range=time_range, limit=limit)

        if not top_tracks or 'items' not in top_tracks:
            print('Error: No top tracks found. Please check the parameters.')
            return False

        period = convert_time_range(time_range)
        counter: int = 0

        table = Table(title=f'Your top {limit} {period}', box=box.SIMPLE)

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
        return True  

    except spotipy.exceptions.SpotifyException as se:
        print('Spotify API error: ', se)

    except KeyError as ke:
        print('Data processing error: Missing key - ', ke)

    except ValueError as ve:
        print('Value error: ', ve)

    except Exception as e:
        print('Unknown Error: ', e)

    return False
    
