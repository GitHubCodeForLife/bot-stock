if [ -f "env/Scripts/activate" ]; then
    source env/Scripts/activate
else
    source env/bin/activate
fi
# run file run.py 
uwsgi --ini uwsgi.ini