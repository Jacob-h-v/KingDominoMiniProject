from collections import deque
import numpy as np
import cv2 as cv

img = np.array([[2, 6, 1, 1, 1],
                [2, 1, 1, 1, 2],
                [2, 5, 0, 1, 2],
                [2, 5, 6, 2, 2],
                [1, 6, 6, 2, 4]], dtype=np.uint8)


def ignite_pixel(image, coordinate, id):
    x, y = coordinate
    burn_queue = deque()

    num = image[y, x]
    burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if image[y, x] == 2:
            image[y, x] = id

            if x + 1 < image.shape[1] and image[y, x + 1] == num:
                burn_queue.append((y, x + 1))
            if y + 1 < image.shape[0] and image[y + 1, x] == num:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and image[y, x - 1] == num:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and image[y - 1, x] == num:
                burn_queue.append((y - 1, x))

        #print(image)
        #print(burn_queue)
        #input()

        if len(burn_queue) == 0:
            return id
            print(img)

    #return id


def grassfire(image):
    next_id = 50
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(image, (y, x), next_id)

grassfire(img)

print(img)
cv.imshow("Output", img)
cv.waitKey()