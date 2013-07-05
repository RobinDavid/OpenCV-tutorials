import cv2.cv as cv

im = cv.LoadImageM("../img/fruits.jpg",cv.CV_32F)

def getDistance(pixel,refcolor):
    return abs( (pixel[0]-refcolor[0]) + (pixel[1]-refcolor[1]) + (pixel[2]-refcolor[2]) )


refcolor = (0,0,0)
minDist = 100

for row in range(im.rows):
    for col in range(im.cols):
        if getDistance(im[row,col], refcolor)<minDist:
            im[row,col] = (255,255,255)


cv.ShowImage("Distance", im)

cv.WaitKey(0)