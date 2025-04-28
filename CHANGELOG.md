# Changelog

All notable changes to **GSTools-Cython** will be documented in this file.

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


[Unreleased]: https://github.com/GeoStat-Framework/gstools-cython/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/GeoStat-Framework/gstools-cython/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/GeoStat-Framework/gstools-cython/releases/tag/v1.0.0
