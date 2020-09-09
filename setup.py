import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyopenair",
    version="0.0.1",
    author="lpofredc",
    author_email="frederic.cloitre@lpo.fr",
    packages=['pyopenair'],
    package_data={
        'pyopenair': [
            'schemas/*.txt',
            'test/*.py',
            'test/testfiles/*.openair',
        ]},
    description="A simple python package to convert geo data to OpenAir format",
    long_description="""\
=========
pyKML
=========
pyKML is a Python package for parsing and authoring KML documents. It is based
on the lxml.objectify API (http://codespeak.net/lxml/objectify.html) which
provides Pythonic access to XML documents.
.. figure:: http://pykml.googlecode.com/hg/docs/source/logo/pyKML_logo_200x200.png
   :scale: 100 %
   :alt: pyKML logo
See the Package Documentation for information on installation and usage.
""",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'shapely>=1.7.1',
        'numpy>=1.19.1'
    ],
)
