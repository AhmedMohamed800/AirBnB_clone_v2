#!/usr/bin/env bash
# install nginx

sudo apt-get update
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
	<head>
	</head>
	<body>
		<p>Hello World!</p>
	</body>
	</html>" | sudo tee  /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "server {
	listen      80 default_server;
	listen      [::]:80 default_server ipv6only=on;
	server_name _;
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=DHITmcKUGik;
	}
	location /hbnb_static {
		alias /data/web_static/current;
	}
	error_page 404 /404.html;
	location /404 {
		root /var/www/error/;
		internal;
	}
	}" | sudo tee  /etc/nginx/sites-available/default
	

sudo service nginx restart

exit 0
