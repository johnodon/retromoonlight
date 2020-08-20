"""
Script to generate a launch script for each game available in moonlight
"""
import sys
import os
import stat

RefreshListScript = 'Refresh.sh'

BashHeader = '#!/bin/bash\n'
StreamString = 'moonlight stream -1080 -app '
roms_directory = '/home/pi/RetroPie/roms/moonlight/'
ip = '192.168.1.50'
space = ' '


def clear_directory(folder_path):
    """
    Clears the directory of old game launching scripts
    :param folder_path: The path to the folder to clear
    """
    for the_file in os.listdir(folder_path):
        try:
            file_path = os.path.join(folder_path, the_file)
            if os.path.isfile(file_path) \
                and the_file != RefreshListScript \
                and not the_file.endswith(('.txt', 'py')):
                    os.unlink(file_path)
        except Exception as e:
            print(e)


def read_games_list(file_path):
    """
    Reads the contents of a file
    :param file_path: path of the file to read in
    :return: contents of the file
    """
    input_data = ""
    if os.path.isfile(file_path):
        f = open(file_path, "r")
        input_data = f.readlines()
        f.close()
    return input_data

def get_game_name(game_listing):
    import re as regex
    search_result = regex.search("\d+\.\s(.*)", game_listing)

    if search_result:
        return search_result.group(1)

    return None

def is_valid_listing(game_listing):
    """
    Check to see if a single line from the listings is a valid game name
    :param game_listing: A single line of text from the Moonlight List command
    :return: True if it is a valid listing, False otherwise
    """
    import re as regex
    return regex.search("\d+\.\s.*", game_listing) is not None

def create_script(game_title):
    """
    Creates the script to run a game title
    :param game_title: The name of the game to launch
    """
    script = '{}{}\"{}\"'.format(BashHeader, StreamString, game_title, space, ip)
    print('\nCreating a script for {}:'.format(game_title))
    print(script)
    return script


def write_script(script, game_title):
    """
    Writes a script string to disk
    :param script: The string to be written as the script
    :param game_title: The game title to be used as the file name
    """
    try:
        script_name = '{}{}.sh'.format(roms_directory, game_title.replace(":", ""))
        print('Writing {} to disk...'.format(script_name))
        f = open(script_name, "w+")
        f.write(script)
        f.close()

        st = os.stat(script_name)
        os.chmod(script_name, st.st_mode | stat.S_IEXEC)
    except Exception as write_exception:
        print(write_exception)


try:
    RawInputList = read_games_list(sys.argv[1])
except Exception as e:
    exit(e)


clear_directory(roms_directory)

for gameListing in RawInputList:
    game_name = get_game_name(gameListing)

    if game_name:
        write_script(create_script(game_name), game_name)
