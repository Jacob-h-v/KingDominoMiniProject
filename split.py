import cv2 as cv

img = cv.imread('Resources/CroppedAndPerspectiveCorrected/1.jpg')
for x in range(0,img.shape[0],img.shape[0]//5):
    for y in range(0,img.shape[1],img.shape[1]//5):
        cv.imwrite(f"Resources/SplitImages/img_{x//100}_{y//100}.jpg",img[y:y+img.shape[0]//5, x:x+img.shape[1]//5])
