import cv2.cv as cv

orig = cv.LoadImage("../img/road.png")
im = cv.CreateMat(orig.height / 5, orig.width / 5, cv.CV_8UC3)
cv.Resize(orig,im) #resize the original image

src = cv.GetSubRect(im, (10,10,30,30))

minSat = 65

hsv = cv.CreateImage(cv.GetSize(src), 8, 3)
cv.CvtColor(src, hsv, cv.CV_BGR2HSV)


# Extract the H and S planes
h_plane = cv.CreateMat(src.rows, src.cols, cv.CV_8UC1)
s_plane = cv.CreateMat(src.rows, src.cols, cv.CV_8UC1)
cv.Split(hsv, h_plane, s_plane, None, None)
planes = [h_plane, s_plane]

#s_plane = cv.Threshold(s_plane, s_plane, minSat, 255, cv.CV_THRESH_BINARY)

h_bins = 30
s_bins = 32
hist_size = [h_bins, s_bins]

# hue varies from 0 (~0 deg red) to 180 (~360 deg red again */
h_ranges = [0, 180]
# saturation varies from 0 (black-gray-white) to
# 255 (pure spectrum color)
s_ranges = [0, 255]
ranges = [h_ranges, s_ranges]
scale = 10
hist = cv.CreateHist([h_bins, s_bins], cv.CV_HIST_ARRAY, ranges, 1)
cv.CalcHist([cv.GetImage(i) for i in planes], hist)

#SetHistogramm ???
#Normalize

im2 = cv.LoadImage("../img/build.png")
hsv2 = cv.CreateImage(cv.GetSize(im2), 8, 3)
cv.CvtColor(im2, hsv2, cv.CV_BGR2HSV)
h_plane2 = cv.CreateImage(cv.GetSize(im2), 8, 1)
s_plane2 = cv.CreateImage(cv.GetSize(im2), 8, 1)
cv.Split(hsv2, h_plane2, s_plane2, None, None)


res = cv.CreateImage((im2.width,im2.height), 8, 3)
cv.CalcBackProject([h_plane2,s_plane2], res, hist)

cv.MeanShift(res, (10,10,30,30), (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 10, 0.01))
#hist_img = cv.CreateImage((h_bins*scale, s_bins*scale), 8, 3)

cv.ShowImage("Image", hsv2)

cv.WaitKey(0)