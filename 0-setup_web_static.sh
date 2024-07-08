#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update package lists and install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the necessary directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file with simple content
echo "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, removing the old one if it exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '
  /index index.html;/ a \
    \n  location /hbnb_static/ { \
    alias /data/web_static/current/; \
    }
' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

# Output status message
echo "Setup completed successfully."
