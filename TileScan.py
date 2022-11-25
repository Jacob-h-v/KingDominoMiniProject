import cv2 as cv
import numpy as np

from HSVConvertion import SplitHSV
from AreaMatching import GetArea, CropArea
from CrownFinder import FindCrowns

def IdentifyTiles(image):

    imageInput = image
    template = cv.imread("Resources/CrownTemplate.jpg")

    # Load RGB sample tiles ------------------------------------------------------
    forest = cv.imread("Resources/TileTemplates/Color/ForestColor.png")
    grass = cv.imread("Resources/TileTemplates/Color/GrassColor.png")
    mine = cv.imread("Resources/TileTemplates/Color/MineColor.png")
    sand = cv.imread("Resources/TileTemplates/Color/SandColor.png")
    wastes = cv.imread("Resources/TileTemplates/Color/WastesColor.png")
    water = cv.imread("Resources/TileTemplates/Color/WaterColor2.png")
    # Load Hue sample tiles ------------------------------------------------------
    forestHue = cv.imread("Resources/TileTemplates/H/ForestHue.png")
    grassHue = cv.imread("Resources/TileTemplates/H/GrassHue.png")
    mineHue = cv.imread("Resources/TileTemplates/H/MineHue.png")
    sandHue = cv.imread("Resources/TileTemplates/H/SandHue.png")
    wastesHue = cv.imread("Resources/TileTemplates/H/WastesHue.png")
    waterHue = cv.imread("Resources/TileTemplates/H/WaterHue2.png")
    # Load Saturation tiles -----------------------------------------------
    forestSaturation = cv.imread("Resources/TileTemplates/S/ForestSaturation.png")
    grassSaturation = cv.imread("Resources/TileTemplates/S/GrassSaturation.png")
    mineSaturation = cv.imread("Resources/TileTemplates/S/MineSaturation.png")
    sandSaturation = cv.imread("Resources/TileTemplates/S/SandSaturation.png")
    wastesSaturation = cv.imread("Resources/TileTemplates/S/WastesSaturation.png")
    waterSaturation = cv.imread("Resources/TileTemplates/S/WaterSaturation2.png")
    # Load Value tiles ------------------------------------------------------------------
    forestValue = cv.imread("Resources/TileTemplates/V/ForestValue.png")
    grassValue = cv.imread("Resources/TileTemplates/V/GrassValue.png")
    mineValue = cv.imread("Resources/TileTemplates/V/MineValue.png")
    sandValue = cv.imread("Resources/TileTemplates/V/SandValue.png")
    wastesValue = cv.imread("Resources/TileTemplates/V/WastesValue.png")
    waterValue = cv.imread("Resources/TileTemplates/V/WaterValue2.png")

    # Declaring variables for later use
    row = 0
    column = 0
    match = False
    matches = 0
    identifiedTiles = np.zeros((5, 5), dtype=np.uint8)
    identifiedCrowns = np.zeros((5, 5), dtype=np.uint8)

    # Calculate mean values for the samples
    meanHueForest = np.mean(forestHue)
    meanHueGrass = np.mean(grassHue)
    meanHueMine = np.mean(mineHue)
    meanHueSand = np.mean(sandHue)
    meanHueWastes = np.mean(wastesHue)
    meanHueWater = np.mean(waterHue)
    # ----------------------------------
    meanValueForest = np.mean(forestValue)
    meanValueGrass = np.mean(grassValue)
    meanValueMine = np.mean(mineValue)
    meanValueSand = np.mean(sandValue)
    meanValueWastes = np.mean(wastesValue)
    meanValueWater = np.mean(waterValue)
    # -----------------------------------
    meanSaturationForest = np.mean(forestSaturation)
    meanSaturationGrass = np.mean(grassSaturation)
    meanSaturationMine = np.mean(mineSaturation)
    meanSaturationSand = np.mean(sandSaturation)
    meanSaturationWastes = np.mean(wastesSaturation)
    meanSaturationWater = np.mean(waterSaturation)

    # Putting sample mean values into arrays so the "r" loop can use them as identifiers
    templateH = [0, meanHueForest, meanHueGrass, meanHueMine, meanHueSand, meanHueWastes, meanHueWater]
    templateS = [0, meanSaturationForest, meanSaturationGrass, meanSaturationMine, meanSaturationSand, meanSaturationWastes,
             meanSaturationWater]
    templateV = [0, meanValueForest, meanValueGrass, meanValueMine, meanValueSand, meanValueWastes, meanValueWater]

    # Loop over sets of coordinates in the tile array
    for i in range(1, 6):
        row = i
        for j in range(1, 6):
            column = j
            # Crop out a part of the image corresponding to the tile's coordinate
            x_start, y_start, x_end, y_end = GetArea(imageInput, row, column)
            region = CropArea(imageInput, x_start, y_start, x_end, y_end)

            # Check for crowns on the cropped out region
            matchCountFinal = FindCrowns(region, template, 0.75)
            identifiedCrowns[j - 1, i - 1] = matchCountFinal
            matchCountFinal = 0

            # Split the tile image into H, S and V channels
            regionHSV = SplitHSV(region)
            regionHue = regionHSV[:, :, 0]
            regionSat = regionHSV[:, :, 1]
            regionVal = regionHSV[:, :, 2]
            regionMeanHue = np.mean(regionHue)
            regionMeanSat = np.mean(regionSat)
            regionMeanVal = np.mean(regionVal)
            identifiedTiles[j - 1, i - 1] = 0

            # Compare region to sample using absolute values
            for r in range(1, 7):
                templateHue = templateH[r]
                templateSat = templateS[r]
                templateVal = templateV[r]
                hueVariance = abs(templateHue - regionMeanHue)
                satVariance = abs(templateSat - regionMeanSat)
                valVariance = abs(templateVal - regionMeanVal)

                if hueVariance < 15 and valVariance < 25 and satVariance < 35:
                    matches += 1
                    identifiedTiles[j - 1, i - 1] = r

    return identifiedTiles, identifiedCrowns