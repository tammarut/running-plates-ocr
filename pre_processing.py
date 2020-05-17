import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)


# Convert to gray image
def conv_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Rescale
def resize(image):
    return cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)


# erosion and followed by dilation
def opening(image):
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# Blur to reduce noise
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# Threshold
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    m = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, m, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


def pre_image(image):
    path = 'images/'

    original = cv2.imread(path + image)
    temp = conv_grayscale(original)
    temp = resize(temp)
    temp = opening(temp)
    temp = remove_noise(temp)
    temp = thresholding(temp)
    after = deskew(temp)

    return after
