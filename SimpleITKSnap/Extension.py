from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from numpy.fft import fft2, fftshift

from SimpleITKSnap.ExtensionTools import imgExtension, pltExtension


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
