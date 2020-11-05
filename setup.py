import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyopenair",
    version="0.1.1",
    author="lpofredc",
    author_email="frederic.cloitre@lpo.fr",
    packages=["pyopenair"],
    description="A simple python package to convert geo data to OpenAir format",
    long_description="""
pyOpenair
=========

pyOpenair is a simple package to convert geo data from wkt to openair
""",
    url="https://github.com/lpoaura/pyopenair",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["shapely>=1.7.1"],
)
