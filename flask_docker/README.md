# Flask_web appliction 
The tiny web application with a single route (/reload) that accepts a POST request to the endpoint.

## Dependencies requirement: 
- Nginx  (web server)
- Flask (web framework)
- Requests 
- Python3

## Installation Command
   sudo apt update
   sudo apt install python3
   sudo apt install python3-pip
   sudo pip3 install flask
   sudo pip3 install requests

## Step
	- Installation all tools above
	- Setup Flask web app on Systemd
	- (can use command curl to see the HTTP host/port)
	- Configure Nginx then restart/reload Nginx
	- Verify reload button from URL : as setup in Nginx Conf 

## Script recall Flask app : .py
Basically, this script just requset POST send secret_code"TC-reactor-reload" as we setup on Tcreactor config file, to port 8084!

![image](https://github.com/lunchakon/Python_Projects/assets/33216011/f9052631-3e71-4f45-a3e2-17c1b58b824c)
