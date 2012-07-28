import cv2.cv as cv
from time import time

capture=cv.CaptureFromCAM(0)
temp=cv.QueryFrame(capture)

startat=10
sum = 0
count=0

t1= time()
t2 = 0

while count<30:
    print count
    image=cv.QueryFrame(capture)
    t2 = time()
    val = t2 - t1
    print val
    #I ignore the ten first frames because tests shows that the elapsed time value is anormaly too low
    if count > startat:
        sum += val #Add the current value
        print "Avg: ", sum / (count - startat) #Compute the temp average
    t1 = t2 
    count+=1

avg = 1/ (sum / (count - startat))
fps = cv.Round(avg)

print fps, "fps"
