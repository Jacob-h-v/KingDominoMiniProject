import cv2 as cv

cropping = False
showCropping = True
x_start, y_start, x_end, y_end = 0, 0, 0, 0

def MouseCrop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping, showCropping

    # Record (x, y) coords if left mouse button is being held down
    if event == cv.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # if mouse is moving, record where to
    elif event == cv.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
    # if left mouse button is released
    elif event == cv.EVENT_LBUTTONUP:
        # Record coords where mouse was released
        x_end, y_end = x, y
        cropping = False
        showCropping = False


def TemplateCropping(image):
    cv.namedWindow("image")
    cv.setMouseCallback("image", MouseCrop)

    while showCropping:
        i = image.copy()
        if not cropping:
            cv.imshow("image", image)
        elif cropping:
            cv.rectangle(i, (x_start, y_start), (x_end, y_end), (0, 0, 255), 2)
            cv.imshow("image", i)
        cv.waitKey(1)
    # close all open windows
    cv.destroyAllWindows()
    result = [x_start, y_start, x_end, y_end]
    return result

def Crop(image, x_start, y_start, x_end, y_end):
    originalImage = image.copy()
    referencePoint =[(x_start, y_start), (x_end, y_end)]
    if len(referencePoint) == 2: # check if two points were found
        roi = originalImage[referencePoint[0][1]:referencePoint[1][1], referencePoint[0][0]:referencePoint[1][0]]
        cv.imwrite("Resources/CrownTemplate.jpg", roi)
    return roi
