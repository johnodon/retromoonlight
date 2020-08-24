# RetroPie Moonlight #
	
This is a set of scripts with the intent of helping people stream games from their PC to their RetroPie. These scripts use [Moonlight](http://moonlight-stream.com/) to query your PC for your available games and generates a "Console" within RetroPi along with a set of "Roms" representing your games. Each rom is actually a shell script configured to tell moonlight to begin streaming the game of your choice.
![alt text](https://github.com/joelghill/retromoonlight/blob/master/Images/moonlight_gameslist.png "Moonlight game collection in Eudora theme")

## Why this fork
Retromoonlight has not been updated for the past three years. 
Unfortunately, some issues makes it unusable.

This fork does not add anything but simply fix the setup scripts by doing two things:
	*itimer.gpg is checked out in the retromoonlight folder, fix chown called
	*moonlight cannot be installed without libcurl3, which is no longer available. Instead, moonlight will be compiled using libcurl4 

## Why Use This? ##
There is already a [solution available](https://github.com/TechWizTime/moonlight-retropie) for streaming Steam Big Picture Mode, why bother using this? There are a few reasons:

  1. Using this script RetroPie will have a list of games it can display with scraped meta-data from the web.
  2. I've found Steam BPM to be unreliable when used with RetroPie and I wanted something better.
  
## Minimum Requirements ##
  * Raspberry Pi running Raspian Stretch (or latest RetroPie release)
  * GPU: Desktop: GeForce GTX 650 or higher desktop GPU.
  * CPU: Intel Core i3-2100 3.1GHz or AMD Athlon II X4 630 2.8 GHz or higher.
  * System Memory: 4 GB or higher.

## Setup ##
#### On your PC: ####
  1. Install and activate [GeFore Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/)
  2. In GeForce Expereince, go to Shield Settings and enable game streaming.

#### On your raspberry pi: ####
  1. git clone https://github.com/johnodon/retromoonlight.git
  2. cd retromoonlight
  3. sudo bash ./Install.sh. If a first time install, use option 1. Otherwise you can use the other options to install select components, or remove MoonLight from RetroPie
  5. Run emulationstation
  
Once EmulationStation is running, navigate to the Moonlight console, select the "Refresh" rom, then reboot emultationstation after the script is finished.

## Usage ##
Emulationstation should now have an entry for Moonlight. There will be a single "Rom" called refresh. Use this to update your games list. After using refresh command you will need to reboot emulationstation.

## Credits ##

Thanks to [Jowl Ghill](https://github.com/joelghill/retromoonlight) for the original code.
A huge thank you to [TechWizTime](https://github.com/TechWizTime) for his work in creating the install and setup script for moonlight in RetroPie. I am building on his work and could not have developed this without following his example!



