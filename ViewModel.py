from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
import SimpleITK as sitk
from utils.ImageIO import getArrayFromFig
from utils.ImageUtils2D import resizeImage
from utils.ImageUtils3D import normalizeToGrayScale8


class Data3D:
    # Calculations happened in View3DCore
    def __init__(self, img: ndarray):
        self.rawData = img
        self.shape = self.rawData.shape
        self.maxVal = np.max(self.rawData)
        self.minVal = np.min(self.rawData)


class View3D:
    def __init__(self, imgDir: str, displaySize: Tuple[int, int]) -> None:
        sitkImg = sitk.ReadImage(imgDir)
        self.spacing = sitkImg.GetSpacing()
        self.data = Data3D(sitk.GetArrayFromImage(sitkImg))
        self.grayScale8 = normalizeToGrayScale8(self.data.rawData)
        self.displaySize = displaySize

    def getXSlice(self, x: int) -> ndarray:
        return resizeImage(self.grayScale8[x, :, :], self.displaySize)

    def getYSlice(self, y: int) -> ndarray:
        return resizeImage(self.grayScale8[:, y, :], self.displaySize)

    def getZSlice(self, z: int) -> ndarray:
        return resizeImage(self.grayScale8[:, :, z], self.displaySize)

    def getHistogram(self) -> ndarray:
        fig = plt.figure(figsize=(self.displaySize[0] // 100, self.displaySize[1] // 100))
        ax = fig.add_subplot(111)
        ax.hist(self.data.rawData.flatten(), 128, [self.data.minVal, self.data.maxVal])
        return getArrayFromFig(fig)
