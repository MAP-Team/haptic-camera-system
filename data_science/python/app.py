from flask import Flask, render_template, Response
from stream import Stream
from main import get_frame

app = Flask(__name__, static_url_path='/static')

stream = Stream()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed_left')
def video_feed_left():
    lvs = stream.lvs
    return Response(gen(lvs),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_right')
def video_feed_right():
    rvs = stream.rvs
    return Response(gen(rvs),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
