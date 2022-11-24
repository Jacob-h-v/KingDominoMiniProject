# Imported libraries
import cv2 as cv
from HSVConvertion import SplitHSV
from TileScan import IdentifyTiles
from Grassfire import grassfire


# 1) read inputs
inputImage = cv.imread("Resources/CroppedAndPerspectiveCorrected/1.jpg")
template = cv.imread("Resources/CrownTemplate.jpg")


# 2) identify tiles and check for crowns on each tile
identifiedTiles, identifiedCrowns = IdentifyTiles(inputImage)
print(identifiedTiles)
print(identifiedCrowns)


# 3) Get points by checking for connected tiles and multiplying by number of crowns on each set of tiles
scoreCount = grassfire(identifiedTiles, identifiedCrowns)
print(scoreCount)

# 5) display outcome


# cv.waitKey(0)
