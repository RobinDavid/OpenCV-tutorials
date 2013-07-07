import cv2.cv as cv#or simply import cv

im = cv.LoadImage("../img/lena.jpg")
im2 = cv.LoadImage("../img/fruits-larger.jpg")
cv.ShowImage("Image1", im)
cv.ShowImage("Image2", im2)

res = cv.CreateImage(cv.GetSize(im2), 8, 3) 

cv.Add(im, im2, res) #Add every pixels together (black is 0 so low change and white overload anyway)
cv.ShowImage("Add", res)

cv.AbsDiff(im, im2, res) # Like minus for each pixel im(i) - im2(i)
cv.ShowImage("AbsDiff", res)

cv.Mul(im, im2, res) #Multiplie each pixels (almost white)
cv.ShowImage("Mult", res)

cv.Div(im, im2, res)  #Values will be low so the image will likely to be almost black
cv.ShowImage("Div", res)

cv.And(im, im2, res) #Bit and for every pixels
cv.ShowImage("And", res)

cv.Or(im, im2, res) # Bit or for every pixels
cv.ShowImage("Or", res)

cv.Not(im, res) # Bit not of an image
cv.ShowImage("Not", res)

cv.Xor(im, im2, res) #Bit Xor
cv.ShowImage("Xor", res)

cv.Pow(im, res, 2) #Pow the each pixel with the given value
cv.ShowImage("Pow", res)

cv.Max(im, im2, res) #Maximum between two pixels
#Same form Min MinS
cv.ShowImage("Max",res)

cv.WaitKey(0)