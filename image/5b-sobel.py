import cv2.cv as cv

im=cv.LoadImage('img/build.png', cv.CV_LOAD_IMAGE_GRAYSCALE)

sobx = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 1)
cv.Sobel(im, sobx, 1, 0, 3) #Sobel with x-order=1

soby = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 1)
cv.Sobel(im, soby, 0, 1, 3) #Sobel withy-oder=1

cv.Abs(sobx, sobx)
cv.Abs(soby, soby)

result = cv.CloneImage(im)
cv.Add(sobx, soby, result) #Add the two results together.

cv.Threshold(result, result, 100, 255, cv.CV_THRESH_BINARY_INV)

cv.ShowImage('Image', im)
cv.ShowImage('Result', result)

cv.WaitKey(0)