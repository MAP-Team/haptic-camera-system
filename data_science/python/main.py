from stream_object import Stream
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
# from matplotlib import pyplot as plt

cam1 = Stream()
cam1.run()

while cam1.size() > 0:
    tup = cam1.dequeue()
    disp = i2d(tup)
    haptic = depth_to_haptic(disp)
    print(haptic)
