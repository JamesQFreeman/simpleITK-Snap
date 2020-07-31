from functools import wraps

import matplotlib.pyplot as plt
import numpy as np
from cv2 import cvtColor, COLOR_GRAY2RGB
from .utils.ImageUtils import toGray8
from SimpleITKSnap.utils.ImageIO import getArrayFromFig


def pltExtension(extension):
    @wraps(extension)
    def wrapper(*args):
        fig = plt.figure(figsize=(4, 4))
        text = extension(*args)
        return getArrayFromFig(fig), text

    return wrapper


def imgExtension(extension):
    @wraps(extension)
    def wrapper(*args):
        img, text = extension(*args)
        img = toGray8(img)
        # if img.dtype != np.uint8:
        #     img = (255 * (img - img.min()) / (img.max() - img.min())).astype(np.uint8)
        # if len(img.shape) == 2:
        #     img = cvtColor(img, COLOR_GRAY2RGB)
        return img, text

    return wrapper
