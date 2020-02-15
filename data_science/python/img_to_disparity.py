import cv2
from matplotlib import pyplot as plt


def img_to_disp(img_tup):
    """Converts a tuple of images to an opencv disparity"""
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    imgL, imgR = img_tup
    h = 16
    y = 125
    imgL_trim = imgL[y:y + h].copy()
    imgR_trim = imgR[y:y + h].copy()
    disparity = stereo.compute(imgL_trim, imgR_trim)
    return disparity


if __name__ == '__main__':
    imgL = cv2.imread('data_science/data/tsukuba_l.png', 0)
    imgR = cv2.imread('data_science/data/tsukuba_r.png', 0)
    disp = img_to_disp((imgL, imgR))
    plt.imshow(disp, 'gray')
    plt.show()
