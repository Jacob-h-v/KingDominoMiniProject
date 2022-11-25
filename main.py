# Imported libraries
import cv2 as cv
from TileScan import IdentifyTiles
from Grassfire import grassfire
import imutils
from TemplateMatching import MatchTemplate


# 1) read inputs
inputImage = cv.imread("Resources/CroppedAndPerspectiveCorrected/3.jpg")
template = cv.imread("Resources/CrownTemplate.jpg")
template90 = imutils.rotate(template, angle=90)
template180 = imutils.rotate(template, angle=180)
template270 = imutils.rotate(template, angle=270)
# marking crowns on output
# (this is not where the crowns are *actually* identified for counting. This is merely for human readability)
output1, matchCount1 = MatchTemplate(inputImage, template, 0.75)
output2, matchCount2 = MatchTemplate(output1, template90, 0.75)
output3, matchCount3 = MatchTemplate(output2, template180, 0.75)
outputFinal, matchCount4 = MatchTemplate(output3, template270, 0.75)


# 2) identify tiles and check for crowns on each tile
identifiedTiles, identifiedCrowns = IdentifyTiles(inputImage)
print(identifiedTiles)
print(identifiedCrowns)


# 3) Get points by checking for connected tiles and multiplying by number of crowns on each set of tiles
scoreCount = grassfire(identifiedTiles, identifiedCrowns)
print(scoreCount)

# 5) display outcome
outputCrowns = cv.putText(outputFinal, f"Proposed score: {scoreCount}", (15, 65), 1, 2, (0, 0, 255), 3, cv.LINE_AA)

cv.imshow("score window", outputCrowns)
cv.waitKey(0)
