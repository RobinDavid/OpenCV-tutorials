import cv2.cv as cv

capture = cv.CaptureFromFile('../img/paulvideo.avi')

nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))

#CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream
#CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream

fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)

wait = int(1/fps * 1000/1)

duration = (nbFrames * fps) / 1000

print 'Num. Frames = ', nbFrames
print 'Frame Rate = ', fps, 'fps'
print 'Duration = ', duration, 'sec'


for f in xrange( nbFrames ):
    
    frameImg = cv.QueryFrame(capture)
    
    print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES) # Number of the frame
    
    cv.ShowImage("The Video",  frameImg)
    cv.WaitKey(wait)
