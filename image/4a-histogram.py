import cv2.cv as cv

def drawGraph(ar,im, size): #Draw the histogram on the image
    minV, maxV, minloc, maxloc = cv.MinMaxLoc(ar) #Get the min and max value
    hpt = 0.9 * histsize
    for i in range(size):
        intensity = ar[i] * hpt / maxV #Calculate the intensity to make enter in the image
        cv.Line(im, (i,size), (i,int(size-intensity)),cv.Scalar(255,255,255)) #Draw the line
        i += 1

#---- Gray image
orig = cv.LoadImage("../img/lena.jpg", cv.CV_8U)

histsize = 256 #Because we are working on grayscale pictures which values within 0-255

hist = cv.CreateHist([histsize], cv.CV_HIST_ARRAY, [[0,histsize]], 1)

cv.CalcHist([orig], hist) #Calculate histogram for the given grayscale picture

histImg = cv.CreateMat(histsize, histsize, cv.CV_8U) #Image that will contain the graph of the repartition of values
drawGraph(hist.bins, histImg, histsize)

cv.ShowImage("Original Image", orig)
cv.ShowImage("Original Histogram", histImg)
#---------------------

#---- Equalized image
imEq = cv.CloneImage(orig)
cv.EqualizeHist(imEq, imEq) #Equlize the original image

histEq = cv.CreateHist([histsize], cv.CV_HIST_ARRAY, [[0,histsize]], 1)
cv.CalcHist([imEq], histEq) #Calculate histogram for the given grayscale picture
eqImg = cv.CreateMat(histsize, histsize, cv.CV_8U) #Image that will contain the graph of the repartition of values
drawGraph(histEq.bins, eqImg, histsize)

cv.ShowImage("Image Equalized", imEq)
cv.ShowImage("Equalized HIstogram", eqImg)
#--------------------------------

cv.WaitKey(0)