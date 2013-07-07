import cv2.cv as cv

im=cv.LoadImage('../img/fruits.jpg',cv.CV_LOAD_IMAGE_COLOR)

res = cv.CreateImage(cv.GetSize(im), cv.CV_8UC2, 3) #cv.CV_32F, cv.IPL_DEPTH_16S, ...
cv.Convert(im, res)
cv.ShowImage("Converted",res)

res2 = cv.CreateImage(cv.GetSize(im), cv.CV_8UC2, 3)
cv.CvtColor(im, res2, cv.CV_RGB2BGR) # HLS, HSV, YCrCb, ....
cv.ShowImage("CvtColor", res2)

cv.WaitKey(0)