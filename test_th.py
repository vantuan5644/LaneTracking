import cv2 as cv
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
def histogram_mask ( gray ):
    img = cv.equalizeHist ( gray )
    ret , histo_th = cv.threshold ( img , thresh=130 , maxval=135 ,  type=cv.THRESH_BINARY )
    return histo_th

img = mpimg.imread('data/test_images/test4.jpg')
gray = cv.cvtColor ( img , cv.COLOR_RGB2GRAY ).astype ( np.uint8 )
result = histogram_mask(gray)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
#f.tight_layout()
ax1.axis('off')
ax1.imshow(img)
ax1.set_title('Original', fontsize=18)
ax2.axis('off')
ax2.imshow(result, cmap='gray')
ax2.set_title('Edges', fontsize=18)
plt.show()