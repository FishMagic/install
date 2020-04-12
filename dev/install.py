import requests
import os
install_json=requests.get("https://install.ftmc.me/dev/links.json").text
install=json.loads(install_json)
currentVersion="1.0.0b"
remoteVersion=install_json["version"]

def wget(url, fileName):
    os.system("wget --no-check-certificate {} -O {}".format(url, fileName))

def getUpadte():
    print("当前版本为：{}".format(currentVersion))
    print("最新版本为：{}".format(remoteVersion))
    if currentVersion!=remoteVersion:
        os.system("echo {} > pid")
        print("脚本将自动更新")
        wget("https://install.ftmc.me/dev/install.sh", "install.sh")
        os.system("chmod +x install.sh")
        os.system("bash install.sh")

def getSelect(ranges):
    while(1):
        select=int(input("请选择一项："))
        if select in ranges:
            break
        else:
            print("您的选项不正确！")
        return select

def main():
    links=install["type"]
    print("请选择您要安装/升级的软件：")
    for i in range(len(links)):
        print("\t{}) {}".format(i,links[i]["name"]))
    target=getSelect(range(len(links)))
    link=links[target]["link"]
    wget("https://install.ftmc.me/dev/{}".format(link),link)
    os.system("sudo python3 {}".format(link))
    os.remove(link)

getUpadte()
main()