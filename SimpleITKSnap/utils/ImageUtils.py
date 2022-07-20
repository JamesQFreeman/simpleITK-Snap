from typing import Tuple

import cv2
import numpy as np
from numpy import ndarray


def padImage(image: ndarray, newShape: Tuple[int, int]) -> ndarray:
    shape = image.shape
    delta_h = newShape[0] - shape[0]
    delta_w = newShape[1] - shape[1]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    return cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
                              value=0)


def resizeBySpacing(image: ndarray, shape: Tuple[int, int], spacing: Tuple[float, float]) -> ndarray:
    physicalRatio = (image.shape[0] * spacing[0]) / (image.shape[1] * spacing[1])
    orgShape = (image.shape[0], image.shape[1] * physicalRatio)
    zoomRatio = min(shape[0] / orgShape[0], shape[1] / orgShape[0])
    shapeBeforePad = (int(zoomRatio * orgShape[0]), int(zoomRatio * orgShape[1]))
    resized = cv2.resize(image, (shapeBeforePad[1], shapeBeforePad[0]))
    return padImage(resized, shape)


def toGray8(img: ndarray):
    result = img.copy()
    cv2.normalize(img, result, 0, 255, cv2.NORM_MINMAX)
    # print(result.shape)
    return result.astype(np.uint8)
