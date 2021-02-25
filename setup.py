import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
readme = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="pnoise",
    version="0.1.0",
    description="Vectorized port of Processing noise() function",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Antoine Beyeler",
    author_email="abeyeler@ab-ware.com",
    url="https://github.com/plottertools/pnoise",
    license="LGPL 2.1",
    packages=["pnoise"],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19",
        "setuptools",
    ],
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics",
        "Typing :: Typed",
    ],
)
