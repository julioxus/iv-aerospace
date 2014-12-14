#!/bin/bash

# Variables
PROJECT_DIR="apps/iv-aerospace/workspace/guestbook"
APPENGINE_SERVER="apps/google_appengine/dev_appserver.py"

# Lanzar aplicación (con autoconfirmación)

echo y | python $APPENGINE_SERVER $PROJECT_DIR/src
