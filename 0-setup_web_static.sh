#!/usr/bin/env bash
# this script sets up web server for deployment
fake_html="<html>\n\t<head>\n\t</head>\n\t<body>\n\tHolberton School, this is a fake HTML file\n\t</body>\n</html>"

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo -e "$fake_html" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '31a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default

sudo service nginx restart
