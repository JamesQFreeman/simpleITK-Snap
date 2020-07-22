import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray
from numpy.fft import fft2, fftshift
from utils.ImageIO import getArrayFromFig
from typing import Tuple
from cv2 import cvtColor, COLOR_GRAY2RGB


def histogram(array: ndarray, x: int, *_) -> Tuple[ndarray, str]:
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)
    arrayAtX = array[x]
    ax.hist(arrayAtX.flatten(), 64, [arrayAtX.min(), arrayAtX.max()])
    ax.set(xlabel='Value', ylabel='# Pixel', title='Histogram')
    return getArrayFromFig(fig), "Histogram of the {}th slice".format(x + 1)


def bone(array: ndarray, x: int, y: int, z: int) -> Tuple[ndarray, str]:
    pass


def FFT(array: ndarray, x: int, *_) -> Tuple[ndarray, str]:
    s = np.log(np.abs(fftshift(fft2(array[x]))))
    s = (255 * (s - s.min()) / (s.max() - s.min())).astype(np.uint8)
    return (cvtColor(s, COLOR_GRAY2RGB)), "Magnitude spectrum of the {}th slice".format(x + 1)
