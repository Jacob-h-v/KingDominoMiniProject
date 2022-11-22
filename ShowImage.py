import cv2 as cv
image = cv.imread("Resources/TileTemplates/ForestTile.jpg")

cv.imshow("Tile", image)
cv.waitKey(0)
