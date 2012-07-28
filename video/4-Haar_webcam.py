import cv2.cv as cv

capture=cv.CaptureFromCAM(0)

hc = cv.Load("../haarcascades/haarcascade_frontalface_alt.xml")

while True:
    frame=cv.QueryFrame(capture)
    faces = cv.HaarDetectObjects(frame, hc, cv.CreateMemStorage(), 1.2,2, cv.CV_HAAR_DO_CANNY_PRUNING, (0,0) )
    
    for ((x,y,w,h),stub) in faces:
        cv.Rectangle(frame,(int(x),int(y)),(int(x)+w,int(y)+h),(0,255,0),2,0)

    cv.ShowImage("Window",frame)
    c=cv.WaitKey(1)
    if c==27 or c == 1048603: #If Esc entered
        break