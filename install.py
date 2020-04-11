import requests
import json
import os

links_json=requests.get("https://install.ftmc.me/links.json").text
links=json.loads(links_json)
links=links['type']
print("Which can be installed:")
for i in range(len(links)):
    print("\t{}) {}".format(i,links[i]["name"]))
while(1):
    target=int(input("Choose on to install:"))
    if target in range(len(links)):
        break
    else:
        print("Your choose is not exist.")
link=links[target]["link"]
os.system("wget --no-check-certificate https://install.ftmc.me/{0} -O {0}".format(link))
os.system("sudo python3 {}".format(link))
os.remove(link)