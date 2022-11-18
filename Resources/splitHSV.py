import numpy as np

def SplitHSV(image):
    inputImage = image
    hsv_conversion = np.zeros(inputImage.shape, dtype=np.uint8)
    for y, row in enumerate(inputImage):
        for x, uintpixel in enumerate(row):
            pixel = uintpixel.astype(np.float64) / 255

            R = pixel[2]
            G = pixel[1]
            B = pixel[0]

            V = pixel.max()
            S = 0
            if V != 0:
                S = (V - pixel.min()) / V
            H = 0
            if R == G == B:
                H = 0
            elif V == pixel[2]:
                H = (60 * (G - B)) / (V - pixel.min())
            elif V == G:
                H = 120 + (60 * (B - R)) / (V - pixel.min())
            elif V == R:
                H = 240 + (60 * (R - G)) / (V - pixel.min())

            if H < 0:
                H += 360

            H /= 2
            S *= 255
            V *= 255
            hsv_conversion[y, x, 0] = H
            hsv_conversion[y, x, 1] = S
            hsv_conversion[y, x, 2] = V
