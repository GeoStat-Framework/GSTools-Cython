# Changelog

All notable changes to **GSTools-Cython** will be documented in this file.

## [1.2.0] - 2025-12

### Changes

- add support for Python 3.14 (incl. free-threaded support)
- move pypy version to 3.11
- add win arm64 wheels (without Python 3.10, since there are no numpy wheels prior to 3.11)
- remove support for Python 3.9 (EOL)
- fix bug in error message in variogram.pyx (undetected by cython<3.1)
- update pyproject.toml and use setuptools>=77
- increased coverage

## [1.1.0] - 2025-04

See [#5](https://github.com/GeoStat-Framework/GSTools-Cython/pull/5)

### Changes

- dropping Python 3.8 ([EOL reached](https://devguide.python.org/versions/))
- adding [musllinux](https://musl.libc.org/) wheels
- adding PyPy wheels (pp39 and pp310)
  - PyPy needs `setuptools<72.2`: https://github.com/pypa/distutils/issues/283
- adding 32bit Windows wheels again (still Tier 1 support in Python)
- adding aarch64 Linux wheels

## [1.0.0] - 2025-02

First release of GSTools-Cython

### Changes
- moved Cython files into this separate package


[Unreleased]: https://github.com/GeoStat-Framework/gstools-cython/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/GeoStat-Framework/gstools-cython/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/GeoStat-Framework/gstools-cython/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/GeoStat-Framework/gstools-cython/releases/tag/v1.0.0
