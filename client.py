import base64
import cv2
import zmq

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.bind('tcp://127.0.0.1:5555')

camera = cv2.VideoCapture(0)  # init the camera
print("Camera initiated")

while True:
    grabbed, frame = camera.read()  # grab the current frame
    # frame = cv2.resize(frame, (320, 240))  # resize the frame
    encoded, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer)
    footage_socket.send(jpg_as_text)
    