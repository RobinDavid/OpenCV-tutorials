import cv2.cv as cv

im = cv.LoadImage("img/lena.jpg",3)

cv.SetImageROI(im, (50,50,150,150))

cv.Zero(im)
#cv.Set(im, cv.RGB(100, 100, 100))

cv.ResetImageROI(im)

cv.ShowImage("Image",im)

cv.WaitKey(0)