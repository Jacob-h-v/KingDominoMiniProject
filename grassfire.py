from collections import deque
import numpy as np
import cv2 as cv

img = np.array([[2, 6, 1, 1, 1],
                [2, 1, 1, 1, 2],
                [2, 5, 0, 1, 2],
                [2, 5, 6, 2, 2],
                [1, 6, 6, 2, 4]], dtype=np.uint8)
crownsArray = np.array([[0, 0, 0, 0, 0],
                        [0, 0, 1, 2, 1],
                        [0, 0, 0, 0, 0],
                        [0, 1, 0, 2, 1],
                        [0, 0, 0, 1, 0]], dtype=np.uint8)


def ignite_pixel(image, coordinate, id):
    y, x = coordinate
    burn_queue = deque()

    if image[y, x] == 1 or 2 or 3 or 4 or 5 or 6:
        currentType = image[y, x]
        crownCount = 0
        connectedTiles = 0

        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if image[y, x] == currentType:
            image[y, x] = id
            crownCount += crownsArray[y, x]
            connectedTiles += 1

            if x + 1 < image.shape[1] and image[y, x + 1] == currentType:
                burn_queue.append((y, x + 1))
            if y + 1 < image.shape[0] and image[y + 1, x] == currentType:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and image[y, x - 1] == currentType:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and image[y - 1, x] == currentType:
                burn_queue.append((y - 1, x))

        #print(image)
        #print(burn_queue)
        #input()

        if len(burn_queue) == 0:
            scoreCount = crownCount * connectedTiles
            print(
                f"Tile: {y},{x}. Crown count: {crownCount}. Connected tiles: {connectedTiles}. ScoreCount: {scoreCount}. burn = 0 return")
            connectedTiles = 0
            crownCount = 0
            return id + 50, scoreCount
            print(img)
    connectedTiles = 0
    crownCount = 0
    print(f"Tile: {y},{x}. Crown count: {crownCount}. Connected tiles: {connectedTiles}. ScoreCount: {scoreCount}. bottom return")
    return id, scoreCount


def grassfire(image):
    next_id = 50
    totalScore = 0
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            next_id, points = ignite_pixel(image, (y, x), next_id)
            totalScore += points
    return totalScore

TotalScore = grassfire(img)

print(F"Points on the board: {TotalScore}")