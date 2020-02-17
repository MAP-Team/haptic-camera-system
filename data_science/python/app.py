from flask import Flask, render_template, Response
from flask_stream import VideoCameraLeft, VideoCameraRight

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed_left')
def video_feed_left():
    lvs = VideoCameraLeft()
    return Response(gen(lvs),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_right')
def video_feed_right():
    rvs = VideoCameraRight()
    return Response(gen(rvs),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)