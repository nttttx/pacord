"""Entry point of program"""

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

from os import getpid
from time import sleep
from . import (discord, playerctl)

# i think it is not the best way to show rpc only if any players are availible but idc
while True:
    if playerctl.any_player_is_availible():
        players = playerctl.get_players()
        discord.update(players[0])
    else:
        discord.RPC.clear(pid=getpid())
    sleep(1)
