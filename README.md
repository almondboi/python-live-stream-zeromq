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

> http://**HOST IP**:5000

A live stream of your webcam should now be shown. 

## Viewing in FreeBoard Pane

1. Launch FreeBoard, after adding a widget and selecting HTML, paste the following code in the HTML box:

> <html><head><meta name="viewport" content="width=device-width, minimum-scale=0.1"></head><body style="margin: 0px; background: #0e0e0e;"><img style="-webkit-user-select: none;margin: auto;" src="http://** HOST IP **:5000/"></body></html>


2. Adjust the colums and height to be able to see the full image. 
