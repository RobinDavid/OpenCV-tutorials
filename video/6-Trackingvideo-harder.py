import cv2.cv as cv

capture = cv.CaptureFromFile('img/micnew.avi')

#-- Informations about the video --
nbFrames = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_COUNT))
fps = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS)
wait = int(1/fps * 1000/1)
width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
#For recording
#codec = cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FOURCC)
#writer=cv.CreateVideoWriter("img/output.avi", int(codec), int(fps), (width,height), 1) #Create writer with same parameters
#----------------------------------

prev_gray = cv.CreateImage((width,height), 8, 1) #Will hold the frame at t-1
gray = cv.CreateImage((width,height), 8, 1) # Will hold the current frame

output = cv.CreateImage((width,height), 8, 3)

prevPyr = cv.CreateImage((height / 3, width + 8), 8, cv.CV_8UC1)
currPyr = cv.CreateImage((height / 3, width + 8), 8, cv.CV_8UC1)

max_count = 500
qLevel= 0.01
minDist = 10

begin = True

initial = []
features = []
prev_points = []
curr_points = []

for f in xrange( nbFrames ):

    frame = cv.QueryFrame(capture)
    
    cv.CvtColor(frame, gray, cv.CV_BGR2GRAY) #Convert to gray
    cv.Copy(frame, output)
    
    
    if (len(prev_points) <= 10): #Try to get more points
        #Detect points on the image
        features = cv.GoodFeaturesToTrack(gray, None, None, max_count, qLevel, minDist)
        prev_points.extend(features) #Add the new points to list
        initial.extend(features) #Idem

    if begin:
        cv.Copy(gray, prev_gray) #Now we have two frames to compare
        begin = False
        
    #Compute movement
    curr_points, status, err = cv.CalcOpticalFlowPyrLK(prev_gray, gray, prevPyr, currPyr, prev_points, (10, 10), 3, (cv.CV_TERMCRIT_ITER|cv.CV_TERMCRIT_EPS,20, 0.03), 0)
    
    #If points status are ok and distance not negligible keep the point
    k = 0
    for i in range(len(curr_points)):
        nb =  abs( int(prev_points[i][0])-int(curr_points[i][0]) ) + abs( int(prev_points[i][1])-int(curr_points[i][1]) )
        if status[i] and  nb > 2 :
            initial[k] = initial[i]
            curr_points[k] = curr_points[i]
            k += 1
            
    curr_points = curr_points[:k]
    initial = initial[:k]
    #At the end only interesting points are kept
    
    #Draw the line between the first position of a point and the
    #last recorded position of the same point
    for i in range(len(curr_points)):
        cv.Line(output, (int(initial[i][0]),int(initial[i][1])), (int(curr_points[i][0]),int(curr_points[i][1])), (255,255,255))
        cv.Circle(output, (int(curr_points[i][0]),int(curr_points[i][1])), 3, (255,255,255))


    cv.Copy(gray, prev_gray)
    prev_points = curr_points

    
    cv.ShowImage("The Video",  output)
    cv.WriteFrame(writer, output)
    cv.WaitKey(wait)