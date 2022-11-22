import cv2 as cv
import numpy as np

from AverageColor import MeanSquaredError, GetAvgColor
from HSVConvertion import SplitHSV
from AreaMatching import GetArea, CropArea
from TemplateMatching import MatchTemplate

imageInput = cv.imread("Resources/CroppedAndPerspectiveCorrected/7.jpg")
imageInput = np.array(imageInput, dtype=np.uint8)
forest = cv.imread("Resources/TileTemplates/ForestTileColor.jpg")
grass = cv.imread("Resources/TileTemplates/GrassTileColor.jpg")
mine = cv.imread("Resources/TileTemplates/MineTileColor.jpg")
sand = cv.imread("Resources/TileTemplates/SandTileColor.jpg")
wastes = cv.imread("Resources/TileTemplates/WastesTileColor.jpg")
water = cv.imread("Resources/TileTemplates/WaterTileColor.jpg")
# hsvImage = SplitHSV(imageInput)
# H = hsvImage[:, :, 0]
# S = hsvImage[:, :, 1]
# V = hsvImage[:, :, 2]
row = 0
column = 0
template = [forest, grass, mine, sand, wastes, water]
match = False
matches = 0
identifiedTiles = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(1, 6):
    row = i
    for j in range(1, 6):
        column = j
        x_start, y_start, x_end, y_end = GetArea(imageInput, row, column)
        region = CropArea(imageInput, x_start, y_start, x_end, y_end)
        for r in range(0, 6):
            nextTile = template[r]
            print(r)
            MSE = MeanSquaredError(region, nextTile)
            print (MSE, i, j, r)
            if MSE < 16000:
                match = True
                matches += 1
                listPos = ((i-1), (j-1))
                identifiedTiles.insert(listPos, r)
                print(match)
                match = False
            elif MSE > 16000:
                print("not a match")
                match = False
print (matches)
matches = 0
print(identifiedTiles)




