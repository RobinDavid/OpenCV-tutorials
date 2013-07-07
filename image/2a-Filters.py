import cv2.cv as cv

image=cv.LoadImage('../img/lena.jpg', cv.CV_LOAD_IMAGE_COLOR) #Load the image
cv.ShowImage("Original", image)

grey = cv.CreateImage((image.width ,image.height),8,1) #8depth, 1 channel so grayscale
cv.CvtColor(image, grey, cv.CV_RGBA2GRAY) #Convert to gray so act as a filter
cv.ShowImage('Greyed', grey) 

smoothed = cv.CloneImage(image)
cv.Smooth(image,smoothed,cv.CV_MEDIAN) #Apply a smooth alogrithm with the specified algorithm cv.MEDIAN
cv.ShowImage("Smoothed", smoothed)

cv.EqualizeHist(grey, grey) #Work only on grayscaled pictures
cv.ShowImage('Equalized', grey)

threshold1 = cv.CloneImage(grey)
cv.Threshold(threshold1,threshold1, 100, 255, cv.CV_THRESH_BINARY)
cv.ShowImage("Threshold Binary", threshold1)

threshold2 = cv.CloneImage(grey)
cv.Threshold(threshold2,threshold2, 100, 255, cv.CV_THRESH_OTSU)
cv.ShowImage("Threshold OTSU", threshold2)

element_shape = cv.CV_SHAPE_RECT
pos=3
element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
cv.Dilate(grey,grey,element,2) #Replace a pixel value with the maximum value of neighboors
#There is others like Erode which replace take the lowest value of the neighborhood
#Note: The Structuring element is optionnal
cv.ShowImage("Dilated", grey)

cv.WaitKey(0)