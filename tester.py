import cv2 as cv
import numpy as np
import math
from AverageColor import MeanSquaredError, GetAvgColor
from HSVConvertion import SplitHSV
from AreaMatching import GetArea, CropArea
from TemplateMatching import MatchTemplate

imageInput = cv.imread("Resources/CroppedAndPerspectiveCorrected/1.jpg")
imageInput = np.array(imageInput, dtype=np.uint8)
# RGB tiles ------------------------------------------------------
forest = cv.imread("Resources/TileTemplates/Color/ForestColor.png")
grass = cv.imread("Resources/TileTemplates/Color/GrassColor.png")
mine = cv.imread("Resources/TileTemplates/Color/MineColor.png")
sand = cv.imread("Resources/TileTemplates/Color/SandColor.png")
wastes = cv.imread("Resources/TileTemplates/Color/WastesColor.png")
water = cv.imread("Resources/TileTemplates/Color/WaterColor.png")
# Hue tiles ------------------------------------------------------
forestHue = cv.imread("Resources/TileTemplates/H/ForestHue.png")
grassHue = cv.imread("Resources/TileTemplates/H/GrassHue.png")
mineHue = cv.imread("Resources/TileTemplates/H/MineHue.png")
sandHue = cv.imread("Resources/TileTemplates/H/SandHue.png")
wastesHue = cv.imread("Resources/TileTemplates/H/WastesHue.png")
waterHue = cv.imread("Resources/TileTemplates/H/WaterHue.png")
# Saturation tiles -----------------------------------------------
forestSaturation = cv.imread("Resources/TileTemplates/S/ForestSaturation.png")
grassSaturation = cv.imread("Resources/TileTemplates/S/GrassSaturation.png")
mineSaturation = cv.imread("Resources/TileTemplates/S/MineSaturation.png")
sandSaturation = cv.imread("Resources/TileTemplates/S/SandSaturation.png")
wastesSaturation = cv.imread("Resources/TileTemplates/S/WastesSaturation.png")
waterSaturation = cv.imread("Resources/TileTemplates/S/WaterSaturation.png")
# Value tiles ------------------------------------------------------------------
forestValue = cv.imread("Resources/TileTemplates/V/ForestValue.png")
grassValue = cv.imread("Resources/TileTemplates/V/GrassValue.png")
mineValue = cv.imread("Resources/TileTemplates/V/MineValue.png")
sandValue = cv.imread("Resources/TileTemplates/V/SandValue.png")
wastesValue = cv.imread("Resources/TileTemplates/V/WastesValue.png")
waterValue = cv.imread("Resources/TileTemplates/V/WaterValue.png")

hsvImage = SplitHSV(imageInput)
H = hsvImage[:, :, 0]
S = hsvImage[:, :, 1]
V = hsvImage[:, :, 2]
row = 0
column = 0
match = False
matches = 0
identifiedTiles = np.zeros((5, 5), dtype=np.uint8)

avgHueForest = np.mean(forestHue)
avgHueGrass = np.mean(grassHue)
avgHueMine = np.mean(mineHue)
avgHueSand = np.mean(sandHue)
avgHueWastes = np.mean(wastesHue)
avgHueWater = np.mean(waterHue)
# ----------------------------------
avgValueForest = np.mean(forestValue)
avgValueGrass = np.mean(grassValue)
avgValueMine = np.mean(mineValue)
avgValueSand = np.mean(sandValue)
avgValueWastes = np.mean(wastesValue)
avgValueWater = np.mean(waterValue)
# -----------------------------------
avgSaturationForest = np.mean(forestSaturation)
avgSaturationGrass = np.mean(grassSaturation)
avgSaturationMine = np.mean(mineSaturation)
avgSaturationSand = np.mean(sandSaturation)
avgSaturationWastes = np.mean(wastesSaturation)
avgSaturationWater = np.mean(waterSaturation)

template = np.array(6, dtype=np.uint8)
templateH = [0, avgHueForest, avgHueGrass, avgHueMine, avgHueSand, avgHueWastes, avgHueWater]
# templateImg = [0, forestH, grassH, mineH, sandH, wastesH, waterH]

for i in range(1, 6):
    row = i
    for j in range(1, 6):
        column = j
        x_start, y_start, x_end, y_end = GetArea(imageInput, row, column)
        region = CropArea(imageInput, x_start, y_start, x_end, y_end)
        for r in range(1, 7):
            regionHSV = SplitHSV(region)
            templateHue = templateH[r]
            regionHue = regionHSV[:, :, 0]
            regionMeanHue = np.mean(regionHue)
            hueVariance = abs(templateHue - regionMeanHue)
            # MSE = MeanSquaredError(region, b)
            print (i, j, r)
            if hueVariance < 5:
                match = True
                matches += 1
                identifiedTiles[i-1, j-1] = r
                print(match)
                match = False

print (matches)
matches = 0
print(identifiedTiles)




