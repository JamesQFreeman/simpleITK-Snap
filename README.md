<div align="center">
  <img width="700px" src="logo.png">
</div>

## Overview
SimpleITKSnap is a 3D-image visualization tool. SimpleITKSnap is developed to bridge the gap between 3D-image process
programming and its visualization. Comparing to the existing method, SimpleITKSnap have these advantage:
1. "In-place" display like matplotlib: ```sis.imshow(yourArray)```. 
You don't need to save your processed result to disk, open ITK-SNAP, find the file and load it again.
2. Extension-based design, meet your visualization demand by writing your own extension. 
The extension development requires minimal code and is super easy to develop.


## Install
First, clone this repo to your local environment:

```bash
git clone https://github.com/JamesQFreeman/simpleITK-Snap.git
```

Then use pip to install the dependency package:

```bash
pip install -r requirements.txt
```

Then you are ready to go!

## Usage

### In-place Mode
You can open 3D image in python code.
```python
import SimpleITKSnap as sis
from SimpleITKSnap.Extension import histogram
array = np.arange(0,256*256*256).reshape(256,256,256)
sis.imshow(array, histogram)
```

Let's see an example of a brain CT image:
### Application Mode
To open an image, simply type:

```bash
python simpleITK-Snap -f YourFile.nii.gz
```

![A CTA image opened in simpleITK-Snap](./demo.gif)


## Dependency
- python3
- SimpleITK
- numpy
- opencv-python
- PyQt5


## Developer
JamesQFreeman(wsheng@sjtu.edu.cn)