#!/bin/bash

echo '[Duco-Dash]' > Settings.cfg
echo "api = ${API}" >> Settings.cfg
echo "url = ${URL}" >> Settings.cfg
echo "debug = ${DEBUG}" >> Settings.cfg

cat Settings.cfg

python3 Duco-Dash-Worker.py