# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np

image_path = r'C:\Users\Swathi Pulipati\Downloads\swath_signature.jpg'
directory = r'C:\Swathi\Comp Sci\is\signature'

image = cv2.imread(image_path, 0)

thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)[1]

transparent_image = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGBA)

transparent_image[np.where((transparent_image == [255, 255, 255, 255]).all(2))] = [
    0, 0, 0, 0
]

window_name = 'image'
cv2.imshow('original', image)
cv2.imshow(window_name, transparent_image)

cv2.imwrite(directory+"\\transparent_image.png", transparent_image)
cv2.waitKey(0)

cv2.destroyAllWindows()


