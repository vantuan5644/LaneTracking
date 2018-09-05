import cv2
from matplotlib import pyplot as plt
import numpy as np
from source.lanetracker.camera import CameraCalibration
from source.lanetracker.window import Window
from source.lanetracker.line import Line
from source.lanetracker.gradients import get_edges
from source.lanetracker.perspective import perspective_transform
from source.lanetracker.tracker import *


# a = np.array ( [[0 , 0 , 0 , 1 , 0 , 1 , 0] ,
#                 [0 , 0 , 0 , 1 , 0 , 1 , 0] ,
#                 [0 , 0 , 0 , 1 , 0 , 1 , 0] ,
#                 [0 , 0 , 0 , 1 , 0 , 1 , 0] ,
#                 [0 , 0 , 0 , 1 , 0 , 1 , 0] ,
#                 [0 , 0 , 0 , 1 , 0 , 1 , 0] ,
#                 [0 , 0 , 0 , 1 , 0 , 1 , 0]] )
# win_indices = (
#         (a.nonzero()[0] >= 3) & (a.nonzero()[0] <= 4) &
#         (a.nonzero()[1] >= 3) & (a.nonzero()[1] <= 4)
# ).nonzero()[0]
# print(a.nonzero()[0])
# print(a.nonzero()[1])
#
# print(a.nonzero()[0] >= 3)
# print(((a.nonzero()[0] >= 3) & (a.nonzero()[0] <= 4) &
#         (a.nonzero()[1] >= 3) & (a.nonzero()[1] <= 4)).nonzero()[0] )
a = np.array([1,2,3,4,5])
print(a.size)