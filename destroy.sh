#!/bin/sh
kill -9 `ps -ef|grep -v grep |grep dev_appserver | awk '{print $2}'`
