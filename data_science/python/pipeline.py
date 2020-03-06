# import the necessary packages
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
from queue import Queue
from threading import Thread
from img_to_disparity import img_to_disp as i2d
from depth_to_haptic import depth_to_haptic
import cProfile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import io
from circular_buffer import CircularBuffer

class Pipeline:
    # created a *threaded* video stream, allow the camera sensor to warmup,
    # and start the FPS counter
    print("[INFO] sampling THREADED frames from webcam...")

    #Constructor creates a list
    def __init__(self, fixed_size):
        self.vs1 = WebcamVideoStream(src=0) #For anylizing 
        self.vs1.start()
        self.vs2 = WebcamVideoStream(src=0) #For anylizing 
        self.vs2.start()
        self.cb = CircularBuffer(fixed_size)
        self.stopped = False
        self.current_stream = (None, None)
        self.disp = None
        self.haptic = None

    #Start thread 
    def start(self):
        t = Thread(target=self.capture, args=())
        t.daemon = True
        t.start()
        return self

    def stop(self):
        self.stopped = True

    def capture(self):
		# keep looping infinitely
			# if the thread indicator variable is set, stop the
			# threa
        while not self.stopped:
            left_captured_frame = self.vs1.read()
            right_captured_frame = self.vs2.read()
            self.cb.enqueue((left_captured_frame, right_captured_frame))



    def push(self):
        pushed_stereo = self.capture() 
        self.cb.enqueue(pushed_stereo) 

    def pull(self):
        pulled_stereo = self.cb.dequeue()
        return pulled_stereo
    
    def get_disp(self):
        plt.clf()
        self.disp = i2d(self.stereo, 16)
        plt.imshow(self.disp, 'gray')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return buf.read()

    def get_depth(self):
        plt.clf ()
        # Then send the disparity to haptic
        self.haptic = np.array(depth_to_haptic(self.disp))
        plt.scatter(self.haptic[:, 0], self.haptic[:, 1])
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return buf.read()


    def get_frame(self):
        stereo_feed = self.stereo
        # depth = self.process(stereo_feed)
        left_feed = stereo_feed[0]
        right_feed = stereo_feed[1]

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        l_ret, l_jpeg = cv2.imencode('.jpg', left_feed)
        r_ret, r_jpeg = cv2.imencode('.jpg', right_feed)
        return l_jpeg.tobytes(), r_jpeg.tobytes()    

    def gen(self, dir):
        self.stereo = self.pull()
        self.current_stream = self.get_frame()
        while True:
            if dir == 'left':
                yield (b'--stream_left\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + self.current_stream[0] + b'\r\n\r\n')
            if dir == 'right':
                yield (b'--stream_right\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + self.current_stream[1] + b'\r\n\r\n')
            if dir == 'disp':
                self.disp = self.get_disp()
                yield (b'--stream_right\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + self.disp + b'\r\n\r\n')
            if dir == 'depth':
                yield (b'--stream_depth\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + self.haptic + b'\r\n\r\n')

                

                

            
        
    



        
        
        
    

        






        

        
        
