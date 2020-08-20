#!/bin/bash

echo -e "\nCreating Moonlight Menu for RetroPie..."

DIRECTORY=/home/pi/.emulationstation/es_systems.cfg

if [ -f $DIRECTORY ]
then	
    echo -e "Removing Duplicate Systems File"
    rm $DIRECTORY
fi

echo -e "Copying Systems Config File"
cp /etc/emulationstation/es_systems.cfg $DIRECTORY

echo -e "Adding Moonlight to Systems"
sudo sed -i -e 's|</systemList>|  <system>\n    <name>moonlight</name>\n    <fullname>Moonlight</fullname>\n    <path>~/RetroPie/roms/moonlight</path>\n    <extension>.sh .SH</extension>\n    <command>bash %ROM%</command>\n    <platform>pc</platform>\n    <theme>moonlight</theme>\n  </system>\n</systemList>|g' $DIRECTORY
sudo chown pi:pi /opt/retropie/configs/all/emulationstation/es_systems.cfg
echo -e "\nMoonlight menu added to RetroPie..."
