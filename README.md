# Virtual-TV
Creating a virtual tv using opencv in python3.

In order to run the code follow the below given steps:

1) Make sure the desired videos which are given as input are changed in the
   source code. (in the variables cap (video which has the frame) and val (video which should be played in the frame)).

2) Now run the code, now you will be presented with a frame (note : not the tv frame) from the first video (cap), 
   now define the four corners (physical corners are easily tracked) of the frame in the clockwise manner.

3) Once the four corners of the frame is selected using the left click of the mouse, press right click.

4) Now you should be able to see the output video playing on the screen.

### Example : 

### INPUT : 

#### Video1 (containing the frame):
![image](https://user-images.githubusercontent.com/70062653/146636173-0573e8f2-5897-49b4-b7fa-8d28ad13e550.png)

#### Video2 (video that should be played on the frame defined on Video1):
![image](https://user-images.githubusercontent.com/70062653/146636223-e4a68864-e14c-4b7b-a0e2-6e05352bc783.png)

#### User Marked corners :
User will be asked to mark the corners in the video1 once the code is executed

Image after the user has defined the corners in the first frame of video1:

![image](https://user-images.githubusercontent.com/70062653/146636262-c1ac0d71-c6aa-4cd3-bbcb-7a8b0ce22daa.png)

### OUTPUT :
Once the frame is defined in the video1, we can see that the video2 starts playing in the frame defined by the user in video1

![image](https://user-images.githubusercontent.com/70062653/146636349-3833f426-b3fd-4a7c-9b79-0b74fabca0d1.png)

