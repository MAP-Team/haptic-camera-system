from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import imutils
import cv2
import io

def get_depth(self, stereo):
        plt.clf()


        # First send the tuple of images to i2d
        disp = i2d(stereo, 16)

        # Then send the disparity to haptic
        # haptic = np.array(depth_to_haptic(disp))
        # plt.scatter(haptic[:, 0], haptic[:, 1])
        # buf = io.BytesIO()
        # plt.savefig(buf, format='png')
        # buf.seek(0)
        # plt.clf()

        plt.imshow(disp, 'gray')
        buf = io.BytesIO()

        plt.savefig(buf1, format='png')
        buf.seek(0)

        return buf.read() # buf.read(), 















