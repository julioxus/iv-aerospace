#!/bin/bash

if [ -d iv-aerospace]; then
	rm -rf iv-aerospace
fi
git clone https://github.com/julioxus/iv-aerospace
cd iv-aerospace
sudo ./uninstall.sh
sudo ./install.sh
