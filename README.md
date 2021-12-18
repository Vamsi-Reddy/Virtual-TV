# Virtual-TV
Creating a virtual tv using opencv in python3.

In order to run the code follow the below given steps:

1) Make sure the desired videos which are given as input are changed in the
   source code. (in the variables cap (video which has the frame) and val (video which should be played in the frame)).

2) Now run the code, now you will be presented with a frame (note : not the tv frame) from the first video (cap), 
   now define the four corners (physical corners are easily tracked) of the frame in the clockwise manner.

3) Once the four corners of the frame is selected using the left click of the mouse, press right click.

4) Now you should be able to see the output video playing on the screen.
