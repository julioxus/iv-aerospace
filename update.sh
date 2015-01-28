#!/bin/bash

if [ -d iv-aerospace]; then
	rm -rf iv-aerospace
fi
sudo service ivaerospace stop
git clone https://github.com/julioxus/iv-aerospace
cd iv-aerospace
chmod +x uninstall.sh
chmod +x install.sh
sudo ./uninstall.sh
sudo ./install.sh
