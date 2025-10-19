sudo apt update
sudo apt install python3 python3-pip -y
sudo apt install python3-venv

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --config python
python --version
pip --version