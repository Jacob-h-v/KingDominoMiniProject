# This is the beginning of the King Domino mini project

# Imported libraries
import cv2 as cv
import numpy as np

# 1) Read input image.
inputImage = cv.imread("Resources/CroppedAndPerspectiveCorrected/1.jpg")

# 2) Pre-process input image (change to grayscale or hsv?, remove noise?).
hsv_conversion = np.zeros(inputImage.shape, dtype=np.uint8)
for y, row in enumerate(inputImage):
    for x, uintpixel in enumerate(row):
        pixel = uintpixel.astype(np.float64)/255

        R = pixel[2]
        G = pixel[1]
        B = pixel[0]

        V = pixel.max()
        S = 0
        if V != 0:
            S = (V-pixel.min())/V
        H = 0
        if R == G == B:
            H = 0
        elif V == pixel[2]:
            H = (60 * (G-B))/(V-pixel.min())
        elif V == G:
            H = 120 + (60*(B-R)) / (V-pixel.min())
        elif V == R:
            H = 240 + (60*(R-G)) / (V-pixel.min())

        if H < 0:
            H += 360

        H /= 2
        S *= 255
        V *= 255
        hsv_conversion[y, x, 0] = H
        hsv_conversion[y, x, 1] = S
        hsv_conversion[y, x, 2] = V


# 3) Read or generate template.

# 4) Pre-process template.

# 5) Check template for similarities against slices of input image.

# display image output
cv.imshow("inputImage", inputImage)
cv.imshow("H channel", hsv_conversion[:, :, 0])
cv.imshow("S channel", hsv_conversion[:, :, 1])
cv.imshow("V channel", hsv_conversion[:, :, 2])
cv.waitKey(0)
