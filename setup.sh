# create python env 
python3 -m venv env

# check if "env/Scripts/activate" file exists

if [ -f "env/Scripts/activate" ]; then
    source env/Scripts/activate
else
    source env/bin/activate
fi

# install dependencies
pip install -r requirements.txt

# verify installation
pip list