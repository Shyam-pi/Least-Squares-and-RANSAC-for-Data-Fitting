import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getTrack(disp_vid = 'True', disp_plot = 'True'):
    cap = cv2.VideoCapture('ball.mov')
 
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    track = []

    n = 0
    
    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            if n == 0:
                first = frame # Extracting the first frame of the video for plotting purposes
                n += 1

            frame_og = frame.copy()

            r_thresh = frame[:,:,2] > 120
            g_thresh = frame[:,:,1] < 60
            b_thresh = frame[:,:,0] < 60

            thresh = r_thresh & g_thresh & b_thresh
            coords = np.where(thresh)
            frame[thresh] = 0 #Putting the thresholded pixels to 0 (black pixels)

            if coords[0].size != 0:
                position = [np.mean(coords[1]),np.mean(coords[0])]
                track.append(position)
        
            # Display the resulting frame
            if disp_vid:
                cv2.imshow('hello',frame)
        
            # Press Q on keyboard to  exit
            if disp_vid:
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
    
    # Break the loop
        else: 
            break
    
    # When everything done, release the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()

    track = np.array(track)
    if disp_plot:
        fig, ax = plt.subplots()
        im = ax.imshow(cv2.cvtColor(first, cv2.COLOR_BGR2RGB))
        ax.scatter(track[:,0], track[:,1], s=2, color='red')
        ax.set_xlabel('X coordinates')
        ax.set_ylabel('Y coordinates')
        ax.set_title('Trajectory of the ball plotted with the first frame as background')
        
        plt.show()

    return first, track

def main():
    getTrack(disp_vid = True)

if __name__ == "__main__":
    main()
