import cv2.cv as cv


image = cv.LoadImageM("img/lena.jpg", cv.CV_LOAD_IMAGE_COLOR)
tmp1 = cv.CreateMat(1, 13 * 5, cv.CV_64FC1)
tmp2 = cv.CreateMat(1, 13 * 5, cv.CV_64FC1)
mask = cv.CreateMat(image.rows, image.cols, cv.CV_8UC1)
cv.GrabCut(image, mask, (10,10,200,200), tmp1, tmp2, 5, cv.GC_INIT_WITH_RECT)

cv.Set(mask[mask == cv.GC_BGD], 0)
cv.Set(mask[mask == cv.GC_PR_BGD], 0)
cv.Set(mask[mask == cv.GC_FGD], 255)
cv.Set(mask[mask == cv.GC_PR_FGD], 255)
cv.Rectangle(image,(150,100),(300,300),(0,0,0),2,0)

result = cv.CreateMat(image.rows, image.cols, cv.CV_8UC3)

cv.ShowImage("Image", image)
cv.ShowImage("mask", mask)
cv.WaitKey(0)