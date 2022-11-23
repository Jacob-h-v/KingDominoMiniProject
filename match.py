# This is the beginning of the King Domino mini project

# Imported libraries
import cv2 as cv
import imutils
import numpy as np
from CropTemplate import TemplateCropping, Crop
from TemplateMatching import MatchTemplate
from HSVConvertion import SplitHSV


# 1) read inputs
input = cv.imread("Resources/CroppedAndPerspectiveCorrected/1.jpg")
#templateCoordinates = TemplateCropping(input)
#template = Crop(input, templateCoordinates[0], templateCoordinates[1], templateCoordinates[2], templateCoordinates[3])
template = cv.imread("Resources/CrownTemplate.jpg")

# crop to play field if needed

# 2) check for crowns (will need 4 rotations)
template90 = imutils.rotate(template, angle=90)
template180 = imutils.rotate(template, angle=180)
template270 = imutils.rotate(template, angle=270)

output1, matchCount1 = MatchTemplate(input, template, 0.75)
output2, matchCount2 = MatchTemplate(output1, template90, 0.75)
output3, matchCount3 = MatchTemplate(output2, template180, 0.75)
outputFinal, matchCount4 = MatchTemplate(output3, template270, 0.75)
matchCountFinal = matchCount1 + matchCount2 + matchCount3 + matchCount4
print(F"Crowns: {matchCountFinal}")

# 3) Get point-giving stuff

# split image to H S and V channels. Might be useful for checking hue / value channels when matching areas
hsvImage = SplitHSV(input)
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
cv.imshow("OutputFinal", outputFinal)
# cv.imshow("template", template)
# cv.imshow("template90", template90)
# cv.imshow("template180", template180)
# cv.imshow("template270", template270)
cv.imshow("Output1", output1)
cv.imshow("Output2", output2)
cv.imshow("Output3", output3)
cv.waitKey(0)
