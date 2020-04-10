#!/bin/bash
sudo apt update
sudo apt install python3 python3-pip -y
wget --no-check-certificate https://install.ftmc.me/install.py -O install.py
chmod +x install.py
pip3 -i https://pypi.tuna.tsinghua.edu.cn/simple install requests
python3 install.py