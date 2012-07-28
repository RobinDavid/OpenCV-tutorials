import cv2.cv as cv


capture=cv.CaptureFromCAM(0)
temp=cv.QueryFrame(capture)
writer=cv.CreateVideoWriter("output.avi", cv.CV_FOURCC("D", "I", "B", " "), 5, cv.GetSize(temp), 1)
#On linux I used to take "M","J","P","G" as fourcc

count=0
while count<50:
    print count
    image=cv.QueryFrame(capture)
    cv.WriteFrame(writer, image)
    cv.ShowImage('Image_Window',image)
    cv.WaitKey(1)
    count+=1
'''

capture = cv.CaptureFromFile('img/mic.avi')

nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))
width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)
codec = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FOURCC)

wait = int(1/fps * 1000/1) #Compute the time to wait between each frame query

duration = (nbFrames * fps) / 1000 #Compute duration

print 'Num. Frames = ', nbFrames
print 'Frame Rate = ', fps, 'fps'

writer=cv.CreateVideoWriter("img/new.avi", int(codec), int(fps), (width,height), 1) #Create writer with same parameters

cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES,80) #Set the number of frames

for f in xrange( nbFrames - 80 ): #Just recorded the 80 first frames of the video
    
    frame = cv.QueryFrame(capture)
    
    print cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_POS_FRAMES)
    
    cv.WriteFrame(writer, frame)
    
    cv.WaitKey(wait)
'''