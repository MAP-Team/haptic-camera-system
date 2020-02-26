from flask import Flask, render_template, Response
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import io
from pipeline import Pipeline

app = Flask(__name__)

pipe = Pipeline(3)
pipe.start()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_stream_left')
def video_stream_left():
    return Response(pipe.gen('left'),
            mimetype='multipart/x-mixed-replace; boundary=stream_left')

@app.route('/video_stream_right')
def video_stream_right():
    return Response(pipe.gen('right'),
            mimetype='multipart/x-mixed-replace; boundary=stream_right')

@app.route('/video_stream_disp')
def video_stream_disp():
    return Response(pipe.gen('disp'),
            mimetype='multipart/x-mixed-replace; boundary=stream_right')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)