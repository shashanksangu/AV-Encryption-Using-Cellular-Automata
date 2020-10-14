# For faster and efficient mathematical evaluations we use numpy
import numpy as np
# For image proccesing we use openCV
import cv2
# For creating and manipulating files
import os
# the time package provides various time-related functions
import time

# Create a video capture object to capture a video using device(camera) or from an existing video
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc =  cv2.VideoWriter_fourcc('M','P','E','G')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# Create a directory for storing the frames
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

# Sometimes, cap(video capture object) may not have initialized the capture. In that case cap.read() raises an error.
# So we first check if the capture has been initialized by using the isOpened() method and use the open() method to initilaise the capture(if necessary...)

if not cap.isOpened() :
    cap.open()

# log the start time in seconds using the time() function
start = time.time()
currentFrame = 0

while(time.time()-start < 2):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

	    # Saves image of the current frame in jpg file
        name = './data/frame'+str(currentFrame) +'.png'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1
    else:
        break


# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
