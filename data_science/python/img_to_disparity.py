import cv2
from matplotlib import pyplot as plt
from numpy import ndim


def img_to_disp(img_tup):
    """Converts a tuple of images to an opencv disparity"""
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    imgL, imgR = img_tup
    h = 16
    y = 125
    imgL_trim = imgL[y:y + h].copy()
    imgR_trim = imgR[y:y + h].copy()

    if imgL.ndim == 3:
        imgL_trim = cv2.cvtColor(imgL_trim, cv2.COLOR_BGR2GRAY)
        imgR_trim = cv2.cvtColor(imgR_trim, cv2.COLOR_BGR2GRAY)
    disparity = stereo.compute(imgL_trim, imgR_trim)
    return disparity


if __name__ == '__main__':
    imgL = cv2.imread('../data/tsukuba_l.png', 0)
    imgR = cv2.imread('../data/tsukuba_r.png', 0)
    disp = img_to_disp((imgL, imgR))
    plt.imshow(disp, 'gray')
    plt.show()
