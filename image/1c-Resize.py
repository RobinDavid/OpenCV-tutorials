import cv2.cv as cv

im = cv.LoadImage("../img/alkaline.jpg") #get the image

thumb = cv.CreateImage((im.width / 2, im.height / 2), 8, 3) #Create an image thatis twice smaller than the original
cv.Resize(im, thumb) #resize the original image into thumb
#cv.PyrDown(im, thumb)
cv.SaveImage("thumb.png", thumb) # save the thumb image
