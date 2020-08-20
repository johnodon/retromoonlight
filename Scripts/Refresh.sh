#!/bin/bash
moonlight list "$ip" > gameslist.txt
python3 ~/RetroPie/roms/moonlight/GenerateGamesList.py "./gameslist.txt"
rm ./gameslist.txt
