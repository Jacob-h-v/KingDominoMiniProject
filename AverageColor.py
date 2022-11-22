import cv2 as cv
import numpy as np

# inputImage = cv.imread("Resources/TileTemplates/WaterTile.jpg")
# inputImage2 = cv.imread("Resources/TileTemplates/WaterTile.jpg")


def MeanSquaredError(image1, image2):
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    return err

def GetAvgColor(image):
    input = image
    average_color_row = np.average(input, axis=0)
    average_color = np.average(average_color_row, axis=0)
    return average_color
