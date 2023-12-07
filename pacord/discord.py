"""Code for pushing player data in discord."""

# Copyright (C) 2023  nttttx <nttxcf@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from os import environ
from pypresence import Presence
from .obj import Player

try:
    client_id = environ["CLIENT_ID"]
except KeyError:
    sys.exit("CLIENT_ID is not set!")

RPC = Presence(client_id)
RPC.connect()


def update(player: Player) -> None:
    """Push info"""
    RPC.update(
        state=f"{player.state} in {player.name}",
        details=f"{player.song} by {player.artist}",
    )
