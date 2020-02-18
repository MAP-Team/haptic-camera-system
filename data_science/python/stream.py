# import the necessary packages
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
from queue import Queue
from threading import Thread
from camera import LeftCamera, RightCamera


class Stream:
    # created a *threaded* video stream, allow the camera sensor to warmup,
    # and start the FPS counter
    print("[INFO] sampling THREADED frames from webcam...")
    
    #Constructor creates a list
    def __init__(self, queue_size=128):
        self.vs1 = WebcamVideoStream(src=1).start() #For anylizing 
        self.lvs = LeftCamera() #For streaming to flask 
        self.vs2 = WebcamVideoStream(src=2).start() #For anylizing   
        self.rvs = RightCamera() #For streaming to flask
      
        
        self.stopped = False
        self.Q = Queue(maxsize=queue_size)

    #Start thread 
    def start(self):
        t = Thread(target=self.run, args=())
        t.daemon = True
        t.start()
        return self



    #     self.queue = list()
      
    # #Adding elements to queue
    # def enqueue(self,data):
    #     #Checking to avoid duplicate entry (not mandatory
    #     self.queue.insert(0,data)
    
    # #Removing the last element from the queue
    # def dequeue(self):
    #   if len(self.queue)>0:
    #       return self.queue.pop()
    #   return ("Queue Empty!")
    
    # #Getting the size of the queue
    # def size(self):
    #     return len(self.queue)

    # #printing the elements of the queue
    # def printQueue(self):
    #     print(self.queue)
    #     return self.queue

    def read(self):
        return self.Q.get()

    def stop(self):
        self.stopped = True

    
    def run(self):
        self.fps = FPS().start()
        # loop over some frames...this time using the threaded stream
        # while self.fps._numFrames < 100:
        while not self.stopped:
            # grab the frame from the threaded video stream and resize it
            # to have a maximum width of 400 pixels
            frame1 = self.vs1.read()
            frame1 = imutils.resize(frame1, width=400)
            frame2 = self.vs2.read()
            frame2 = imutils.resize(frame2, width=400)
            stereo = (frame1, frame2)
            self.Q.put(stereo)         

            # check to see if the frame should be displayed to our screen
            # if args["display"] > 0:
            #     cv2.imshow("Frame", frame)
            #     key = cv2.waitKey(1) & 0xFF
            # update the FPS counter
            self.fps.update()
        # stop the timer and display FPS information
        # self.fps.stop()
        print("[INFO] elasped time: {:.2f}".format(self.fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(self.fps.fps()))
        # do a bit of cleanup
        # cv2.destroyAllWindows()
        self.vs1.stop()
        self.vs2.stop()



# if __name__ == '_main__':
#     cam1 = Stream()
#     cam1.run()
#     cam1.printQueue()



# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--num-frames", type=int, default=100,
# 	help="# of frames to loop over for FPS test")
# ap.add_argument("-d", "--display", type=int, default=-1,
# 	help="Whether or not frames should be displayed")
# args = vars(ap.parse_args())
