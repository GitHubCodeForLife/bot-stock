if [ -f "env/Scripts/activate" ]; then
    source env/Scripts/activate
else
    source env/bin/activate
fi
# run file run.py 
python run.py