from flask import Flask, render_template, Response
from stream import streamer

server = Flask(__name__)

def generate():

  while True:
      s = streamer()
      yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + s + b'\r\n\r\n')

@server.route('/')
def camera():
  return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    server.run()