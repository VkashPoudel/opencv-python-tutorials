import cv2

"""return video from the camera"""
camera = cv2.VideoCapture(0)

"""Checking if the camera is True or False, 
        If true then read camera"""
while(True):
    
    """Capture frame-by-frame reading camera data to frame, ret=return frame"""
    ret, frame = camera.read()    

    """Display the resulting frame with custom Name='Display Frame' """
    cv2.imshow('Display Frame', frame)

    """# understand waitkey by uncommenting and testing output"""
    cv2.waitKey(1)
    # cv2.waitKey(0)

    """In Terminal,PRESS Ctrl + c to terminate program"""

    """---The function waitKey waits for a key event ---

    1.waitKey(0) will display the window infinitely 
    until any keypress (it is suitable for image display).
    
    2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed. 
    Since the OS has a minimum time between switching threads, 
    the function will not wait exactly 1 ms, it will wait at least 1 ms, 
    depending on what else is running on your computer at that time.
    
    **So, if you use waitKey(0) you see a still image 
    until you actually press something while for waitKey(1) 
    the function will show a frame for at least 1 ms only.** """



