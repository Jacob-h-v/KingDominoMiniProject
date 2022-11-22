import cv2 as cv
import numpy as np


def GetArea(image, tileRow, tileColumn):
    input = image.copy()
    input = np.array(input, dtype=np.uint8)
    tileSize = input.shape
    tileSizeRows = len(input) // 5
    tileSizeColumns = len(input[0]) // 5
    x_start = tileSizeRows * (tileRow - 1)
    x_end = tileSizeRows * tileRow
    y_start = tileSizeColumns * (tileColumn - 1)
    y_end = tileSizeColumns * tileColumn
    return x_start, y_start, x_end, y_end


def CropArea(image, x_start, y_start, x_end, y_end):
    originalImage = image.copy()
    referencePoint =[(x_start, y_start), (x_end, y_end)]
    if len(referencePoint) == 2: # check if two points were found
        roi = originalImage[referencePoint[0][1]:referencePoint[1][1], referencePoint[0][0]:referencePoint[1][0]]
        cv.imwrite("Resources/TempArea.jpg", roi)
    return roi