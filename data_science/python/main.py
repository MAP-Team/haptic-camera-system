from stream_object import Stream
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile
import numpy as np
import matplotlib.pyplot as plt

import io


cams = Stream()
cams.start()

def print_images():
    tup = cam1.read()

    # First send the tuple of images to i2d
    disp = i2d(tup, 16)

    # Then send the disparity to haptic
    haptic = depth_to_haptic(disp)
    plt.scatter(haptic[:, 0], haptic[:, 1])
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


print_images()
