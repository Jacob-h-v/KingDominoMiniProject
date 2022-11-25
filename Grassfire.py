# Basic grassfire script source: Kode gennemgang, billedbehandling lecture 7

from collections import deque


def IgniteTile(tiles, coordinate, id, crownsArray):
    y, x = coordinate
    burn_queue = deque()

    # Check if current coordinate has a value matching a tile type
    if tiles[y, x] == 1 or 2 or 3 or 4 or 5 or 6:
        currentType = tiles[y, x]
        crownCount = 0
        connectedTiles = 0
        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if tiles[y, x] == currentType:
            # If tile is not already burnt, add values to crownCount and connectedTiles
            if tiles[y, x] < 7:
                crownCount += crownsArray[y, x]
                connectedTiles += 1
            tiles[y, x] = id

            if x + 1 < tiles.shape[1] and tiles[y, x + 1] == currentType:
                burn_queue.append((y, x + 1))
            if y + 1 < tiles.shape[0] and tiles[y + 1, x] == currentType:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and tiles[y, x - 1] == currentType:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and tiles[y - 1, x] == currentType:
                burn_queue.append((y - 1, x))

        # when burn_queue is empty, return scoreCount for area and increase id (burn value)
        if len(burn_queue) == 0:
            scoreCount = crownCount * connectedTiles
            return id + 50, scoreCount
    return id


def grassfire(tiles, crownsArray):
    next_id = 50
    totalScore = 0
    # start IgniteTile for each coordinate in given tiles array
    for y, row in enumerate(tiles):
        for x, pixel in enumerate(row):
            next_id, points = IgniteTile(tiles, (y, x), next_id, crownsArray)
            totalScore += points
    return totalScore