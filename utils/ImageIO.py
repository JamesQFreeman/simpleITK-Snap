import io

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from numpy import ndarray


def createQPixmapFromArray(img: ndarray, fmt=QImage.Format_Grayscale8) -> QPixmap:
    height, width = img.shape[:2]
    pixelSize = 1 if fmt == QImage.Format_Grayscale8 else 3
    qImg = QImage(img.data, width, height, pixelSize * width, fmt)
    return QPixmap(qImg)


def getArrayFromFig(fig) -> ndarray:
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    plt.close()
    buf.seek(0)
    imgArr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(imgArr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img
