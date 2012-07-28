import cv2.cv as cv

capture = cv.CaptureFromFile('img/paulvideo.avi')

nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))
fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)
wait = int(1/fps * 1000/1)

dst = cv.CreateImage((int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH)),
                      int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))), 8, 1)

for f in xrange( nbFrames ):
    
    frame = cv.QueryFrame(capture)
    
    cv.CvtColor(frame, dst, cv.CV_BGR2GRAY)
    cv.Canny(dst, dst, 125, 350)
    cv.Threshold(dst, dst, 128, 255, cv.CV_THRESH_BINARY_INV)
    
    cv.ShowImage("The Video", frame)
    cv.ShowImage("The Dst", dst)
    cv.WaitKey(wait)