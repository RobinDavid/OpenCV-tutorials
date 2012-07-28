import cv2.cv as cv
import math

im=cv.LoadImage('img/road.png', cv.CV_LOAD_IMAGE_GRAYSCALE)

pi = math.pi #Pi value

dst = cv.CreateImage(cv.GetSize(im), 8, 1)

cv.Canny(im, dst, 200, 200)
cv.Threshold(dst, dst, 100, 255, cv.CV_THRESH_BINARY)

#---- Standard ----
color_dst_standard = cv.CreateImage(cv.GetSize(im), 8, 3)
cv.CvtColor(im, color_dst_standard, cv.CV_GRAY2BGR)#Create output image in RGB to put red lines

lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, 1, pi / 180, 100, 0, 0)
for (rho, theta) in lines[:100]:
    a = math.cos(theta) #Calculate orientation in order to print them
    b = math.sin(theta)
    x0 = a * rho 
    y0 = b * rho
    pt1 = (cv.Round(x0 + 1000*(-b)), cv.Round(y0 + 1000*(a)))
    pt2 = (cv.Round(x0 - 1000*(-b)), cv.Round(y0 - 1000*(a)))
    cv.Line(color_dst_standard, pt1, pt2, cv.CV_RGB(255, 0, 0), 2, 4) #Draw the line

        
#---- Probabilistic ----
color_dst_proba = cv.CreateImage(cv.GetSize(im), 8, 3)
cv.CvtColor(im, color_dst_proba, cv.CV_GRAY2BGR) # idem

rho=1
theta=pi/180
thresh = 50
minLength= 120 # Values can be changed approximately to fit your image edges
maxGap= 20

lines = cv.HoughLines2(dst, cv.CreateMemStorage(0), cv.CV_HOUGH_PROBABILISTIC, rho, theta, thresh, minLength, maxGap)
for line in lines:
    cv.Line(color_dst_proba, line[0], line[1], cv.CV_RGB(255, 0, 0), 2, 8)
'''
n = 0
one_line = cv.CreateMat(im.height, im.width, cv.CV_8U)
cv.Line(one_line, lines[n][0], lines[n][1], (255,255,255), 5)
cv.And(dst, one_line, one_line)
cv.Smooth(one_line, one_line, cv.CV_MEDIAN, 3)
cv.Threshold(one_line, one_line, 128, 255, cv.CV_THRESH_BINARY)

l = []
for x in range(one_line.height):
    for y in range(one_line.width):
        if one_line[x,y]:
            l.append((x,y))

x1, y1, x0, y0 = cv.FitLine(l, cv.CV_DIST_L2, 0, 0.1, 0.1)
print x1, y1, x0, y0

cv.Line(im, (int(x0),int(y0)), (int(x1),int(y1)), (0,0,0),3,8)
'''
cv.ShowImage('Image',im)
cv.ShowImage("Cannied", dst)
cv.ShowImage("Hough Standard", color_dst_standard)
cv.ShowImage("Hough Probabilistic", color_dst_proba)
#cv.ShowImage("Other", one_line)
cv.WaitKey(0)

