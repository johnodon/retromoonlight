#!/bin/bash

echo -e "\nUpdating System..."
apt-get update -y

echo -e "\nInstalling Moonlight..."
apt-get install git libopus0 libexpat1 libasound2 libudev1 libavahi-client3 libcurl4 libevdev2 libenet7 libssl-dev libopus-dev libasound2-dev libudev-dev libavahi-client-dev libcurl4-openssl-dev libevdev-dev libexpat1-dev libpulse-dev uuid-dev libenet-dev cmake gcc g++ fakeroot debhelper -y
git clone https://github.com/irtimmer/moonlight-embedded.git
cd moonlight-embedded
git submodule update --init
mkdir build
cd build/
cmake ../
make
sudo make install
sudo ldconfig
cd retromoonlight
echo -e "\nMoonlight Installed!"
