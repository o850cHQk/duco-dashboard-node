#!/usr/bin/env python3

"""
Duino Dashboard worker

Made by Vargink and a bunch of people online after i googled
"""

from os import _exit
from configparser import ConfigParser
from pathlib import Path
from time import ctime, sleep, strptime, time

def install(package):
    try:
        pip.main(["install",  package])
    except AttributeError:
        check_call([sys.executable, '-m', 'pip', 'install', package])
    call([sys.executable, __file__])

try:
    import requests
except ModuleNotFoundError:
    print("Requests is not installed. "
          + "We will try to automatically install it "
          + "If it fails, please manually execute "
          + "python3 -m pip install requests")
    install('requests')

try:
    from colorama import Back, Fore, Style, init
    init(autoreset=True)
except ModuleNotFoundError:
    print("Colorama is not installed. "
          + "We will try to automatically install it "
          + "If it fails, please manually execute "
          + "python3 -m pip install colorama")
    install("colorama")

class Settings:
    VER = '0.1'
    WEB_URL = ''
    WEB_TIMEOUT = 15
    API = ''

config = ConfigParser()


def debug_output(text: str):
    if debug == 'y':
        print(Style.RESET_ALL + Fore.WHITE
              + now().strftime(Style.DIM + '%H:%M:%S.%f ')
              + Style.NORMAL + f'DEBUG: {text}')

def handler(signum, frame):
    msg = "Ctrl-c was pressed. Exiting "
    _exit(1)

def load_config():
    global debug
    global userID
    global userTime
    global userName
    global checkinterval
    if not Path('./Settings.cfg').is_file():
        website_works = False
        while not website_works:
            Settings.WEB_URL = input(
                    Style.RESET_ALL + Fore.YELLOW
                    + 'Please enter the dashboard url eg https://duco.tcmeta.net'
                    + Fore.RESET + Style.BRIGHT)
            Settings.API = input(
                    Style.RESET_ALL + Fore.YELLOW
                    + 'Please enter your api key'
                    + Fore.RESET + Style.BRIGHT)
            server = requests.get(f"{Settings.WEB_URL}/api/v1/runner/?api={Settings.API}" , 
                             timeout=Settings.WEB_TIMEOUT).json()
            website_works = server["id"]
            userID = server["id"]
            userName = server["name"]
            userTime = server["lastChecked"]
            checkinterval = server["checkTime"]
            if not website_works:
                print('Couldnt connect to site please try again')
        
        config["Duco-Dash"] = {
            'api':         Settings.API,
            'url':         Settings.WEB_URL,
            'debug':       'n' }

        with open('./Settings.cfg', 'w') as configfile:
            config.write(configfile)
        print(Style.RESET_ALL + 'Config Saved')

    else:
        config.read('./Settings.cfg')
        Settings.WEB_URL = config["Duco-Dash"]['url']
        Settings.API = config["Duco-Dash"]['api']
        debug = config["Duco-Dash"]['debug']
        server = requests.get(f"{Settings.WEB_URL}/api/v1/runner/?api={Settings.API}" , 
                                timeout=Settings.WEB_TIMEOUT).json()
        userID = server["id"]
        userName = server["name"]
        userTime = server["lastChecked"]
        checkinterval = server["checkTime"]

init(autoreset=True)
print(f"Duco Dashboard - {str(Settings.VER)})")
    
try:
    load_config()
    debug_output('Config file loaded')
except Exception as e:
    print(Style.RESET_ALL + 'Couldnt load config')
    print(e);
    sleep(10)
    _exit(1)

while True:
    # okay check the time of the current user to the unix time 
    now = int( time() )
    if (int(userTime) + int(checkinterval) > now):
        sleep(1)
        continue
    # get the latest user data
    try:
        server = requests.get(f"https://server.duinocoin.com/users/{userName}" , 
                                timeout=Settings.WEB_TIMEOUT).json()
        minersTotal = 0
        hashrateTotal = 0
        for miners in server['result']['miners']:
            minersTotal += 1
            hashrateTotal += miners['hashrate']
        nowRounded = int(now//60 * 60)
        postData = {
            'userID': userID,
            'balance': server['result']['balance']['balance'],
            'stakeAmount': server['result']['balance']['stake_amount'],
            'verfied': (server['result']['balance']['verified'] == 'yes'),
            'mintersTotal': minersTotal,
            'hashrateTotal': hashrateTotal,
            'checkedTime': nowRounded
        }
        print(postData)
        server = requests.post(f"{Settings.WEB_URL}/api/v1/runner/?api={Settings.API}", data=postData , 
                                timeout=Settings.WEB_TIMEOUT).json()
        print(server)
        userID = server["id"]
        userName = server["name"]
        userTime = server["lastChecked"]
        checkinterval = server["checkTime"]
    except Exception as e:
        print(Style.RESET_ALL + 'could not update user, sleeping for 10 seconds and trying again')
        print(e);
        sleep(10)

