#!/usr/bin/env bash
# this script sets up wec server for deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "this is a fake HTML file" > sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '31a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
