import cv2.cv as cv
import math

im = cv.LoadImage("../img/build.png", cv.CV_LOAD_IMAGE_GRAYSCALE)
im2 = cv.CloneImage(im)

# Goodfeatureto track algorithm
eigImage = cv.CreateMat(im.height, im.width, cv.IPL_DEPTH_32F)
tempImage = cv.CloneMat(eigImage)
cornerCount = 500
quality = 0.01
minDistance = 10

corners = cv.GoodFeaturesToTrack(im, eigImage, tempImage, cornerCount, quality, minDistance)

radius = 3
thickness = 2

for (x,y) in corners:
    cv.Circle(im, (int(x),int(y)), radius, (255,255,255), thickness)
    
cv.ShowImage("GoodfeaturesToTrack", im)

#SURF algorithm
hessthresh = 1500 # 400 500
dsize = 0 # 1
layers = 1 # 3 10

keypoints, descriptors = cv.ExtractSURF(im2, None, cv.CreateMemStorage(), (dsize, hessthresh, 3, layers))
for ((x, y), laplacian, size, dir, hessian) in keypoints:
    cv.Circle(im2, (int(x),int(y)), cv.Round(size/2), (255,255,255), 1)
    x2 = x+((size/2)*math.cos(dir))
    y2 = y+((size/2)*math.sin(dir))
    cv.Line(im2, (int(x),int(y)), (int(x2),int(y2)), (255,255,255), 1)

cv.ShowImage("SURF ", im2)

cv.WaitKey(0)