from stream_object import Stream
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile
import numpy as np
import matplotlib.pyplot as plt


cam1 = Stream()
cam1.start()

def print_images():
    count = 0
    while count < 100:
        plt.clf()
        tup = cam1.read()
        disp = i2d(tup)
        haptic = np.array(depth_to_haptic(disp))
        plt.scatter(haptic[:, 0], haptic[:, 1])
        plt.draw()
        plt.pause(0.05)
        count += 1

    cam1.stop()

plt.show()
print_images()
