#!/bin/bash

# Variables
PROJECT_DIR="apps/iv-aerospace/workspace/guestbook"
APPENGINE_SERVER="apps/google_appengine/dev_appserver.py"

# Lanzar aplicación (con autoconfirmación)

echo y | python $APPENGINE_SERVER $PROJECT_DIR/src &

if [ $(curl localhost:8080 | wc -l) > 0 ]; then
        echo  '\n LA WEB FUNCIONA!!! \n'
else
        echo "\n LA WEB NO FUNCIONA :S \n"
fi
