# This is the beginning of the King Domino mini project

# Imported libraries
import cv2 as cv
import imutils
import numpy as np
from CropTemplate import TemplateCropping, Crop
from TemplateMatching import MatchTemplate


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
output1, matchCount1 = MatchTemplate(input, template)
output2, matchCount2 = MatchTemplate(output1, template90)
output3, matchCount3 = MatchTemplate(output2, template180)
output4, matchCount4 = MatchTemplate(output3, template270)
matchCountFinal = matchCount1 + matchCount2 + matchCount3 + matchCount4
print(F"Crowns: {matchCountFinal}")

# 3) check for similar areas connected to crown
        # pre-save templates (maybe using H-channel from hsv to look for specific colors)

# 4) disregard the rest

# 5) display outcome

cv.imshow("Output4", output4)
cv.imshow("template", template)
cv.imshow("template90", template90)
cv.imshow("template180", template180)
cv.imshow("template270", template270)
cv.imshow("Output1", output1)
cv.imshow("Output2", output2)
cv.imshow("Output3", output3)
cv.waitKey(0)
