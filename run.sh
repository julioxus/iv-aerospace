#!/bin/bash

# Variables

APPENGINE_SERVER="google_appengine/dev_appserver.py"

# Lanzar aplicación (con autoconfirmación)

echo y | python $APPENGINE_SERVER  src --host=0.0.0.0 --port=80 --admin_port=8080 --storage_path=database &
