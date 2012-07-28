import cv2.cv as cv

im = cv.LoadImageM("img/alkaline.jpg")

#Access a specific pixel
print im[3,3]

print cv.Get1D(im, 3)

print cv.Get2D(im, 3, 3) # etc..

#cv.GetND(im, [3,3,3,3]) for a 4 dimension array

col0 = cv.GetCol(im, 0) #Return the first column
cols = cv.GetCols(im, 0, 10) # Return a matrix of the ten first column

row = cv.GetRow(im, 0) #Return the first row (first pixels line)
rows = cv.GetRows(im, 0, 10) # Return the ten first rows of the image

#---------------------------


#Iterate throught pixels
red_sum = 0
green_sum = 0
blue_sum = 0
c = 0
for i in range(0,im.rows-1):
    for j in range(0,im.cols-1):
        c= c +1
        red_sum += im[i,j][0]
        green_sum += im[i,j][1]
        blue_sum += im[i,j][2]
print red_sum, green_sum, blue_sum, c

dur = cv.GetTickCount() #Calculate time between two points
print cv.GetTickCount() - dur



#2
li = cv.InitLineIterator(im, (0, 0), (im.rows, im.cols))
red_sum = 0
green_sum = 0
blue_sum = 0
c = 0
for (r, g, b) in li:
    red_sum += r
    green_sum += g
    blue_sum += b
    c = c + 1
print red_sum, green_sum, blue_sum, c


# 3
li = cv.InitLineIterator(im, (0, 0), (im.rows, im.cols))
print [sum(c) for c in zip(*li)]

