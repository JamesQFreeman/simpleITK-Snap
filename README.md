# simpleITK-Snap

It's a Qt-based 3D medical image visualization tool. The code is short thus easy to understand and modify. In short, it is an ITK-Snap in 200 lines!

Let's see an example of a brain CT image.

![A CTA image opened in simpleITK-Snap](./example.gif)


## DEV NOTE

### BUGS TO FIX
1. Fix the position.
2. Resize by imaging spacing.

### FEATURES TO ADD
- Add ```SimpleITKSnap.display(img: ndarray), SimpleITKSnap.show()```
- The lower right widget should be wrote as an extension not a fix format.
- Write some example of extension, like Fourier Transform.args = get_args()