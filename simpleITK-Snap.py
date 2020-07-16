import sys

from PyQt5.QtWidgets import QApplication

from SimpleITKSnap import SimpleITKSnap

if __name__ == '__main__':
    app = QApplication([])
    gallery = SimpleITKSnap("CTA.nii.gz")
    gallery.show()
    sys.exit(app.exec_())
