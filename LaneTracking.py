import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec
import glob
import numpy as np
import cv2 as cv
# # Can chinh camera
from source.lanetracker.camera import CameraCalibration
calibrate = CameraCalibration(glob.glob('data/camera_cal/calibration*.jpg'), retain_calibration_images=True)
# # Nhung hinh chessboard tim duoc pattern va corners
# plt.figure(figsize = (11.5, 9))
# gridspec.GridSpec(5, 4)
# for i, image in enumerate(calibrate.calibration_images_success):
#     plt.subplot2grid((5, 4), (i // 4, i % 4), colspan=1, rowspan=1)
#     plt.imshow(image)
#     plt.axis('off')
# print ((calibrate.camera_matrix).astype(np.int))
# plt.show()
# # Nhung hinh chessboard khong tim duoc pattern, tu cac thong so camera, tien hanh can chinh:
# for i, image in enumerate(calibrate.calibration_images_error):
#     f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 2.5))
#     ax1.axis('off')
#     ax1.imshow(image)
#     ax1.set_title('Anh truoc can chinh', fontsize=10)
#     ax2.axis('off')
#     ax2.imshow(calibrate(image))
#     ax2.set_title('Sau khi can chinh', fontsize=10)
# plt.show()

# Color and gradient thresholding

from source.lanetracker.thresholding import get_edgess
# for image_name in glob.glob('data/test_images/curve*.jpg'):
#     image = mpimg.imread(image_name)
#     result = get_edgess(image,separate_channels=False)
#     # Plot the result
#     f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
#     f.tight_layout()
#     ax1.axis('off')
#     ax1.imshow(image)
#     ax1.set_title('Anh goc', fontsize=18)
#     ax2.axis('off')
#     ax2.imshow(result,cmap='gray')
#     ax2.set_title('Anh nhi phan', fontsize=18)
# plt.show()

# Perspective Transform
#
from source.lanetracker.perspective import perspective_transform
# for image_name in glob.glob('data/test_images/curve*.jpg'):
#     image = mpimg.imread(image_name)
#     perspective,_ = perspective_transform(image)
#     result = get_edgess ( perspective , separate_channels=False )
#     f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
#     f.tight_layout()
#     ax1.axis('off')
#     ax1.imshow(image, cmap='gray')
#     ax1.set_title('Anh goc', fontsize=18)
#     ax2.axis('off')
#     ax2.imshow(result,cmap='gray')
#     ax2.set_title('Bien doi phoi canh', fontsize=18)
#     plt.show()


# Draw histogram

# img, _ = perspective_transform(result)
# histogram = np.sum ( img[int ( img.shape[0] / 2 ): , :] , axis=0 )
# # plt.plot(histogram)
# plt.imshow(img)
# plt.show()

#
from source.lanetracker.pipeline import LaneTracker
# for image_name in glob.glob('data/test_images/curve*.jpg'):
#     calibrated = calibrate(mpimg.imread(image_name))
#     lane_tracker = LaneTracker(mpimg.imread(image_name))
#     overlay_frame = lane_tracker.process(calibrated, draw_lane=True, draw_statistics=True)
#     plt.imshow(overlay_frame)
#     mpimg.imsave(image_name.replace('test_images', 'output_images'), overlay_frame)
#     plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
#     plt.show()

# # Applying pipeline to video
# # Export to Video

from moviepy.editor import VideoFileClip
video_output_name = 'data/video/curve_op.mp4'
video = VideoFileClip("data/video/curve.mp4")
tracker = LaneTracker(calibrate(video.get_frame(0)))
video_output = video.fl_image(tracker.process)
video_output.write_videofile(video_output_name, audio=False)
