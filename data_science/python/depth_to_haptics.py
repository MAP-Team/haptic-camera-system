import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import cProfile

imgL = cv.imread('../data/tsukuba_l.png',0)
imgR = cv.imread('../data/tsukuba_r.png',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')

h = 16
y = 125
imgL_trim = imgL[y:y+h].copy()
imgR_trim = imgR[y:y+h].copy()
disparity = stereo.compute(imgL_trim, imgR_trim)
plt.imshow(disparity, 'gray')

def depth_to_haptic(disparity):
    ''' 
    A function to convert depth data into haptic data
        Args:
            disparity (array): an array of and images depth values
        Returns:
            haptic_data (array): an array of haptic values 
    
    The function currently takes in the disparity array, gets the horizontal 
    pixel position or the middle of the depth values (the pixels on the screen),
    horizontal resolution, and then runs through the depth values at the 
    horizontal pixle position. As it runs through, it calculates theta from the 
    depth values from eachvpixel using the equasion ((horizontal-pixile-position
    / horizontal-resolution)- 0.5)*62.2, then converts the outcome into radians.
    Once theta is calculated, it calculates the x and y values using the equasion
    sin(theta)*depth for the x value and cos(theta)*depth for the x value
    
    The next step is to take the x and y values and compare them to the haptic positions
    '''
    computed_values_array = []
    horiz_resolution = len(disparity[8])
    for pixel_position in range(0, len(disparity[8])-1):
        depth = (256-disparity[8][pixel_position])
        theta = np.radians(((pixel_position/horiz_resolution)-0.5)*62.2)
        x, y = np.sin(theta)*depth, np.cos(theta)*depth
        computed_values_array.append((x, y))
    return computed_values_array

cProfile.run('depth_to_haptic(disparity)')

# results = depth_to_haptic(disparity)
# X = [cord[0] for cord in results]
# Y = [cord[1] for cord in results]

# plt.xlim((-200, 200))
# plt.ylim((0, 400))
# plt.scatter(X, Y,)