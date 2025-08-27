import click
from helpers import (
    list_users, create_user, create_playlist, view_user_playlists,
    view_playlist_songs, add_song_to_playlist, delete_song,
    search_songs, seed_sample_data
)
from models import session

@click.group()
def cli():
    """🎵 Music App CLI - Manage your music playlists with ease!"""
    pass

# User commands
@cli.command()
def list_users_cmd():
    """List all users"""
    list_users()

@cli.command()
@click.option('--name', prompt='User name', help='Name of the user')
@click.option('--email', prompt='User email', help='Email address of the user')
def create_user_cmd(name, email):
    """Create a new user"""
    create_user(name, email)

# Playlist commands
@cli.command()
@click.option('--user-id', prompt='User ID', type=int, help='ID of the user who owns the playlist')
@click.option('--title', prompt='Playlist title', help='Title of the playlist')
@click.option('--description', default=None, help='Description of the playlist (optional)')
def create_playlist_cmd(user_id, title, description):
    """Create a new playlist"""
    create_playlist(user_id, title, description)

@cli.command()
@click.option('--user-id', prompt='User ID', type=int, help='ID of the user')
def list_playlists_cmd(user_id):
    """List all playlists for a user"""
    view_user_playlists(user_id)

# Song commands
@cli.command()
@click.option('--playlist-id', prompt='Playlist ID', type=int, help='ID of the playlist')
@click.option('--title', prompt='Song title', help='Title of the song')
@click.option('--artist', prompt='Artist name', help='Artist of the song')
@click.option('--album', default=None, help='Album name (optional)')
def add_song_cmd(playlist_id, title, artist, album):
    """Add a song to a playlist"""
    add_song_to_playlist(playlist_id, title, artist, album)

@cli.command()
@click.option('--playlist-id', prompt='Playlist ID', type=int, help='ID of the playlist')
def list_songs_cmd(playlist_id):
    """List all songs in a playlist"""
    view_playlist_songs(playlist_id)

@cli.command()
@click.option('--song-id', prompt='Song ID', type=int, help='ID of the song to delete')
def delete_song_cmd(song_id):
    """Delete a song from a playlist"""
    delete_song(song_id)

@cli.command()
@click.option('--search-term', prompt='Search term', help='Search for songs by title, artist, or album')
def search_songs_cmd(search_term):
    """Search for songs across all playlists"""
    search_songs(search_term)

# Utility commands
@cli.command()
def seed_data_cmd():
    """Load sample data into the database"""
    seed_sample_data()

@cli.command()
def interactive_mode():
    """Start interactive mode with menus"""
    from interactive import interactive_main
    interactive_main()

if __name__ == '__main__':
    cli()