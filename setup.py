from setuptools import setup, find_packages

setup(
    name="drowsy_detector",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "dlib",
        "pygame",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "drowsy-detector=src.main:main"
        ]
    },
    author="Aujas Jain",
    description="A Python-based drowsiness detection system using OpenCV and dlib.",
    license="MIT"
)
