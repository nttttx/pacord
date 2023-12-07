"""Adapter for playerctl"""

# This code is modified version of github.com/abhishekmj303/ulauncher-playerctl/blob/main/playerctl/__init__.py file
# Original source code/file was published under GPLv3 license.


import subprocess
from .obj import Player


def _run(cmd: str) -> str:
    try:
        output = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        return output
    except subprocess.CalledProcessError:
        return None


def any_player_is_availible() -> bool:
    """Check if any player is running"""
    result = _run("playerctl -l")
    if result in ["No players found", ""]:
        return False
    return True


def get_player_info(player: str) -> Player:
    """Get info about player"""
    status = _run(f"playerctl -p {player} status")
    if status in ["No players found", ""]:
        return Player(player, None, None, None, None)
    return Player(
        player,
        status,
        get_player_metadata_value(player, "artist"),
        get_player_metadata_value(player, "album"),
        get_player_metadata_value(player, "title"),
    )


def get_player_metadata_value(player: str, key: str) -> str:
    """Get player`s metadata value"""
    return _run(f"playerctl -p '{player}' metadata {key}")


def get_players() -> [Player]:
    """Get availible players"""
    if not any_player_is_availible():
        return None
    result = _run("playerctl -l").split("\n")
    players = []
    for player in result:
        players.append(get_player_info(player))
    return players
