# Welcome to GSTools
[![GMD](https://img.shields.io/badge/GMD-10.5194%2Fgmd--15--3161--2022-orange)](https://doi.org/10.5194/gmd-15-3161-2022)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1313628.svg)](https://doi.org/10.5281/zenodo.1313628)
[![PyPI version](https://badge.fury.io/py/gstools.svg)](https://badge.fury.io/py/gstools)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/gstools.svg)](https://anaconda.org/conda-forge/gstools)
[![Build Status](https://github.com/GeoStat-Framework/GSTools/workflows/Continuous%20Integration/badge.svg?branch=main)](https://github.com/GeoStat-Framework/GSTools/actions)
[![Coverage Status](https://coveralls.io/repos/github/GeoStat-Framework/GSTools/badge.svg?branch=main)](https://coveralls.io/github/GeoStat-Framework/GSTools?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gstools/badge/?version=latest)](https://geostat-framework.readthedocs.io/projects/gstools/en/stable/?badge=stable)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

<p align="center">
<img src="https://raw.githubusercontent.com/GeoStat-Framework/GSTools/main/docs/source/pics/gstools.png" alt="GSTools-LOGO" width="251px"/>
</p>

<p align="center"><b>Get in Touch!</b></p>
<p align="center">
<a href="https://github.com/GeoStat-Framework/GSTools/discussions"><img src="https://img.shields.io/badge/GitHub-Discussions-f6f8fa?logo=github&style=flat" alt="GH-Discussions"/></a>
<a href="https://swung.slack.com/messages/gstools"><img src="https://img.shields.io/badge/Swung-Slack-4A154B?style=flat&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA%2FwD%2FAP%2BgvaeTAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAB3RJTUUH5AYaFSENGSa5qgAABmZJREFUSMeFlltsVNcVhr%2B1z5m7Zzy%2BxaBwcQrGQOpgCAkKtSBQIqJepKhPBULpQ6sKBVWVKqXtSy%2BR0qYXqa2qRmlDCzjBEZGKUCK1TWqlNiGIEKDQBtf4Fki4OIxnxrex53LOXn2YwbjEtOvlHG3tvX%2Btf%2B21%2Fl%2BYJ1QVEbn1vwLYBWwCVgG1lW0ZoA%2FoAQ6LSP%2BdZ%2BeGzAMiIqK%2Bem0GpxNYVeBj3j2b4NCfM2QnfAAaa11al4fZuCZK24owQJ9v%2BbLryIVbd9wVSNUaEWNVtQPYfXHmAD0T32ZJeBM1Q8d0zzMDUpMwAFgLJU%2BxClURw9NfqedLWxMAHSKyR1WNiNhPAM0B6c%2FbdPORTLuOeUMSNkmMBHgyeo32bwwRDMh8bDM%2BZVl0j6uvPrdYknFnSESWzwUzt%2BkyVlUHx7zh5j%2BmPkXBjosjLkWdominiMQ%2BoiEZxuq8OFRXGXJ5K5%2Fde5nha8VlqjooIlZVBcBUiqeqemjGppd1ptfhSpS8pmmN7GVf4whPNY4Di9m%2BMcR03nK3sBbCQeFbv7gBsExVOyp3l6nz1VtjcM4fTK3Uok5IXtPsrHuPevcBXk8d4dWPX6I%2BsIB9wf1s%2B2Y%2FVbFynUIBIeDeplIECiXl5Iv3kbLogogRgbWukfNumT%2FnlYszBxj3hwXg0cQvqXcfYNu5tVyYPE%2B1G8dXn%2BfW72fH49U8sSlOPGr4SccoF4cKs3WzFrY%2BFCMUNmz%2Ba0aeWR1l15JwJ7DaVPpk1YnJ7xIxtQRNjDXRvTx%2F9ef0Tl0g6SYQhAlvmkH%2Fgv74qUaiTSG8ewJ0%2FGgRK5aG8Cts5ouWDa1RxoDRovK9i9MAq1S12QA7b5ROUdBxBIeQ1ACG49m%2FEXPis7Qk3ChHbx6Qw1dgXVeWB7uyDOctP%2Fx6w2zdrIVIyFCyiq8wXlJOZzyAXQbY%2FGGhC8EAilJ%2BVg7ufxU6IAHeSvewfQEadiDuCr%2B6NE1LU4hwUFAF1xFGRkvEjVDlgiPwVqoEsNkAq0ZKp3EIYrFM2xGm7Uc8u%2FzXjHkTmHIHoCiDM73E3IIsDCtRV3gn7QHQ0hTCt0ooKLw%2FWCAM1AcNISOcHSsBrDRAbc7eQMQBFFciHM18kaZIMz3r%2F0HO5mazytsiw%2FmTtCYiGGCkQlltwkEVjMDVmyUA6oIGR%2BDGjAWoM3f2giHAhH%2BFI5nPsDrWxqWNE9S4tUz5k1S7cQ5df4k9S6qY9JRipXtr4w5WQYH0eHkWrqxy8FTn3AvpmFmIqj%2B76EiQjNfHH1JNWFKc3vABj9V9npw%2FRXfmBNsaoTRnRAQDAgqqMJr1KBWUtUmHaR8WRgzAqAH6FgYexqd4R2Yuns5wcLSFK4U36bj%2FdbbUbGdoZoCi3uS%2Bqtt73TlNWygpqXGfZTGXnKesrwkA9BmgZ0noMZT5R0tQ4hzLfo4rhS46W%2F%2BCAn3T7%2BhDySiWMl2RkHArP8dAesKjPixYVbbUBwB6DHB4QWADIamuHPtkhE0t3ZP7ANhe9zgvXP2dfK0pymRJmQLiEYNW6mEVljYGuDzlkwwaHq51AQ4bERkAetvjP2XCT6H480AJeZsB4N7QYt7OnuSROtRXJV2wNNS4qIJvlbUtERJxhxcv5%2FlNWwygV0QGyzKBv%2FP%2ByFfZXf%2ButoR3UuXcS95mKNgxSjpN3qZZFHwUgFPjx5n2c9wo9ktrtcOZtMeWB2NEw4b2thivPLuIS1M%2BAzmrTy4O4ys7Zv1B5fsnVdWCr7PxYf7vej73ex2YeU1VVY9nu7ShG63vRo%2Fe%2FK1%2B518FbXkjo3OjO1XU2LFRzRZ9VdWDczFQ1VsCOHgpd1G%2FcG6jHrj2vPbn%2BjVdHNfr%2BRH92eXva2MPuvxEQpe%2BHdEnzm%2FQf4%2BrRo%2BldMUbGd393oS2dWU0cDSlw1OequrALVG9Q8rLsquqg2OlzLL2Myu1N5eShgB4CjEnSMSJYrX8Oj0t8UH7NMnX0iSDwmhBWRl3tKs9IcmgGRSRZqtqzFwpL4uWWKvWiMjyZKC24%2F1HbsrLn95Pwk3gCpS0yIw%2Fg6clPC2RLc3QmzvJupoARQsvrItxZmtSkkFz6E6Q%2F2m3PFta44jbCaw%2BO3GK7uybnJs8xfXC1fLYCdTz9NIfsCS0mYVhAHp9ZYdr5J%2F%2F127dxUA2AzuBzRUDWVfZlq4YyG6gs9ImdzWQ%2FwFNRlgCFdG5bAAAAABJRU5ErkJggg%3D%3D" alt="Slack-Swung"/></a>
<a href="https://gitter.im/GeoStat-Framework/GSTools"><img src="https://img.shields.io/badge/Gitter-GeoStat--Framework-ed1965?logo=gitter&style=flat" alt="Gitter-GSTools"/></a>
<a href="mailto:info@geostat-framework.org"><img src="https://img.shields.io/badge/Email-GeoStat--Framework-468a88?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbDpzcGFjZT0icHJlc2VydmUiIHdpZHRoPSI1MDAiIGhlaWdodD0iNTAwIj48cGF0aCBkPSJNNDQ4IDg4SDUyYy0yNyAwLTQ5IDIyLTQ5IDQ5djIyNmMwIDI3IDIyIDQ5IDQ5IDQ5aDM5NmMyNyAwIDQ5LTIyIDQ5LTQ5VjEzN2MwLTI3LTIyLTQ5LTQ5LTQ5em0xNiA0OXYyMjZsLTIgNy0xMTUtMTE2IDExNy0xMTd6TTM2IDM2M1YxMzdsMTE3IDExN0wzOCAzNzBsLTItN3ptMjE5LTYzYy0zIDMtNyAzLTEwIDBMNjYgMTIxaDM2OHptLTc5LTIzIDQ2IDQ2YTM5IDM5IDAgMCAwIDU2IDBsNDYtNDYgMTAxIDEwMkg3NXoiIHN0eWxlPSJmaWxsOiNmNWY1ZjU7ZmlsbC1vcGFjaXR5OjEiLz48L3N2Zz4=" alt="Email"/></a>
<a href="https://twitter.com/GSFramework"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/GSFramework?style=social"></a>
</p>

<p align="center"><b>Youtube Tutorial on GSTools</b><br></p>

<p align="center">
<a href="http://www.youtube.com/watch?feature=player_embedded&v=qZBJ-AZXq6Q" target="_blank">
<img src="http://img.youtube.com/vi/qZBJ-AZXq6Q/0.jpg" alt="GSTools Transform 22 tutorial" width="480" height="360" border="0" />
</a>
</p>

## Purpose

<img align="right" width="450" src="https://raw.githubusercontent.com/GeoStat-Framework/GSTools/main/docs/source/pics/demonstrator.png" alt="">

GeoStatTools provides geostatistical tools for various purposes:
- random field generation
- simple, ordinary, universal and external drift kriging
- conditioned field generation
- incompressible random vector field generation
- (automated) variogram estimation and fitting
- directional variogram estimation and modelling
- data normalization and transformation
- many readily provided and even user-defined covariance models
- metric spatio-temporal modelling
- plotting and exporting routines


## Installation


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


## Citation

If you are using GSTools in your publication please cite our paper:

> Müller, S., Schüler, L., Zech, A., and Heße, F.:
> GSTools v1.3: a toolbox for geostatistical modelling in Python,
> Geosci. Model Dev., 15, 3161–3182, https://doi.org/10.5194/gmd-15-3161-2022, 2022.

You can cite the Zenodo code publication of GSTools by:

> Sebastian Müller & Lennart Schüler. GeoStat-Framework/GSTools. Zenodo. https://doi.org/10.5281/zenodo.1313628

If you want to cite a specific version, have a look at the [Zenodo site](https://doi.org/10.5281/zenodo.1313628).


## Documentation for GSTools

You can find the documentation under [geostat-framework.readthedocs.io][doc_link].


## Cython backend

This package is the cython backend implementation for GSTools.


## Requirements

- [NumPy >= 1.20.0](https://www.numpy.org)


## Contact

You can contact us via <info@geostat-framework.org>.


## License

[LGPLv3][license_link] © 2018-2024

[license_link]: https://github.com/GeoStat-Framework/GSTools-Cython/blob/main/LICENSE
