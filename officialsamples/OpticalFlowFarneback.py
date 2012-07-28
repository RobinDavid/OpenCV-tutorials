#!/usr/bin/env python

import cv2.cv as cv

class FBackDemo:
    def __init__(self):
        self.capture = cv.CaptureFromCAM(0)
        self.mv_step = 16
        self.mv_scale = 1.5
        self.mv_color = (0, 255, 0)
        self.cflow = None
        self.flow = None
        
        cv.NamedWindow( "Optical Flow", 1 )

        print( "Press ESC - quit the program\n" )

    def draw_flow(self, flow, prevgray):
        """ Returns a nice representation of a hue histogram """

        cv.CvtColor(prevgray, self.cflow, cv.CV_GRAY2BGR)
        for y in range(0, flow.height, self.mv_step):
            for x in range(0, flow.width, self.mv_step):
                fx, fy = flow[y, x]
                cv.Line(self.cflow, (x,y), (int(x+fx),int(y+fy)), self.mv_color)
                cv.Circle(self.cflow, (x,y), 2, self.mv_color, -1)
        cv.ShowImage("Optical Flow", self.cflow)

    def run(self):
        first_frame = True
        
        while True:
            frame = cv.QueryFrame( self.capture )

            if first_frame:
                gray = cv.CreateImage(cv.GetSize(frame), 8, 1)
                prev_gray = cv.CreateImage(cv.GetSize(frame), 8, 1)
                flow = cv.CreateImage(cv.GetSize(frame), 32, 2)
                self.cflow = cv.CreateImage(cv.GetSize(frame), 8, 3)
                
            cv.CvtColor(frame, gray, cv.CV_BGR2GRAY)
            
            if not first_frame:
                cv.CalcOpticalFlowFarneback(prev_gray, gray, flow,
                    pyr_scale=0.5, levels=3, winsize=15,
                    iterations=3, poly_n=5, poly_sigma=1.2, flags=0)
                self.draw_flow(flow, prev_gray)
                c = cv.WaitKey(7)
                if c in [27, ord('q'), ord('Q')]:
                    break
                    
            prev_gray, gray = gray, prev_gray        
            first_frame = False

if __name__=="__main__":
    demo = FBackDemo()
    demo.run()
