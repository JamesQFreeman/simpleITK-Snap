from typing import Tuple

import cv2
import SimpleITK as sitk
import numpy as np
from numpy import ndarray


def imageResize(image: ndarray, shape: Tuple[int, int], padding: bool = True):
    if padding:
        old_shape = image.shape[:2]
        ratio = min(shape[0]/old_shape[0], shape[1]/old_shape[1])
        new_shape = (int(ratio*old_shape[1]), int(ratio*old_shape[0]))
        resized = cv2.resize(image, new_shape)

        delta_h = shape[1] - new_shape[1]
        delta_w = shape[0] - new_shape[0]
        top, bottom = delta_h//2, delta_h-(delta_h//2)
        left, right = delta_w//2, delta_w-(delta_w//2)

        padded = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT,
                                    value=0)
        return padded
    else:
        return cv2.resize(image, (shape[1], shape[0]))


def readNiiToArray(imgDir: str) -> ndarray:
    return sitk.GetArrayFromImage(sitk.ReadImage(imgDir))


def to255(img: ndarray) -> ndarray:
    _min = np.min(img)
    _max = np.max(img)
    result = (img - _min)/(_max-_min) * 255
    return result.astype(np.uint8)


class View3D():
    def __init__(self, imgDir: str, displaySize: Tuple[int, int], isSpacingEqual:True) -> None:
        self.data = to255(readNiiToArray(imgDir))
        self.shape = self.data.shape
        self.displaySize = displaySize
        self.padding = isSpacingEqual
        self.x = 0
        self.y = 0
        self.z = 0

    def getXSlice(self, x: int) -> ndarray:
        return imageResize(self.data[x, :, :], self.displaySize, self.padding)

    def getYSlice(self, y: int) -> ndarray:
        return imageResize(self.data[:, y, :], self.displaySize, self.padding)

    def getZSlice(self, z: int) -> ndarray:
        return imageResize(self.data[:, :, z], self.displaySize, self.padding)

