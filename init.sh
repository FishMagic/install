#!/bin/bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
wget --no-check-certificate https://install.ftmc.me/install.sh -O install.sh
chmod +x install.sh
bash install.sh