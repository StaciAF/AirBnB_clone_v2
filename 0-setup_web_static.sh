#!/usr/bin/env bash
# Configures a web server for web_static deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Nginx test content" >> /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
# TODO: Add nginx config here. sed and alias
sudo service nginx restart

