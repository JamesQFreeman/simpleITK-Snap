from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
import SimpleITK as sitk
from utils.ImageIO import getArrayFromFig
from utils.ImageUtils2D import resizeImage
from utils.ImageUtils3D import normalizeToGrayScale8


class View3D:
    def __init__(self, array: ndarray, displaySize: Tuple[int, int],
                 spacing: Tuple[float, float, float] = (1, 1, 1)) -> None:
        self.data = array
        self.grayScale8 = normalizeToGrayScale8(self.data)
        self.displaySize = displaySize

    def getXSlice(self, x: int) -> ndarray:
        return resizeImage(self.grayScale8[x, :, :], self.displaySize)

    def getYSlice(self, y: int) -> ndarray:
        return resizeImage(self.grayScale8[:, y, :], self.displaySize)

    def getZSlice(self, z: int) -> ndarray:
        return resizeImage(self.grayScale8[:, :, z], self.displaySize)

    def getHistogram(self) -> ndarray:
        fig = plt.figure(figsize=(self.displaySize[0] // 75, self.displaySize[1] // 75))
        ax = fig.add_subplot(111)
        ax.hist(self.data.flatten(), 64, [np.min(self.data), np.max(self.data)])
        ax.set(xlabel='Value', ylabel='# Pixel', title='Histogram')
        return getArrayFromFig(fig)


class FileView3D(View3D):
    def __init__(self, imgDir: str, displaySize: Tuple[int, int]) -> None:
        sitkImg = sitk.ReadImage(imgDir)
        spacing = sitkImg.GetSpacing()
        print('\n\n\n', spacing)
        array = sitk.GetArrayFromImage(sitkImg)
        array = np.flip(array, 0)
        super().__init__(array, displaySize, spacing)
