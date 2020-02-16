from stream_object import Stream
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile

import matplotlib.pyplot as plt


cam1 = Stream()
cam1.start()

def print_images():
    count = 0
    while count < 100:
        tup = cam1.read()
        disp = i2d(tup)
        haptic = depth_to_haptic(disp)
        plt.imshow(haptic)
        count += 1

    cam1.stop()
cProfile.run('print_images()')