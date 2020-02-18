from stream_object import Stream
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile
import numpy as np
import matplotlib.pyplot as plt


cams = Stream()
cams.start()

def print_images():
    count = 0
    while count < 10:
        plt.clf()
        tup = cams.read()
        disp = i2d(tup, 16)
        haptic = depth_to_haptic(disp)
        plt.imshow(haptic)
        count += 1

    cams.stop()

#streams video from opencv to flask 
def gen(stream):
    while True:
        frame = stream.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')