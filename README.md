# Duino Coin Dashboard Node
The worker node for the Duinocoin dashboard.

## About

This is the worker for the [Duino Coin Dashboard](https://github.com/o850cHQk/duco-dashboard). 
The worker scraps the [Duino Coin API Server](https://explorer.duinocoin.com/) for wallet updates and then parses this information to the Dashboard. 

## Setup

To set this up simply clone this repo or download it and run it on your pc, there is a simple setup that is prompted when you first run it.

NOTE Only run one of these nodes, the software has not been designed to run multiple.

For Linux 
```
sudo apt update
sudo apt install python3 python3-pip git screen -y
git clone https://github.com/o850cHQk/duco-dashboard-node.git
cd duco-dashboard-node
python3 -m pip install -r requirements.txt
```

To run this simply use `python3 Duco-Dash-Worker.py` you can also use screen to this to run in the background or other methods.

## Configuration

The configuration is done when the Worker is run for the first time it will ask for 2 things when started

- Website URL: This is the full url to the base folder of your site, for example `https://example.site.com` this can also be subfolders as well eg `https://example.site.com/dashboard`
- API Key: This is the api key that you setup in your config.php in the Dashboard, if you did not change this from the default this will not work.

Your worker should now start showing you logs of jobs it needs to parse! 