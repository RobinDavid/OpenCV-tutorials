import cv2.cv as cv

im = cv.LoadImage("img/lena.jpg", cv.CV_8U)

cv.SetImageROI(im, (1, 1,30,30))

histsize = 256 #Because we are working on grayscale pictures
hist = cv.CreateHist([histsize], cv.CV_HIST_ARRAY, [[0,histsize]], 1)
cv.CalcHist([im], hist)


cv.NormalizeHist(hist,1) # The factor rescale values by multiplying values by the factor
_,max_value,_,_ = cv.GetMinMaxHistValue(hist)

if max_value == 0:
    max_value = 1.0
cv.NormalizeHist(hist,256/max_value)

cv.ResetImageROI(im)

res = cv.CreateMat(im.height, im.width, cv.CV_8U)
cv.CalcBackProject([im], res, hist)

cv.Rectangle(im, (1,1), (30,30), (0,0,255), 2, cv.CV_FILLED)
cv.ShowImage("Original Image", im)
cv.ShowImage("BackProjected", res)
#--------------------------------------------------------


'''
# For colored pictures !
im = cv.LoadImage("img/lena.jpg")

r = cv.CreateImage(cv.GetSize(im), 8, cv.CV_8UC1)
g = cv.CreateImage(cv.GetSize(im), 8, cv.CV_8UC1)
b = cv.CreateImage(cv.GetSize(im), 8, cv.CV_8UC1)
cv.Split(im, r, g, b, None)

cv.SetImageROI(r, (1, 1,30,30))
cv.SetImageROI(g, (1, 1,30,30))
cv.SetImageROI(b, (1, 1,30,30))
planes = [r,g,b]

histsize = [256,256,256]

hist = cv.CreateHist(histsize, cv.CV_HIST_ARRAY, [[0,256],[0,256],[0,256]], 1)
cv.CalcHist([cv.GetImage(i) for i in planes], hist)

cv.NormalizeHist(hist,1)
_,max_value,_,_ = cv.GetMinMaxHistValue(hist)

if max_value == 0:
    max_value = 1.0
    
cv.NormalizeHist(hist,1/max_value)

cv.ResetImageROI(r)
cv.ResetImageROI(g)
cv.ResetImageROI(b)


res = cv.CreateImage((im.width,im.height), 8, 3)
cv.CalcBackProject([r,g,b], res, hist)

thresh = cv.CloneImage(res)
cv.Threshold(thresh, thresh, 1.0, 256, cv.CV_THRESH_BINARY)


cv.Rectangle(im, (1,1), (30,30), (0,0,255), 2, cv.CV_FILLED)
cv.ShowImage("Original Image", im)
cv.ShowImage("Threshed", thresh)
cv.ShowImage("BackProjected", res)
'''

cv.WaitKey(0)