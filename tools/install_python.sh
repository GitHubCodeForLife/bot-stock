sudo apt update
sudo apt install python3 python3-pip -y

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --config python

python --version
pip --version

# uninstall python3 
sudo apt remove python3 -y
sudo apt autoremove -y