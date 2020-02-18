import cProfile
import numpy as np

def depth_to_haptic(disparity, camera_fov=62.2, max_depth=200):
    ''' 
    A function to convert depth data into haptic data by converting a 
    disparity array to 
        Args:
            disparity (array): an array of two images' depth values
        Returns:
            haptic_values (array): an array of haptic values 
    '''
    # # Averages out the the depth values by column
    # avg_disparity = [0 for value in disparity[0]]
    # for row in disparity:
    #     for index in range(0, len(row)-1):
    #         avg_disparity[index] += row[index]
    # for index in range(0, len(avg_disparity)-1):
    #     avg_disparity[index] /= len(disparity)
    avg_disparity = disparity[8]

    # Converts the averaged depth values into haptic values
    haptic_values = []
    horizontal_resolution = len(avg_disparity)
    for pixel_position in range(0, horizontal_resolution-1):
        disparity_value = (256-avg_disparity[pixel_position])
        theta = np.radians(((pixel_position / horizontal_resolution) - 0.5) * camera_fov)
        x, y = (np.sin(theta) * disparity_value), (np.cos(theta) * disparity_value)
        haptic_values.append((x, y))
    return haptic_values

    

if (__name__ == '__main__'):
    cProfile.run('depth_to_haptic(disparity)')
