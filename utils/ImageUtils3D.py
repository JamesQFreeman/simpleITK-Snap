import cv2
import numpy as np

from numpy import ndarray


def normalizeToGrayScale8(img: ndarray):
    result = img.copy()
    cv2.normalize(img, result, 0, 255, cv2.NORM_MINMAX)
    return result.astype(np.uint8)
