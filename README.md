# python-live-stream-zeromq

## Installation & Dependencies

This package has multiple dependencies that are listed below:

opencv

imagezmq

zeromq

## Setting Up

If there is more than one camera, change the number in:

> camera = cv2.VideoCapture(0) 

## Viewing the Stream

**In server.py, enter your local IP Address to allow other devices on the same network to view your stream.**

Run both client.py and server.py files in your virtual environment.

> python client.py

> python server.py

Go to chrome and enter the URl below:

> http://127.0.0.1:5000

A live stream of your webcam should now be shown. 
