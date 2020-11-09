import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyopenair",
    version="0.1.1",
    author="@lpofredc",
    author_email="frederic.cloitre@lpo.fr",
    maintainer="@lpofredc",
    maintainer_email="frederic.cloitre@lpo.fr",
    packages=["pyopenair"],
    description="A simple python package to convert geo data to OpenAir format",
    long_description="""************************************
pyOpenair, a WKT 2 OpenAir converter
************************************

A simple package to convert geo data from WKT to `OpenAir format <http://www.winpilot.com/usersguide/userairspace.asp>`_.

This project has been developped by LPO Auvergne-Rhône-Alpes to improve `GeoTrek-admin <https://github.com/GeotrekCE/Geotrek-admin>`_ by adding openair file export format to sensitivity module for aerial areas.


Documentation
#############

`<https://pyopenair.readthedocs.io/en/latest/>`_

Licence
#######

`GNU GPLv3 <https://www.gnu.org/licenses/gpl.html>`_

## Team

* `@lpofredc <https://github.com/lpofredc/>`_ (`LPO Auvergne-Rhône-Alpes <https://github.com/lpoaura/>`_), main developper
* `@BPascal-91 <https://github.com/BPascal-91>`_ for advice, tests and recommendations


.. image:: https://raw.githubusercontent.com/lpoaura/biodivsport-widget/master/images/LPO_AuRA_l250px.png
    :align: center
    :height: 100px
    :alt: alternate text
""",
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
