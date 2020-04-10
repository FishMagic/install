import os

os.system("wget https://mirrors.ftmc.me/openj9.tar.gz -O openj9.tar.gz")
os.system("tar xvf openj9.tar.gz")
os.remove("openj9.tar.gz")
os.system("mv jdk* jdk")
os.mkdir("/usr/local/java")
os.system("mv jdk /usr/local/java")
os.system("cp /etc/profile /etc/profile.bak")
os.system("echo 'export JAVA_HOME=/usr/local/java/jdk' >> /etc/profile")
os.system("echo 'export CLASSPATH=$:CLASSPATH:$JAVA_HOME/lib/' >> /etc/profile")
os.system("echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile")
os.system("source /etc/profile")