import cv2.cv as cv

image=cv.LoadImage('img/alkaline.jpg', cv.CV_LOAD_IMAGE_COLOR)

#Load the haar cascade
hc = cv.Load("../haarcascades/haarcascade_frontalface_alt.xml")

#Detect face in image
faces = cv.HaarDetectObjects(image, hc, cv.CreateMemStorage(), 1.2,2, cv.CV_HAAR_DO_CANNY_PRUNING, (0,0) )

for ((x,y,w,h),stub) in faces:

    face = cv.GetSubRect(image, (x,y,w,h)) #Get the coordinate of the face in a rectangle
    
    cv.Smooth(face,face,cv.CV_BLUR, 15,15) #Blur the face for instance

    cv.Rectangle(image,(int(x),int(y)),(int(x)+w,int(y)+h),(0,255,0),2,0) #Draw a rectangle around the face

cv.ShowImage("Face detect", image)
cv.WaitKey(0)
