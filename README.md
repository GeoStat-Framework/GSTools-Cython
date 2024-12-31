# Welcome to GSTools-Cython
[![GMD](https://img.shields.io/badge/GMD-10.5194%2Fgmd--15--3161--2022-orange)](https://doi.org/10.5194/gmd-15-3161-2022)
[![Build Status](https://github.com/GeoStat-Framework/GSTools-Cython/workflows/Continuous%20Integration/badge.svg?branch=main)](https://github.com/GeoStat-Framework/GSTools-Cython/actions)
[![Coverage Status](https://coveralls.io/repos/github/GeoStat-Framework/GSTools-Cython/badge.svg?branch=main)](https://coveralls.io/github/GeoStat-Framework/GSTools-Cython?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gstools-cython/badge/?version=latest)](https://geostat-framework.readthedocs.io/projects/gstools-cython/en/stable/?badge=stable)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

<p align="center">
<img src="https://raw.githubusercontent.com/GeoStat-Framework/GSTools/main/docs/source/pics/gstools.png" alt="GSTools-LOGO" width="251px"/>
</p>

<p align="center"><b>Get in Touch!</b></p>
<p align="center">
<a href="https://github.com/GeoStat-Framework/GSTools/discussions"><img src="https://img.shields.io/badge/GitHub-Discussions-f6f8fa?logo=github&style=flat" alt="GH-Discussions"/></a>
<a href="mailto:info@geostat-framework.org"><img src="https://img.shields.io/badge/Email-GeoStat--Framework-468a88?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbDpzcGFjZT0icHJlc2VydmUiIHdpZHRoPSI1MDAiIGhlaWdodD0iNTAwIj48cGF0aCBkPSJNNDQ4IDg4SDUyYy0yNyAwLTQ5IDIyLTQ5IDQ5djIyNmMwIDI3IDIyIDQ5IDQ5IDQ5aDM5NmMyNyAwIDQ5LTIyIDQ5LTQ5VjEzN2MwLTI3LTIyLTQ5LTQ5LTQ5em0xNiA0OXYyMjZsLTIgNy0xMTUtMTE2IDExNy0xMTd6TTM2IDM2M1YxMzdsMTE3IDExN0wzOCAzNzBsLTItN3ptMjE5LTYzYy0zIDMtNyAzLTEwIDBMNjYgMTIxaDM2OHptLTc5LTIzIDQ2IDQ2YTM5IDM5IDAgMCAwIDU2IDBsNDYtNDYgMTAxIDEwMkg3NXoiIHN0eWxlPSJmaWxsOiNmNWY1ZjU7ZmlsbC1vcGFjaXR5OjEiLz48L3N2Zz4=" alt="Email"/></a>
<a href="https://twitter.com/GSFramework"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/GSFramework?style=social"></a>
</p>


## Installation

This is the Cython backend for the Geo-Statistical Toolbox [GSTools](https://github.com/GeoStat-Framework/GSTools).
It is not ment to be installed directly.

### conda

GSTools can be installed via [conda][conda_link] on Linux, Mac, and Windows.
Install the package by typing the following command in a command terminal:

    conda install gstools

In case conda forge is not set up for your system yet, see the easy to follow
instructions on [conda forge][conda_forge_link]. Using conda, the parallelized
version of GSTools should be installed.


### pip

GSTools can be installed via [pip][pip_link] on Linux, Mac, and Windows.
On Windows you can install [WinPython][winpy_link] to get Python and pip
running. Install the package by typing the following command in a command terminal:

    pip install gstools

To install the latest development version via pip, see the
[documentation][doc_install_link].
One thing to point out is that this way, the non-parallel version of GSTools
is installed. In case you want the parallel version, follow these easy
[steps][doc_install_link].


## Citation

If you are using GSTools in your publication please cite our paper:

> Müller, S., Schüler, L., Zech, A., and Heße, F.:
> GSTools v1.3: a toolbox for geostatistical modelling in Python,
> Geosci. Model Dev., 15, 3161–3182, [https://doi.org/10.5194/gmd-15-3161-2022](https://doi.org/10.5194/gmd-15-3161-2022), 2022.

You can cite the Zenodo code publication of GSTools by:

> Sebastian Müller & Lennart Schüler. GeoStat-Framework/GSTools. Zenodo. [https://doi.org/10.5281/zenodo.1313628](https://doi.org/10.5281/zenodo.1313628)

If you want to cite a specific version, have a look at the [Zenodo site](https://doi.org/10.5281/zenodo.1313628).


## Documentation

- GSTools: [https://gstools.readthedocs.io/](https://gstools.readthedocs.io/)
- GSTools-Cython: [https://gstools-cython.readthedocs.io/](https://gstools-cython.readthedocs.io/)

## Cython backend

This package is the cython backend implementation for GSTools.


## Requirements

- [NumPy >= 1.20.0](https://www.numpy.org)


## Contact

You can contact us via <info@geostat-framework.org>.


## License

[LGPLv3][license_link] © 2018-2025

[license_link]: https://github.com/GeoStat-Framework/GSTools-Cython/blob/main/LICENSE
[pip_link]: https://pypi.org/project/gstools
[conda_link]: https://docs.conda.io/en/latest/miniconda.html
[conda_forge_link]: https://github.com/conda-forge/gstools-feedstock#installing-gstools
[winpy_link]: https://winpython.github.io/
[doc_install_link]: https://geostat-framework.readthedocs.io/projects/gstools/en/stable/#pip
