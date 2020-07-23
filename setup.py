import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimpleITKSnap",  # Replace with your own username
    version="0.1.1-alpha",
    author="JamesQFreeman",
    author_email="wsheng@sjtu.edu.cn",
    description="A Qt-based 3D medical image visualization tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JamesQFreeman/simpleITK-Snap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
