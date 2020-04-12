#!/bin/bash
if [ -f pid ]; then
    PID=$(cat pid)
    sudo kill -QUIT $PID
fi
rm pid
wget --no-check-certificate https://install.ftmc.me/install.py -O install.py
chmod +x install.py
python3 install.py