import cv2.cv as cv

image=cv.LoadImage('img/lena.jpg', cv.CV_LOAD_IMAGE_COLOR) #Load the image

font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font

y = image.height / 2 # y position of the text
x = image.width / 4 # x position of the text

cv.PutText(image,"Hello World !", (x,y),font, cv.RGB(255, 255, 255)) #Draw the text

cv.ShowImage('Hello World', image) #Show the image
cv.WaitKey(0)