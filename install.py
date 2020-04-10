import requests
import json
import os

links_json=requests.get("https://install.ftmc.me/links.json").text
links=json.loads(links_json)
links=links['type']
print("可以安装的目标：")
for i in range(len(links)-1):
    print("\t{}) {}".format(i,links[i]["name"]))
while(1):
    target=input("请选择要安装的目标（输入序号）：")
    if target in range(len(links)-1):
        break
    else:
        print("选项不存在")
link=links[target]["link"]
os.system("wget --no-check-certificate https://install.ftmc.me/{0} -O {0}".format(link))
os.system("python3 {}".format(link))
os.remove(link)