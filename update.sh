#!/bin/bash

if [ -d iv-aerospace]; then
	rm -rf iv-aerospace
fi
git clone https://github.com/julioxus/iv-aerospace
cd iv-aerospace
sudo /bin/bash uninstall.sh
sudo /bin/bash install.sh
