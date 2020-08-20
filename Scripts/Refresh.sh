#!/bin/bash
moonlight list "$ipaddress" > gameslist.txt
python3 ~/RetroPie/roms/moonlight/GenerateGamesList.py "./gameslist.txt"
rm ./gameslist.txt
