# import requests
import matplotlib.pyplot as plt
from flask import Flask, render_template
from stream_object import Stream
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic


app = Flask(__name__)
stream = Stream()
stream.start()


@app.route('/')
def index():
    """Return homepage."""
    tup = stream.read()
    disp = i2d(tup, 16)
    haptic = depth_to_haptic(disp)
    plt.imshow(haptic)
    return render_template('index.html', tup=tup, haptic=haptic)
