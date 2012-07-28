import cv2.cv as cv

capture=cv.CaptureFromCAM(0)

frame1 = cv.QueryFrame(capture)
frame1gray = cv.CreateMat(frame1.height, frame1.width, cv.CV_8U)
cv.CvtColor(frame1, frame1gray, cv.CV_RGB2GRAY)

res = cv.CreateMat(frame1.height, frame1.width, cv.CV_8U)

frame2gray = cv.CreateMat(frame1.height, frame1.width, cv.CV_8U)

while True:
    frame2 = cv.QueryFrame(capture)
    cv.CvtColor(frame2, frame2gray, cv.CV_RGB2GRAY)
    
    cv.Smooth(frame2gray, frame2gray, cv.CV_BLUR, 12,12)
    
    cv.Cmp(frame1gray, frame2gray, res, cv.CV_CMP_EQ) #Call the compare with the tow frames
    
    cv.ShowImage("Image", frame2)
    cv.ShowImage("Res", res)

    cv.Copy(frame2gray, frame1gray)
    c=cv.WaitKey(1)
    if c==27: #Break if user enters 'Esc'.
        break
    
    