import cv2 as cv
from AreaMatching import CropArea, GetArea
from HSVConvertion import SplitHSV
image = cv.imread("Resources/CroppedAndPerspectiveCorrected/6.jpg")


avgSaturationForest = np.mean(forestSaturation)
avgSaturationGrass = np.mean(grassSaturation)
avgSaturationMine = np.mean(mineSaturation)
avgSaturationSand = np.mean(sandSaturation)
avgSaturationWastes = np.mean(wastesSaturation)
avgSaturationWater = np.mean(waterSaturation)
