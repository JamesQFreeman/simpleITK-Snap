from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from cv2 import cvtColor, COLOR_GRAY2RGB
from numpy import ndarray
from numpy.fft import fft2, fftshift

from SimpleITKSnap.utils.ImageIO import getArrayFromFig


def pltExtension(extension):
    def wrapper(*args):
        fig = plt.figure(figsize=(4, 4))
        text = extension(*args)
        return getArrayFromFig(fig), text

    return wrapper


def imgExtension(extension):
    def wrapper(*args):
        img, text = extension(*args)
        if img.dtype != np.uint8:
            img = (255 * (img - img.min()) / (img.max() - img.min())).astype(np.uint8)
        if len(img.shape) == 2:
            img = cvtColor(img, COLOR_GRAY2RGB)
        return img, text

    return wrapper


@pltExtension
def histogram(array: ndarray, x: int, *_) -> str:
    plt.hist(array[x].flatten(), 64)
    return "Histogram of the {}th slice".format(x + 1)


def bone(array: ndarray, x: int, y: int, z: int) -> Tuple[ndarray, str]:
    pass


@imgExtension
def FFT(array: ndarray, x: int, *_) -> Tuple[ndarray, str]:
    s = np.log(np.abs(fftshift(fft2(array[x]))))
    return s, "Magnitude spectrum of the {}th slice".format(x + 1)
