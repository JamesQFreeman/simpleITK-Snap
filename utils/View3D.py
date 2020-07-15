import io
from typing import Tuple

import cv2
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk

from numpy import ndarray


def getImageFromFig(fig):
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    buf.seek(0)
    imgArr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(imgArr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def padImage(image: ndarray, newShape: Tuple[int, int]) -> ndarray:
    shape = image.shape
    delta_h = shape[1] - newShape[1]
    delta_w = shape[0] - newShape[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    return cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT,
                              value=0)


def resizeImage(image: ndarray, shape: Tuple[int, int], padding: bool = True) -> ndarray:
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


class View3D():
    def __init__(self, imgDir: str, displaySize: Tuple[int, int], isSpacingEqual: True) -> None:
        self.data = readNiiToArray(imgDir)
        cv2.normalize(self.data, self.data, 0, 255, cv2.NORM_MINMAX)
        self.data = self.data.astype(np.uint8)
        self.data = np.flip(self.data, (0, 1, 2))

        self.shape = self.data.shape
        self.displaySize = displaySize
        self.padding = isSpacingEqual

    def getXSlice(self, x: int) -> ndarray:
        return resizeImage(self.data[x, :, :], self.displaySize, self.padding)

    def getYSlice(self, y: int) -> ndarray:
        return resizeImage(self.data[:, y, :], self.displaySize, self.padding)

    def getZSlice(self, z: int) -> ndarray:
        return resizeImage(self.data[:, :, z], self.displaySize, self.padding)

    def getHistogram(self) -> ndarray:
        fig = plt.figure(figsize=(3,3))
        ax = fig.add_subplot(111)
        ax.hist(self.data.ravel(), 256, [0, 256])
        return getImageFromFig(fig)
