import cv2
from matplotlib import pyplot as plt


def img_to_disp(img_tup, height):
    """Converts a tuple of images to an opencv disparity with height in px"""
    # Creating objects to manipulate
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    imgL, imgR = img_tup

    # Trimming images to 16px tall, starting at y=125px
    h = height
    y = 125
    imgL_trim = imgL[y:y + h].copy()
    imgR_trim = imgR[y:y + h].copy()

    # Check if image is in color
    if imgL.ndim == 3:
        # Convert it to grayscale if so
        imgL_trim = cv2.cvtColor(imgL_trim, cv2.COLOR_BGR2GRAY)
        imgR_trim = cv2.cvtColor(imgR_trim, cv2.COLOR_BGR2GRAY)

    # Compute and return disparity values
    disparity = stereo.compute(imgL_trim, imgR_trim)
    return disparity


if __name__ == '__main__':
    # Testing with sample images
    imgL = cv2.imread('../data/tsukuba_l.png', 0)
    imgR = cv2.imread('../data/tsukuba_r.png', 0)
    disp = img_to_disp((imgL, imgR), 16)
    plt.imshow(disp, 'gray')
    plt.show()
