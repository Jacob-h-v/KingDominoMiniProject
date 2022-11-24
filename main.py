# Imported libraries
import cv2 as cv
from HSVConvertion import SplitHSV
from TileScan import IdentifyTiles
from Grassfire import grassfire


# 1) read inputs
inputImage = cv.imread("Resources/CroppedAndPerspectiveCorrected/1.jpg")
template = cv.imread("Resources/CrownTemplate.jpg")

# crop to play field if needed

# 2) identify tiles and check for crowns on each tile
identifiedTiles, identifiedCrowns = IdentifyTiles(inputImage)
print(identifiedTiles)
print(identifiedCrowns)


# 3) Get point-giving stuff
scoreCount = grassfire(identifiedTiles, identifiedCrowns)
print(scoreCount)

# split image to H S and V channels. Might be useful for checking hue / value channels when matching areas
hsvImage = SplitHSV(inputImage)
H = hsvImage[:, :, 0]
S = hsvImage[:, :, 1]
V = hsvImage[:, :, 2]

# Split play field into tiles



# check for connected areas and count them

# Multiply connected area score by number of crowns (bounding boxes) in area

# 4) disregard the rest

# 5) display outcome

# cv.imshow("HSV Image", hsvImage)
# cv.imshow("H", H)
# cv.imshow("S", S)
# cv.imshow("V", V)
# cv.imshow("OutputFinal", outputFinal)
# cv.imshow("template", template)
# cv.imshow("template90", template90)
# cv.imshow("template180", template180)
# cv.imshow("template270", template270)
# cv.imshow("Output1", output1)
# cv.imshow("Output2", output2)
# cv.imshow("Output3", output3)
# cv.waitKey(0)
