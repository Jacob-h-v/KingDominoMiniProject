from collections import deque
import numpy as np
import cv2 as cv

# img = np.array([[2, 6, 1, 1, 1],
              #  [2, 1, 1, 1, 2],
              #  [2, 5, 0, 1, 2],
              #  [2, 5, 6, 2, 2],
              #  [1, 6, 6, 2, 4]], dtype=np.uint8)
# crownsArray = np.array([[0, 0, 0, 0, 0],
                       # [0, 0, 0, 1, 0],
                       # [0, 1, 0, 0, 0],
                       # [0, 2, 0, 2, 1],
                       # [0, 1, 0, 1, 0]], dtype=np.uint8)
def ignite_pixel(tiles, coordinate, id, crownsArray):
    y, x = coordinate
    burn_queue = deque()

    if tiles[y, x] == 1 or 2 or 3 or 4 or 5 or 6:
        currentType = tiles[y, x]
        crownCount = 0
        connectedTiles = 0
        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if tiles[y, x] == currentType:
            if tiles[y, x] < 7:
                crownCount += crownsArray[y, x]
                connectedTiles += 1
                print(f"Tile: {y},{x}. CrownCount: {crownCount}. Connected tiles: {connectedTiles}")
            tiles[y, x] = id

            if x + 1 < tiles.shape[1] and tiles[y, x + 1] == currentType:
                burn_queue.append((y, x + 1))
            if y + 1 < tiles.shape[0] and tiles[y + 1, x] == currentType:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and tiles[y, x - 1] == currentType:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and tiles[y - 1, x] == currentType:
                burn_queue.append((y - 1, x))
            print(tiles)

        if len(burn_queue) == 0:
            scoreCount = crownCount * connectedTiles
            connectedTiles = 0
            crownCount = 0
            return id + 50, scoreCount
            print(img)
    connectedTiles = 0
    crownCount = 0
    return id, scoreCount


def grassfire(tile, crowns):
    next_id = 50
    tiles = tile
    totalScore = 0
    for y, row in enumerate(tiles):
        for x, pixel in enumerate(row):
            next_id, points = ignite_pixel(tiles, (y, x), next_id, crowns)
            totalScore += points
    return totalScore

# TotalScore = grassfire(img)

# print(F"Points on the board: {TotalScore}")