import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft2, fftshift

import SimpleITKSnap as sis
from SimpleITKSnap.Extension import pltExtension, imgExtension
from SimpleITKSnap.utils.ImageUtils3D import normalizeToGrayScale8


# FEATURE 1: Extension, in a single line! 
# Support both matplotlib and numpy array,
# everything you have in 2D, use it in 3D without modification.
@imgExtension
def FFT(array, x, *_):
    s = np.log(np.abs(fftshift(fft2(array[x]))))
    return s, "Spectrum"


@pltExtension
def histogram(array, x, *_):
    plt.hist(array[x].flatten(), 64)
    return "Histogram"


# edges = cv2.Canny(img,100,200) -> If it is a 2D image
@imgExtension
def Canny(img, x, y, z):
    img = normalizeToGrayScale8(img[:, y, :])
    edges = cv2.Canny(img, 100, 200)
    return edges, "Canny"


sis.fileshow('CTA.nii.gz', Canny)


# FEATURE 2: In-place 3D imshow, Why not use 3D like 2D
# You never have to save use SimpleITK, then open ITK-SNAP, then,
# find your file in dozens of other images, finally, open it.
# myArray = np.arange(0, 256 * 256 * 256).reshape(256, 256, 256)
# sis.imshow(myArray, histogram)
