#!/bin/bash
moonlight list 192.168.1.50 > gameslist.txt
python3 ~/RetroPie/roms/moonlight/GenerateGamesList.py "./gameslist.txt"
rm ./gameslist.txt
