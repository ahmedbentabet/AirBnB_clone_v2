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
cat << 'EOF' > /etc/nginx/sites-available/default
server {
	listen 80;
	server_name 7md.tech;
	root /var/www/html;
	index index.html;

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}

	location /about {
		root /var/www/html;
	}

	location /blog {
		alias /var/www/html/blog;
	}

	add_header X-Served-By $hostname;

	location / {
		try_files $uri $uri/ =404;
	}
	location /redirect_me {
		return 301 google.com;
	}

	error_page 404 /errors/404.html;
	location = /errors/404.html {
		internal;
	}
}
EOF

# Restart Nginx to apply the changes
sudo service nginx restart
