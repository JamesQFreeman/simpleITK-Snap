import numpy as np
import SimpleITKSnap as sis
from SimpleITKSnap.Extension import FFT

array = np.arange(0, 256 * 256 * 256).reshape(256, 256, 256)
sis.imshow(array, FFT)
