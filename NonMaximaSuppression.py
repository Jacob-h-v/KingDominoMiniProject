import numpy as np

def nonMaxSupp(boundingBox, overlapThreshold):
    # if there are no bounding box, just return empty
    pickedIndexes = []
    if len(boundingBox) == 0:
        return pickedIndexes

    # take coordinates from bounding box
    x1 = boundingBox[:, 0]
    x2 = boundingBox[:, 2]
    y1 = boundingBox[:, 1]
    y2 = boundingBox[:, 3]

    # Compute area of bounding box, then sort by bottom-right y-coords
    area = (x2-x1+1) * (y2-y1+1)
    idxs = np.argsort(y2)

    # Keep looping until no indexes remain in the list
    while len(idxs) > 0:
        # grab last index in the list, add its value to pickedIndexes, then initialize suppression list using last index
        last = len(idxs) - 1
        i = idxs[last]
        pickedIndexes.append(i)
        suppress = [last]

        # Loop over all indexes in the list
        for pos in range(0, last):
            j = idxs[pos]

            # find largest and smallest (x, y) values to indentify start and end of bounding box
            xMax = max(x1[i], x1[j])
            xMin = min(x2[i], x2[j])
            yMax = max(y1[i], y1[j])
            yMin = min(y2[i], y2[j])

            # Calculate height/width of bounding box
            height = max(0, yMin - yMax + 1)
            width = max(0, xMin - xMax + 1)

            # check overlap ratio between calculated box and the box from list
            overlap = float(height*width) / area[j]

            # if overlap exceeds the threshold, suppress the current box
            if overlap > overlapThreshold:
                suppress.append(pos)

        # delete all the indexes that were added to the suppression list
        idxs = np.delete(idxs, suppress)

    # Return unsuppressed bounding boxes
    return boundingBox[pickedIndexes]