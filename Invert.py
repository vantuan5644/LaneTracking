import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import glob
import cv2



#Color and gradient thresholding

# Edge Detection
from source.lanetracker.gradients import get_edges
image = mpimg.imread('data/test_images/test2.jpg')
result = get_edges(image, separate_channels=True)

# Plot the result
# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
# #f.tight_layout()
# ax1.axis('off')
# ax1.imshow(image)
# ax1.set_title('Original', fontsize=18)
# ax2.axis('off')
# ax2.imshow(result)
# ax2.set_title('Edges', fontsize=18)
# plt.show()

#Perspective transform

# Perspective Transform
from source.lanetracker.perspective import flatten_perspective
image = mpimg.imread('data/test_images/test6.jpg')
result, _ = flatten_perspective(image)

# # Plot the result
# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
# #f.tight_layout()
# ax1.axis('off')
# ax1.imshow(image)
# ax1.set_title('Original', fontsize=18)
# ax2.axis('off')
# ax2.imshow(result)
# ax2.set_title('Bird\'s eye view', fontsize=18)

#Finding the line

# Lane Tracking
from source.lanetracker.tracker import LaneTracker

#Plot the result
# for image_name in glob.glob('data/test_images/*.jpg'):
#     calibrated = calibrate(mpimg.imread(image_name))
#     lane_tracker = LaneTracker(calibrated)
#     overlay_frame = lane_tracker.process(calibrated, draw_lane=True, draw_statistics=True)
#     plt.imshow(overlay_frame)
#     plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
#     plt.show()


#Applying pipeline to video

# Export to Video
# from moviepy.editor import VideoFileClip
# video_output_name = 'data/video/project_video_processed.mp4'
# video = VideoFileClip("data/video/project_video.mp4")
# tracker = LaneTracker(calibrate(video.get_frame(0)))
# video_output = video.fl_image(tracker.process)
# video_output.write_videofile(video_output_name, audio=False)

# cap=cv2.VideoCapture('data/video/project_video.mp4')
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.namedWindow('Vd',cv2.WINDOW_AUTOSIZE)
#     tracker = LaneTracker ( calibrate ( frame))
#     cv2.imshow(tracker)
#     k = cv2.waitKey ( 5 ) & 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows ( )