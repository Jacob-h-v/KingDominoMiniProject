import cv2 as cv
from AreaMatching import CropArea, GetArea
from HSVConvertion import SplitHSV
image = cv.imread("Resources/CroppedAndPerspectiveCorrected/1.jpg")

x_start, y_start, x_end, y_end = GetArea(image, 3, 4)
roi = CropArea(image, x_start, y_start, x_end, y_end)

roiHSV = SplitHSV(roi)
roiH = roiHSV[:, :, 0]
roiS = roiHSV[:, :, 1]
roiV = roiHSV[:, :, 2]

cv.imwrite("Resources/TileTemplates/Color/WaterColor2.png", roi)
cv.imwrite("Resources/TileTemplates/H/WaterHue2.png", roiH)
cv.imwrite("Resources/TileTemplates/S/WaterSaturation2.png", roiS)
cv.imwrite("Resources/TileTemplates/V/WaterValue2.png", roiV)



