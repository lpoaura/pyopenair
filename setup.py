import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyopenair",
    version="1.0.0",
    author="@lpofredc",
    author_email="frederic.cloitre@lpo.fr",
    maintainer="@lpofredc",
    maintainer_email="frederic.cloitre@lpo.fr",
    packages=["pyopenair"],
    description="A simple python package to convert geo data to OpenAir format",
    long_description=long_description,
    url="https://github.com/lpoaura/pyopenair",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE Version 3",
        "Operating System :: OS Independent",
    ],
    keywords=["openair", "paragliding", "wkt2openair", "geo2openair", "airspace"],
    python_requires=">=3.6",
    install_requires=["shapely>=1.7.1"],
)
