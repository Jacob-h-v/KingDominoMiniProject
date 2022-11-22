import cv2 as cv
import numpy as np
from NonMaximaSuppression import nonMaxSupp

# def MatchTemplate(image, processed, template):
def MatchTemplate(image, template, thresh):
    image = np.array(image, dtype=np.uint8)
    # processed = np.array(processed, dtype=np.uint8)
    template = np.array(template, dtype=np.uint8)
    templateHeight, templateWidth = template.shape[:2]

    # res = cv.matchTemplate(processed, template, cv.TM_CCOEFF_NORMED)
    res = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    threshold = thresh
    (yCoords, xCoords) = np.where(res >= threshold)

    rects = []
    for (x, y) in zip(xCoords, yCoords):
        rects.append((x, y, x + templateWidth, y + templateHeight))

    pickedIndexes = nonMaxSupp(np.array(rects), 0.1)
    resultAmount = len(pickedIndexes)
    print(resultAmount)

    # Loop over final bounding boxes
    for (startX, startY, endX, endY) in pickedIndexes:
        # draw bounding on output
        cv.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 3)

    # Return the output image
    return image, resultAmount
