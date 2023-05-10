# colour filter script

# imports
# =================================
import cv2
import numpy as np
# =================================

# main
# =================================
# frame import
# -------------------------
frameUnfiltered = cv2.imread()
# needs to be configured to import individual frames
# -------------------------

# colour thresholds
# -------------------------
# upper
rHigh = 255
gHigh = 225
bHigh = 150
# lower
rLow = 200
gLow = 100
bLow = 40
# remember that openCV deals in BGR instead of RGB
# -------------------------

def frameFilter(frame, rHigh, gHigh, bHigh, rLow, gLow, bLow):
    (rows, cols, layers) = frame.shape
    frameFiltered = np.zeros((rows, cols, layers), dtype=np.ubyte)
    for i in range(rows):
        for j in range(cols):
            frameFiltered[i, j, (0, 1, 2)] = frame[i, j, (0, 1, 2)]
            if rHigh >= frame[i, j, 2] >= rLow and gHigh >= frame[i, j, 1] >= gLow and bHigh >= frame[i, j, 0] >= bLow:
                frameFiltered[i, j, (0, 1, 2)] = (0, 0, 0)
    return frameFiltered
    # image filter function, checks each pixel and compares it to a predetermined range of BGR values
    # if the value of the pixel falls between the range, then its replaced by black

def mask(frame, rHigh, gHigh, bHigh, rLow, gLow, bLow):
    frameMask = cv2.inRange(frame, (bLow, gLow, rLow), (bHigh, gHigh, rHigh))
    frameMasked = cv2.bitwise_and(frameMask, frameMask)
    return frameMasked
    # creates a mask where white = sand, black = object
    # for future use with depth cam

def displayFrame(frame, name):
    cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(name, frame)
    cv2.resizeWindow(name, (800, 400))
    # test function - needs to be configured to output the filtered frame

frameFiltered = frameFilter(frameUnfiltered, rHigh, gHigh, bHigh, rLow, gLow, bLow)
displayFrame(frameUnfiltered, "imageUnfiltered")
displayFrame(frameFiltered, "imageFiltered")
cv2.waitKey()
cv2.destroyAllWindows()
# =================================

# to do
# =================================
# config to work with video frames

# tune BGR values to work with the rover camera
# test using HSV values instead of BGR for detection - may require less fine tuning?

# add function to detect payload
# -------------------------
# add second filter function that detects the payload instead of rocks and sand
# would need to know colour range for payload though
# -------------------------

# integrate use of depth camera
# -------------------------
# use mask with depth camera, so that the script can find the distance to all objects detected
# use that to output depth map of only objects, ignoring sand and other background objects
# could use to throw up warnings if distance <= specified distance
# -------------------------
# =================================
