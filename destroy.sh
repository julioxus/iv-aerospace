#!/bin/bash

line=$(ps -ef|grep -v grep |grep dev_appserver | awk '{print $2}')
if [[ $line -gt 0 ]];
    then
    kill -9 `ps -ef|grep -v grep |grep dev_appserver | awk '{print $2}'`
else
	echo 'El servicio no está funcionando. Omitiendo...'
fi
