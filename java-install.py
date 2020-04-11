import os
import requests
import json

links_json=requests.get("https://install.ftmc.me/java-install.json").text
links=json.loads(links_json)
links=links['version']
print("Which can be installed:")
for i in range(len(links)):
    print("\t{}) {}".format(i,links[i]["name"]))
while(1):
    target=int(input("Choose one to install:"))
    if target in range(len(links)):
        break
    else:
        print("Your choose is not exist.")
print("Which is you want to downlaod from:\n\t0) Origin\n\t1) Mirros")
while(1):
    downlaod=int(input("Chooes one to downlaod:"))
    if target==0:
        os.system("wget --no-check-certificate {} -O openj9.tar.gz".format(links[target]["directDownloadLink"]))
    elif target==1:
        os.system("wget --no-check-certificate {} -O openj9.tar.gz".format(links[target]["mirrorDownloadLink"]))
    else:
        print("Your choose is not exist.")
os.system("tar xvf openj9.tar.gz")
os.remove("openj9.tar.gz")
os.system("mv {}/ {}/".format(links[target]["originName"],links[target]["targetName"]))
try:
    os.mkdir("/usr/local/java")
finally:
    os.system("mv {} /usr/local/java".format(links[target]["targetName"]))
    os.system("cp /etc/profile /etc/profile.bak")
    os.system("echo 'export JAVA_HOME=/usr/local/java/{}' >> /etc/profile".format(links[target]["targetName"]))
    os.system("echo 'export CLASSPATH=$:CLASSPATH:$JAVA_HOME/lib/' >> /etc/profile")
    os.system("echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile")
    os.system("source /etc/profile")