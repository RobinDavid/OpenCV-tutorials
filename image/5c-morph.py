import cv2.cv as cv

image=cv.LoadImage('../img/build.png', cv.CV_LOAD_IMAGE_GRAYSCALE)

#Get edges
morphed = cv.CloneImage(image)
cv.MorphologyEx(image, morphed, None, None, cv.CV_MOP_GRADIENT) # Apply a dilate - Erode

cv.Threshold(morphed, morphed, 30, 255, cv.CV_THRESH_BINARY_INV)

cv.ShowImage("Image", image)
cv.ShowImage("Morphed", morphed)

cv.WaitKey(0)
