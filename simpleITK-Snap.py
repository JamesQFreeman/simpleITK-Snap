import argparse
import sys

from PyQt5.QtWidgets import QApplication

from SimpleITKSnap import SimpleITKSnap


def getArgs():
    parser = argparse.ArgumentParser(description='Visualize a 3D image file')
    parser.add_argument('-f', '--file', dest='file', type=str, default=False,
                        help='Load image from a file')
    return parser.parse_args()


if __name__ == '__main__':
    args = getArgs()
    app = QApplication([])
    gallery = SimpleITKSnap(args.file)
    gallery.show()
    sys.exit(app.exec_())
