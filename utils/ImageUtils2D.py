import numpy as np
from numpy import ndarray
from typing import Tuple

import cv2


def padImage(image: ndarray, newShape: Tuple[int, int]) -> ndarray:
    shape = image.shape
    delta_h = shape[1] - newShape[1]
    delta_w = shape[0] - newShape[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    return cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
                              value=0)


# TODO: resize by imaging spacing
def resizeImage(image: ndarray, shape: Tuple[int, int]) -> ndarray:
    return cv2.resize(image, (shape[1], shape[0]))
