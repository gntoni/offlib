import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "offlib",
    version = "0.1.0",
    author = "Toni Gabas",
    author_email = "a.gabas@aist.go.jp",
    description = ("A library to load 3D objects in OFF format file "
                                   "https://en.wikipedia.org/wiki/OFF_(file_format)"),
    license = "GPLv3",
    keywords = "OFF 3D object file format",
    url = "http://packages.python.org/an_example_pypi_project",
    py_modules=['offlib'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
