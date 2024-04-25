#!/bin/bash

#activate venv and start flask and open browser
#open browser
xdg-open http://localhost:5000 &
#end.sh


source .venv/bin/activate

python3 main.py

# #wait for flask to start
# while ! nc -z localhost 5000; do   
#     sleep 0.1 # wait for 100ms before check again
# done

