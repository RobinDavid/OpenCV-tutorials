import cv2.cv as cv

im = cv.LoadImage("img/lena.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE)
thresholded = cv.CreateImage(cv.GetSize(im), 8, 1)

def onChange(val):
    cv.Threshold(im, thresholded, val, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage("Image", thresholded)


onChange(100) #Call here otherwise at startup. Show nothing until we move the trackbar
cv.CreateTrackbar("Thresh", "Image", 100, 255, onChange) #Threshold value arbitrarily set to 100

cv.WaitKey(0)

'''
capture=cv.CaptureFromCAM(0)

value = 100

def onChange(val):
    global value
    value = val
    #cv.Threshold(im, dst, value, 255, cv.CV_THRESH_BINARY)

cv.NamedWindow("Image")
cv.CreateTrackbar("Mytrack", "Image", 100, 255, onChange)
tmp = cv.QueryFrame(capture)
gray = cv.CreateImage(cv.GetSize(tmp), 8, 1)

while True:
    frame=cv.QueryFrame(capture)
    cv.CvtColor(frame, gray, cv.CV_BGR2GRAY)
    cv.Threshold(gray, gray, value, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage("Image",gray)
    c=cv.WaitKey(1)
    if c==27: #Break if user enters 'Esc'.
        break
'''