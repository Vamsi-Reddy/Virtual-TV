# importing the required packages
import cv2
import numpy as np

# laoding the first video (video containing the frame)
cap = cv2.VideoCapture('frame2.mp4')
# loading the second video
val = cv2.VideoCapture('temp.mp4')
# finding the width of the second video
width = val.get(cv2.CAP_PROP_FRAME_WIDTH )
# finding the height of the second video
height = val.get(cv2.CAP_PROP_FRAME_HEIGHT )
# finding the width of the first video
tvw = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
# finding the height of the first video
tvh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )

# Lucas kanade most used default params
lk_params = dict(winSize = (15, 15),
maxLevel = 4,
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# function to take the four corner points of the frame and creating a mask 
# which can be used to make the polygon region enclosed by the four corners black.
def getMask(points):
  # converting the numpy array so that dtype of the numpy array is int32
	points = points.astype('int32')
  # initializing the mask size same as the size of the first video.
	mask = np.ones((int(tvh),int(tvw)), dtype=np.uint8)
  # now using the filloply function we make the polygon region defined by the points numpy array black
  # in the previously created mask.
	cv2.fillPoly(mask, pts = [points], color =(0,0,0))
  # returning the mask created.
	return mask

# defining a list corners whcih contains the corners of the frame.
corners = []
cnt = 1
ret, frame = cap.read()
# function used to make user define the corners of the frame initially.
def selectCorners(event, x, y, flags, params):
    global cnt
    # storing the corner position in the corners list when mouse left button is used.
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        corners.append(point) 
        cv2.putText(frame, str(len(corners)), (x, y), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
    # after choosing all the 4 corners user should press right button so that the algorithm continues.
    if event == cv2.EVENT_RBUTTONDOWN:
        cnt = cnt+1

cv2.namedWindow("Frame")
# call back function so that the mouse clicks are treated as we expect (i.e as per the rules defined in the selectCorners function).
cv2.setMouseCallback('Frame', selectCorners)

# bellow lines of code make sure that the program waits till all the four corners of the 
# frame is selected by the user.
while(cnt != 6):
  cv2.imshow('Frame', frame)
  if len(corners) == cnt:
    cv2.circle(frame, corners[cnt-1], 5, (255, 0, 0), 2)
    cnt = cnt + 1
  cv2.waitKey(1)

# initializing the variables oldframe and oldcorners which are used by the calcOpticalFlowPyrLK
# funciton.
oldframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
oldcorners = np.asarray(corners, dtype=np.float32)

while(True):
  # reading the frames (note: not the tv frame) from the first video   
  ret, frame = cap.read()
  # reading the frames (note: not the tv frame) from the second video   
  ret2 , valframe = val.read()
  # we stop if either first video or second video is finished
  if ret == True and ret2 == True:
    # converting the frame from the first video to gray scale.
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # using the calcOpticalFlowPyrLK function which takes the old frame (note: not the tv frame) and the current 
    # frame (note: not the tv frame), and the old positions of the corners then the function calculates the new position of the corners. 
    newcorners, status, error = cv2.calcOpticalFlowPyrLK(oldframe, grayImg, oldcorners, None, **lk_params)
    # update the oldframe variable.
    oldframe = grayImg
    # update the oldcorners variable. 
    oldcorners = newcorners
    # pt1 defines the four corner points of the second video
    pt1 = np.float32([[0,0],[width,0], [width,height], [0,height]])
    # marking the newly found corners using the calcOpticalFlowPyrLK function
    for corner in newcorners:
      x, y = corner
      # function used to mark the corners
      cv2.circle(frame, (int(x),int(y)), 5, (0, 255, 0), -1)
    # getting the perspective transform using the getPerspectiveTransform function.
    # arguments passed are the four corners of the second video stored in the pt1 variable 
    # and the newcorners variable which contains the newly updated corners of the tv frame.
    matrix = cv2.getPerspectiveTransform(pt1, newcorners)
    # warpPerspective function is used to apply the previously found matrix on the second video.
    # we also make sure that the size of the resultant image is same as the size of the first video.
    result = cv2.warpPerspective(valframe, matrix, (int(tvw), int(tvh)))
    # now we use the getMask function 
    mask = getMask(newcorners)
    # once we get the mask we apply this mask for each frame (note: not the tv frame) of the 
    # first video (which is defined by the frame vairable) i.e we apply the mask in every iteration 
    # for the frame in the first video.
    newtv = cv2.bitwise_and(frame, frame, mask = mask)
    # we combine the newtv variable which contains the tv frame region blacked out in a frame (note: not the tv frame)
    # of the first video and the result which is the perspective transformed version of a frame (note: not the tv frame) 
    # of the second video. this is nothing but the desired output which is shown using the imshow function of the cv2.
    cv2.imshow("frame", newtv+result)
    # the below code is to ensure that we quit the output video when we press the key 'q' on the keyboard.
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  # the below code is to ensure that we exit when either first video or second video is finished.
  else: 
    break

# Closes all the frames once we reach end of the code.
cv2.destroyAllWindows()