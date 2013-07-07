#! /usr/bin/env python

# import the necessary things for OpenCV
import cv2.cv as cv

#############################################################################
# some "constants"

win_size = 10
MAX_COUNT = 500


if __name__ == '__main__':

    # first, create the necessary windows
    cv.NamedWindow ('LkDemo', cv.CV_WINDOW_AUTOSIZE)

    frame = cv.LoadImage("../img/build.png")

    image = cv.CreateImage (cv.GetSize (frame), 8, 3)
    image.origin = frame.origin
    grey = cv.CreateImage (cv.GetSize (frame), 8, 1)
    prev_grey = cv.CreateImage (cv.GetSize (frame), 8, 1)
    pyramid = cv.CreateImage (cv.GetSize (frame), 8, 1)
    prev_pyramid = cv.CreateImage (cv.GetSize (frame), 8, 1)
    features = []

    # copy the frame, so we can draw on it
    cv.Copy (frame, image)

    # create a grey version of the image
    cv.CvtColor (image, grey, cv.CV_BGR2GRAY)

    # create the wanted images
    eig = cv.CreateImage (cv.GetSize (grey), 32, 1)
    temp = cv.CreateImage (cv.GetSize (grey), 32, 1)

    # the default parameters
    quality = 0.01
    min_distance = 10

    # search the good points
    features = cv.GoodFeaturesToTrack (
        grey, eig, temp,
        MAX_COUNT,
        quality, min_distance, None, 3, 0, 0.04)

    # refine the corner locations
    features = cv.FindCornerSubPix (
        grey,
        features,
        (win_size, win_size),  (-1, -1),
        (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 20, 0.03))

    # calculate the optical flow
    features, status, track_error = cv.CalcOpticalFlowPyrLK (
        prev_grey, grey, prev_pyramid, pyramid,
        features,
        (win_size, win_size), 3,
        (cv.CV_TERMCRIT_ITER|cv.CV_TERMCRIT_EPS, 20, 0.03),
        0)

    # set back the points we keep
    features = [ p for (st,p) in zip(status, features) if not st]

    # draw the points as green circles
    for the_point in features:
        cv.Circle (image, (int(the_point[0]), int(the_point[1])), 3, (0, 255, 0, 0), -1, 8, 0)

    # swapping
    prev_grey, grey = grey, prev_grey
    prev_pyramid, pyramid = pyramid, prev_pyramid
    
    # we can now display the image
    cv.ShowImage ('LkDemo', image)

    # handle events
    c = cv.WaitKey(0)
